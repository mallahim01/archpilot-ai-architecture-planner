from __future__ import annotations

import json
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional

import anyio
from openai import AsyncOpenAI


# -----------------------------
# Paths (match your existing structure)
# -----------------------------
BASE_DIR = Path(__file__).resolve().parents[1]  # app/llm
EXTRACTION_DIR = BASE_DIR / "extraction"
DATA_DIR = EXTRACTION_DIR / "data"
DOCS_DIR = EXTRACTION_DIR / "documents"


# -----------------------------
# Section specs
# -----------------------------
@dataclass(frozen=True)
class SectionSpec:
    key: str
    title: str
    goal: str
    format: str


REQ_SECTIONS: List[SectionSpec] = [
    SectionSpec(
        key="01_overview",
        title="Overview",
        goal="Summarize what is being built, who it serves, and the core value. Keep it crisp but concrete.",
        format="1–2 paragraphs + bullets: Product, Target users, Core value, Non-goals (if any).",
    ),
    SectionSpec(
        key="02_goals_success",
        title="Goals and Success Criteria",
        goal="Translate objectives into measurable outcomes and acceptance signals.",
        format="Bullets under: Goals, Success Metrics, Acceptance Criteria.",
    ),
    SectionSpec(
        key="03_scope",
        title="Scope",
        goal="Define what is in scope and out of scope for this version.",
        format="Two lists: In Scope / Out of Scope. Add notes if scope depends on budget/timeline.",
    ),
    SectionSpec(
        key="04_personas_roles",
        title="Personas and Roles",
        goal="List roles/personas with responsibilities and permissions (RBAC) if discussed.",
        format="Role table in markdown (Role, Description, Key permissions). If unknown, add Open Questions.",
    ),
    SectionSpec(
        key="05_user_journeys_high_level",
        title="High-level User Journeys",
        goal="Document end-to-end flows for each main role based on extracted journeys.",
        format="Per role: numbered steps. Include edge cases & exceptions if present.",
    ),
    SectionSpec(
        key="06_functional_requirements",
        title="Functional Requirements",
        goal="Generate a detailed, grouped set of functional requirements derived from features/journeys.",
        format="Grouped by modules with MUST/SHOULD/COULD tags. Be very detailed.",
    ),
    SectionSpec(
        key="07_non_functional",
        title="Non-Functional Requirements",
        goal="Capture performance, security, compliance, reliability, scalability, localization, observability, etc.",
        format="Bullets grouped by category. If unknown, propose defaults as Assumptions.",
    ),
    SectionSpec(
        key="08_integrations_data",
        title="Integrations and Data",
        goal="Capture external integrations and key data entities and high-level data flows (NOT schema).",
        format="Integrations list + key entities + brief data flow notes. If missing, add questions.",
    ),
    SectionSpec(
        key="09_constraints_assumptions",
        title="Constraints and Assumptions",
        goal="List constraints (budget/timeline/platform/compliance) and explicit assumptions.",
        format="Bullets under: Constraints, Assumptions.",
    ),
    SectionSpec(
        key="10_open_questions",
        title="Open Questions",
        goal="List unanswered questions that block finalization. Make them actionable.",
        format="Prioritized list: P0/P1/P2 with owner suggestion (Founder/Product/Engineering).",
    ),
]


# -----------------------------
# Prompts
# -----------------------------
REQ_SYSTEM = """\
You are AI Ventex — an expert Product + Solutions Analyst writing a professional Requirements Document.

Audience:
- Product owner / founder (semi-technical)
- Engineering team

Style:
- Very detailed, structured, practical.
- DO NOT be salesy.
- DO NOT invent facts. If something is missing, write it as an Open Question or an Assumption.
- Preserve all details provided (features, numbers, rules, constraints, roles, flows).

Output rules:
- Return MARKDOWN only (no code fences).
- Write only the requested section content (not the whole document).
- Prefer grouped bullet lists and clear headings.
"""

SECTION_USER = """\
Write ONLY this section:

SECTION TITLE:
{title}

SECTION GOAL:
{goal}

SECTION FORMAT:
{format}

INPUT CONTEXT (extracted from chat):
{context_json}

Hard rules:
- Keep maximum detail: include every feature, rule, flow, constraint mentioned.
- If anything is ambiguous, add an Open Question (do not guess silently).
- If proposing defaults, label clearly as Assumption.
"""


# -----------------------------
# IO (load extraction pack you already save)
# -----------------------------
def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def load_extraction_pack(job_id: str) -> Dict[str, Any]:
    return {
        "job_id": job_id,
        "discovery": _read_text(DATA_DIR / f"{job_id}_discovery.md"),
        "ui_ux": _read_text(DATA_DIR / f"{job_id}_ui_ux.md"),
        "features_journeys": _read_text(DATA_DIR / f"{job_id}_features_journeys.md"),
        "tech_stack": _read_text(DATA_DIR / f"{job_id}_tech_stack.md"),
        "budget_timeline": _read_text(DATA_DIR / f"{job_id}_budget_timeline.md"),
        "open_questions": _read_text(DATA_DIR / f"{job_id}_open_questions.md"),
        "full_json": json.loads(_read_text(DATA_DIR / f"{job_id}_full.json")),
    }


def build_context_payload(pack: Dict[str, Any]) -> Dict[str, Any]:
    # Keep it big for high recall.
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
# OpenAI helpers
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
            await anyio.sleep(min(2.0 * attempt, 6.0))
    raise RuntimeError(f"OpenAI call failed after {max_retries} retries: {last_err}")


# -----------------------------
# Main generator (multi-call, one document)
# -----------------------------
async def generate_requirements_document(
    *,
    job_id: str,
    model: str = "gpt-4o",
    out_dir: Path = DOCS_DIR,
    debug_preview: bool = False,
) -> Dict[str, str]:
    """
    Creates ONE Requirements Document as Markdown via multiple OpenAI calls.
    Saves:
      - {job_id}_requirements.md
    Returns:
      {"md_path": "..."}
    """
    out_dir.mkdir(parents=True, exist_ok=True)

    pack = load_extraction_pack(job_id)
    ctx = build_context_payload(pack)

    client = _get_client()

    parts: List[str] = []
    parts.append(f"# Requirements Document\n\n**Job ID:** `{job_id}`\n")

    # Optional: quick context preview in logs
    if debug_preview:
        print("\n[requirements_doc] Context preview (first 250 chars each):")
        for k, v in ctx["extraction_files"].items():
            vv = (v or "").replace("\n", " ")
            print(f"  - {k}: {vv[:250]}{'...' if len(vv) > 250 else ''}")

    # Table of contents
    toc = ["## Table of Contents"]
    for s in REQ_SECTIONS:
        toc.append(f"- {s.title}")
    parts.append("\n".join(toc) + "\n")

    # Generate each section sequentially for consistency
    for s in REQ_SECTIONS:
        print(f"\n--- [requirements_doc] Generating: {s.key} / {s.title} ---")

        user_prompt = SECTION_USER.format(
            title=s.title,
            goal=s.goal,
            format=s.format,
            context_json=json.dumps(ctx, ensure_ascii=False),
        )

        section_md = await _call_openai_markdown(
            client,
            model=model,
            system=REQ_SYSTEM,
            user=user_prompt,
        )

        # Ensure section heading
        if not section_md.lstrip().startswith("#") and not section_md.lstrip().startswith("##"):
            section_md = f"## {s.title}\n\n{section_md}"

        parts.append(section_md.strip() + "\n")

    final_md = "\n\n".join(parts).strip() + "\n"
    md_path = out_dir / f"{job_id}_requirements.md"
    md_path.write_text(final_md, encoding="utf-8")

    return {"md_path": str(md_path.resolve())}
