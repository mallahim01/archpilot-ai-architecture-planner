from __future__ import annotations

import json
import os
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Tuple

import anyio
from openai import AsyncOpenAI

import re

_JSON_BLOCK_RE = re.compile(r"\{.*\}", re.DOTALL)

def strip_code_fences(text: str) -> str:
    """
    Removes ```json ... ``` or ``` ... ``` fences if present.
    """
    t = (text or "").strip()
    if t.startswith("```"):
        # remove first fence line
        t = re.sub(r"^```[a-zA-Z0-9_-]*\s*", "", t)
        # remove ending fence
        t = re.sub(r"\s*```$", "", t)
    return t.strip()

def extract_first_json_object(text: str) -> str | None:
    """
    Best-effort: find the first {...} JSON object in the text.
    Works when model adds commentary or multiple blocks.
    """
    t = strip_code_fences(text)
    m = _JSON_BLOCK_RE.search(t)
    if not m:
        return None
    return m.group(0).strip()

# -----------------------------
# 1) Prompt (extract deltas only)
# -----------------------------

EXTRACTOR_SYSTEM = """\
You are a high-recall information extraction engine for a software discovery chat.

You will receive:
- chat_context (object)
- rolling_summary (string)
- batch_messages: a SMALL batch of conversation messages, chronological (oldest -> newest)

Your goal:
Capture ALL useful details from this batch for later requirement/architecture document generation.
Do NOT be conservative. Prefer over-including rather than missing details.

Return STRICT JSON ONLY with this schema:
{
  "discovery_delta": [string],
  "ui_ux_delta": [string],
  "features_journeys_delta": [string],
  "tech_stack_delta": [string],
  "budget_timeline_delta": [string],
  "open_questions_delta": [string]
}

Rules:
- Include every feature, action, workflow, role, screen, integration, constraint, assumption, pricing idea, timeline hint,
  edge-case, and non-functional requirement mentioned.
- It is OK if items are long and contain full context.
- Prefer including exact phrasing/details when possible.
- If a category truly has nothing new in this batch, output [].
- Do NOT output markdown fences/backticks. JSON only.
"""



# -----------------------------
# 2) Data model (final merged state)
# -----------------------------
@dataclass
class ExtractedKnowledge:
    discovery: List[str] = field(default_factory=list)
    ui_ux: List[str] = field(default_factory=list)
    features_journeys: List[str] = field(default_factory=list)
    tech_stack: List[str] = field(default_factory=list)
    budget_timeline: List[str] = field(default_factory=list)
    open_questions: List[str] = field(default_factory=list)

    def _add_unique(self, target: List[str], items: Optional[List[str]]) -> None:
        if not items:
            return
        seen = set(target)
        for x in items:
            x = (x or "").strip()
            if x and x not in seen:
                target.append(x)
                seen.add(x)

    def merge_delta(self, delta: Dict[str, Any]) -> None:
        self._add_unique(self.discovery, delta.get("discovery_delta"))
        self._add_unique(self.ui_ux, delta.get("ui_ux_delta"))
        self._add_unique(self.features_journeys, delta.get("features_journeys_delta"))
        self._add_unique(self.tech_stack, delta.get("tech_stack_delta"))
        self._add_unique(self.budget_timeline, delta.get("budget_timeline_delta"))
        self._add_unique(self.open_questions, delta.get("open_questions_delta"))

    def as_dict(self) -> Dict[str, Any]:
        return {
            "discovery": self.discovery,
            "ui_ux": self.ui_ux,
            "features_journeys": self.features_journeys,
            "tech_stack": self.tech_stack,
            "budget_timeline": self.budget_timeline,
            "open_questions": self.open_questions,
        }


# -----------------------------
# 3) Helpers
# -----------------------------
def ensure_oldest_to_newest(messages_newest_to_oldest: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    # Your messages are currently reversed (newest -> oldest)
    # Convert to oldest -> newest for batch processing:
    return list(reversed(messages_newest_to_oldest))


def chunk_messages(messages_oldest_to_newest: List[Dict[str, Any]], batch_size: int = 4) -> List[List[Dict[str, Any]]]:
    return [messages_oldest_to_newest[i : i + batch_size] for i in range(0, len(messages_oldest_to_newest), batch_size)]

def _safe_parse_json(text: str) -> Dict[str, Any]:
    raw = (text or "").strip()
    candidate = extract_first_json_object(raw) or strip_code_fences(raw)

    try:
        return json.loads(candidate)
    except Exception as e:
        print("JSON PARSE FAILED:", repr(e))
        print("RAW MODEL OUTPUT (first 700 chars):", raw[:700])
        print("CANDIDATE JSON (first 700 chars):", (candidate or "")[:700])
        return {
            "discovery_delta": [],
            "ui_ux_delta": [],
            "features_journeys_delta": [],
            "tech_stack_delta": [],
            "budget_timeline_delta": [],
            "open_questions_delta": [],
        }

def _pretty_batch_preview(batch: List[Dict[str, Any]], max_chars: int = 600) -> str:
    lines = []
    for i, m in enumerate(batch, start=1):
        role = (m.get("role") or "").upper()
        content = (m.get("content") or "").strip().replace("\n", " ")
        if len(content) > max_chars:
            content = content[:max_chars] + "…"
        lines.append(f"{i:02d}. {role}: {content}")
    return "\n".join(lines)


def _build_payload(chat_context: Dict[str, Any], rolling_summary: str, batch: List[Dict[str, Any]]) -> Dict[str, Any]:
    return {
        "rolling_summary": rolling_summary or "",
        "chat_context": chat_context or {},
        "batch_messages": [
            {"role": m.get("role"), "content": m.get("content", "")}
            for m in batch
            if m.get("role") in ("user", "assistant")
        ],
    }


# -----------------------------
# 4) Main extraction function (ASYNC, parallel)
# -----------------------------
async def extract_knowledge_from_chat(
    *,
    chat_context: Dict[str, Any],
    rolling_summary: str,
    messages: List[Dict[str, Any]],
    model: str = "gpt-4.1-mini",
    batch_size: int = 4,
    max_parallel: int = 6,
    api_key: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Step-1 ONLY: Knowledge extraction.

    Inputs:
      - chat_context: your stored context snapshot
      - rolling_summary: optional
      - messages: currently reversed in your system (newest -> oldest)

    Output:
      dict with keys:
        discovery, ui_ux, features_journeys, tech_stack, budget_timeline, open_questions
    """
    api_key = api_key or os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY is not set")

    client = AsyncOpenAI(api_key=api_key)

    # msgs = ensure_oldest_to_newest(messages)
    msgs = messages
    batches = chunk_messages(msgs, batch_size=batch_size)

    extracted = ExtractedKnowledge()
    sem = anyio.Semaphore(max_parallel)

    async def run_one_batch(batch: List[Dict[str, Any]]) -> Dict[str, Any]:
        payload = _build_payload(chat_context, rolling_summary, batch)
        print("Batch/////////////////")
        # print("SYSTEM:")
        # print(EXTRACTOR_SYSTEM)
        # print("PAYLOAD//////////////////////")
        # print(payload)
        print("\n================= BATCH PREVIEW =================")
        print(_pretty_batch_preview(payload["batch_messages"]))
        print("=================================================\n")
        try:

            resp = await client.responses.create(
                model=model,
                input=[
                    {"role": "system", "content": EXTRACTOR_SYSTEM},
                    {"role": "user", "content": json.dumps(payload, ensure_ascii=False)},
                ],
            )
            text = (resp.output_text or "").strip()
            print("Response:.................")
            print(text)
            print("############################")
            return _safe_parse_json(text)
        except Exception as e:
            print("OPENAI CALL FAILED:", repr(e))
            return {
                "discovery_delta": [],
                "ui_ux_delta": [],
                "features_journeys_delta": [],
                "tech_stack_delta": [],
                "budget_timeline_delta": [],
                "open_questions_delta": [],
            }
    # Run batches concurrently (bounded)
    results: List[Dict[str, Any]] = []

    async def guarded(batch: List[Dict[str, Any]]) -> None:
        async with sem:
            results.append(await run_one_batch(batch))
            
    async with anyio.create_task_group() as tg:
        results = [None] * len(batches)

        async def guarded(i: int, batch: List[Dict[str, Any]]) -> None:
            async with sem:
                results[i] = await run_one_batch(batch)

        for i, b in enumerate(batches):
            tg.start_soon(guarded, i, b)

    # Merge
    for delta in results:
        if delta:
            extracted.merge_delta(delta)

    # async with anyio.create_task_group() as tg:
    #     for b in batches:
    #         tg.start_soon(guarded, b)

    # # Merge into final knowledge
    # for delta in results:
    #     extracted.merge_delta(delta)

    return extracted.as_dict()
