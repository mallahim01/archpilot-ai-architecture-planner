from __future__ import annotations

import json
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional

import anyio
from openai import AsyncOpenAI


# -----------------------------
# Config
# -----------------------------
BASE_DIR = Path(__file__).resolve().parents[1]  # app/llm
EXTRACTION_DIR = BASE_DIR / "extraction"
DATA_DIR = EXTRACTION_DIR / "data"
DOCS_DIR = EXTRACTION_DIR / "documents"


# -----------------------------
# Prompts
# -----------------------------
DOC_SYSTEM = """\
You are AI Ventex — an Agentic AI Architect that also communicates clearly to non-technical founders.

Goal:
Write a professional but founder-friendly product document.

Audience:
- Primary: business owner / founder (non-technical).
- Secondary: product + engineering (technical).

Tone:
- Clear, structured, confident, not salesy.
- Explain tech only when needed, with simple language.

Important:
- Be VERY detailed and capture ALL specifics present in the input.
- You MAY expand and structure the content (better wording, clearer grouping),
  but DO NOT invent missing facts.
- If something is missing, state it as an Open Question or Assumption.
- If you need to “guess” a reasonable default, label it explicitly as an Assumption.

Output format:
- Return MARKDOWN only (no code fences).
- Write only the requested section content (not the whole doc again).
"""

SECTION_WRITER_USER = """\
You are writing ONLY this section:

SECTION TITLE:
{title}

SECTION GOAL:
{goal}

SECTION FORMAT:
{format}

CONTEXT (extracted from chat):
{context_json}

ADDITIONAL RULES:
- Include as many concrete details as possible (features, roles, flows, constraints, numbers).
- Use bullet lists + subheadings where helpful.
- Prefer clarity over buzzwords.
"""


@dataclass(frozen=True)
class SectionSpec:
    key: str
    title: str
    goal: str
    format: str


SECTIONS: List[SectionSpec] = [
    SectionSpec(
        key="01_exec_summary",
        title="Executive Summary (Founder-friendly)",
        goal="Explain what is being built, for whom, and why it matters. Include top 5 capabilities.",
        format="2–4 short paragraphs + bullets for top capabilities + 1 line 'Success looks like...'.",
    ),
    SectionSpec(
        key="02_problem_solution",
        title="Problem, Solution, and Business Value",
        goal="Describe the pain points, proposed solution, and measurable business outcomes.",
        format="Headings: Problem, Solution, Business Value (bullets + metrics if present).",
    ),
    SectionSpec(
        key="03_users_roles_flows",
        title="Users, Roles, and High-level User Flows",
        goal="List personas/roles and describe end-to-end flows in simple steps.",
        format="Role list + 3–8 step flows per role (happy path), plus edge cases if present.",
    ),
    SectionSpec(
        key="04_features",
        title="Feature Set (Detailed, Grouped)",
        goal="Convert feature/journey notes into a clean grouped feature list (very detailed).",
        format="Group by modules (Auth, Admin, Booking/Payments, Content, Notifications, etc.) with bullets.",
    ),
    SectionSpec(
        key="05_scope_mvp_v1_v2",
        title="Scope Split: MVP vs V1 vs V2",
        goal="Propose what to ship first vs later based on constraints and complexity.",
        format="3 columns in text form (MVP / V1 / V2), with rationale bullets.",
    ),
    SectionSpec(
        key="06_budget_timeline",
        title="Budget, Timeline, and Tradeoffs",
        goal="Summarize budget/timeline info and show what changes across budget bands.",
        format="Timeline estimate + budget bands (Low/Medium/High) + tradeoffs + risks.",
    ),
    SectionSpec(
        key="07_risks_open_questions",
        title="Risks, Assumptions, and Open Questions",
        goal="Compile all unknowns, risks, and assumptions clearly.",
        format="3 headings: Risks, Assumptions, Open Questions (bullets).",
    ),
    SectionSpec(
        key="08_next_steps",
        title="Next Steps",
        goal="Give a practical next plan: what to confirm, what to prepare, what happens next.",
        format="Checklist + suggested workshop agenda (30–60 minutes).",
    ),
]


# -----------------------------
# IO helpers
# -----------------------------
def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def load_extraction_pack(job_id: str) -> Dict[str, Any]:
    """
    Reads the files you already created:
      {job_id}_discovery.md
      {job_id}_ui_ux.md
      {job_id}_features_journeys.md
      {job_id}_tech_stack.md
      {job_id}_budget_timeline.md
      {job_id}_open_questions.md
      {job_id}_full.json
    """
    pack = {
        "job_id": job_id,
        "discovery": _read_text(DATA_DIR / f"{job_id}_discovery.md"),
        "ui_ux": _read_text(DATA_DIR / f"{job_id}_ui_ux.md"),
        "features_journeys": _read_text(DATA_DIR / f"{job_id}_features_journeys.md"),
        "tech_stack": _read_text(DATA_DIR / f"{job_id}_tech_stack.md"),
        "budget_timeline": _read_text(DATA_DIR / f"{job_id}_budget_timeline.md"),
        "open_questions": _read_text(DATA_DIR / f"{job_id}_open_questions.md"),
        "full_json": json.loads(_read_text(DATA_DIR / f"{job_id}_full.json")),
    }
    return pack


def build_context_payload(pack: Dict[str, Any]) -> Dict[str, Any]:
    """
    Keep it big, because you want high recall.
    This is NOT strict. We want maximum detail preserved.
    """
    return {
        "job_id": pack["job_id"],
        "extraction_files": {
            "discovery": pack["discovery"],
            "ui_ux": pack["ui_ux"],
            "features_journeys": pack["features_journeys"],
            "tech_stack": pack["tech_stack"],
            "budget_timeline": pack["budget_timeline"],
            "open_questions": pack["open_questions"],
        },
        "full_json": pack["full_json"],
    }


# -----------------------------
# OpenAI helpers (robust)
# -----------------------------
def _get_client() -> AsyncOpenAI:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY is not set")
    return AsyncOpenAI(api_key=api_key)


async def _call_openai_markdown(
    client: AsyncOpenAI,
    *,
    model: str,
    system: str,
    user: str,
    max_retries: int = 3,
) -> str:
    """
    Production-ish wrapper with retries.
    """
    last_err: Optional[Exception] = None
    for attempt in range(1, max_retries + 1):
        try:
            resp = await client.responses.create(
                model=model,
                input=[
                    {"role": "system", "content": system},
                    {"role": "user", "content": user},
                ],
            )
            text = (resp.output_text or "").strip()
            if not text:
                raise RuntimeError("Empty model output")
            return text
        except Exception as e:
            last_err = e
            # exponential-ish backoff
            await anyio.sleep(min(2.0 * attempt, 6.0))
    raise RuntimeError(f"OpenAI call failed after {max_retries} retries: {last_err}")


# -----------------------------
# Main: generate ONE document (multi-call)
# -----------------------------
async def generate_founder_brief_document(
    *,
    job_id: str,
    model: str = "gpt-4o",
    out_dir: Path = DOCS_DIR,
) -> Dict[str, str]:
    """
    Creates ONE founder-friendly document as Markdown using multiple API calls.
    Saves:
      - {job_id}_founder_brief.md

    Returns:
      {"md_path": "..."}
    """
    out_dir.mkdir(parents=True, exist_ok=True)

    pack = load_extraction_pack(job_id)
    context_payload = build_context_payload(pack)

    client = _get_client()

    # Keep an outline header + table of contents
    doc_parts: List[str] = []
    doc_parts.append(f"# Founder & Team Brief\n\n**Job ID:** `{job_id}`\n")

    toc_lines = ["## Table of Contents"]
    for s in SECTIONS:
        toc_lines.append(f"- {s.title}")
    doc_parts.append("\n".join(toc_lines) + "\n")

    # Generate sections sequentially (more consistent)
    for s in SECTIONS:
        print(f"\n--- Generating section: {s.key} / {s.title} ---")

        # Optional: log a compact preview for debugging
        # (avoid printing full_json if huge)
        print("Context preview (first 300 chars each):")
        for k, v in context_payload["extraction_files"].items():
            vv = (v or "").replace("\n", " ")
            print(f"  - {k}: {vv[:300]}{'...' if len(vv) > 300 else ''}")

        user_prompt = SECTION_WRITER_USER.format(
            title=s.title,
            goal=s.goal,
            format=s.format,
            context_json=json.dumps(context_payload, ensure_ascii=False),
        )

        section_md = await _call_openai_markdown(
            client,
            model=model,
            system=DOC_SYSTEM,
            user=user_prompt,
        )

        # Ensure section header exists
        if not section_md.lstrip().startswith("#") and not section_md.lstrip().startswith("##"):
            section_md = f"## {s.title}\n\n{section_md}"

        doc_parts.append(section_md.strip() + "\n")

    final_md = "\n\n".join(doc_parts).strip() + "\n"

    md_path = out_dir / f"{job_id}_founder_brief.md"
    md_path.write_text(final_md, encoding="utf-8")

    return {"md_path": str(md_path.resolve())}
