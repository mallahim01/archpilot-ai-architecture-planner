from __future__ import annotations

import os
import json
from pathlib import Path
from typing import Optional, Dict, Any, List

from openai import AsyncOpenAI


# Where your extraction step already saved files
EXTRACTION_DATA_DIR = Path(__file__).resolve().parents[1] / "extraction" / "data"
# Where we will save final docs
DOCUMENTS_DIR = Path(__file__).resolve().parents[1] / "extraction" / "documents"


def _read_text(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8", errors="ignore").strip()


def _read_json(path: Path) -> Dict[str, Any]:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8", errors="ignore"))
    except Exception:
        return {}


def _load_extraction_bundle(job_id: str) -> Dict[str, Any]:
    """
    Loads the extracted knowledge files created earlier:
      job_id_discovery.md
      job_id_ui_ux.md
      job_id_features_journeys.md
      job_id_tech_stack.md
      job_id_budget_timeline.md
      job_id_open_questions.md
      job_id_full.json
    """
    bundle = {
        "job_id": job_id,
        "discovery": _read_text(EXTRACTION_DATA_DIR / f"{job_id}_discovery.md"),
        "ui_ux": _read_text(EXTRACTION_DATA_DIR / f"{job_id}_ui_ux.md"),
        "features_journeys": _read_text(EXTRACTION_DATA_DIR / f"{job_id}_features_journeys.md"),
        "tech_stack": _read_text(EXTRACTION_DATA_DIR / f"{job_id}_tech_stack.md"),
        "budget_timeline": _read_text(EXTRACTION_DATA_DIR / f"{job_id}_budget_timeline.md"),
        "open_questions": _read_text(EXTRACTION_DATA_DIR / f"{job_id}_open_questions.md"),
        "full_json": _read_json(EXTRACTION_DATA_DIR / f"{job_id}_full.json"),
    }
    return bundle


def _build_source_pack(bundle: Dict[str, Any]) -> str:
    """
    A compact but information-dense source pack that we feed into each section call.
    (This is not a strict prompt—it's the knowledge base for the model.)
    """
    # Keep full_json short if it’s huge
    full_json = bundle.get("full_json") or {}
    full_json_str = json.dumps(full_json, ensure_ascii=False)
    if len(full_json_str) > 12_000:
        full_json_str = full_json_str[:12_000] + "\n...TRUNCATED..."

    return (
        "SOURCE PACK (extracted from the chat)\n"
        "-----------------------------------\n\n"
        f"[DISCOVERY]\n{bundle.get('discovery','')}\n\n"
        f"[FEATURES & JOURNEYS]\n{bundle.get('features_journeys','')}\n\n"
        f"[UI/UX]\n{bundle.get('ui_ux','')}\n\n"
        f"[BUDGET & TIMELINE]\n{bundle.get('budget_timeline','')}\n\n"
        f"[OPEN QUESTIONS]\n{bundle.get('open_questions','')}\n\n"
        f"[FULL_JSON (partial)]\n{full_json_str}\n"
    )


def _clean_md(text: str) -> str:
    """
    Removes common model artifacts like ``` fences. Keeps plain markdown.
    """
    t = (text or "").strip()
    # Remove code fences if model wraps markdown
    if t.startswith("```"):
        t = t.strip("`")
        # sometimes it becomes like "markdown\n...."
        t = t.replace("markdown\n", "", 1).strip()
        t = t.replace("json\n", "", 1).strip()
    return t.strip()


async def _write_section(
    client: AsyncOpenAI,
    *,
    model: str,
    source_pack: str,
    section_name: str,
    instructions: str,
) -> str:
    """
    One OpenAI call = one section.
    """
    system = (
        "You are a senior product designer + business analyst writing user journeys for a software product.\n"
        "Audience: founders + non-technical stakeholders + developers.\n"
        "Style rules:\n"
        "- Write in clear, friendly, professional language (not overly technical).\n"
        "- Use concrete steps, bullets, and checklists.\n"
        "- If information is missing, write assumptions explicitly and add questions at the end.\n"
        "- Output MUST be Markdown. No code blocks. No backticks.\n"
    )

    user = (
        f"{source_pack}\n\n"
        f"SECTION TO WRITE: {section_name}\n"
        f"SECTION INSTRUCTIONS:\n{instructions}\n"
    )

    resp = await client.responses.create(
        model=model,
        input=[
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
    )
    return _clean_md(resp.output_text or "")


async def generate_user_journeys_document(
    *,
    job_id: str,
    model: str = "gpt-4o",
    api_key: Optional[str] = None,
) -> Dict[str, str]:
    """
    Generates the *User Journeys* document as Markdown using multiple calls (sections).
    Saves it to: app/llm/extraction/documents/{job_id}_user_journeys.md

    Returns:
      {"path": "...", "content": "..."}
    """
    api_key = api_key or os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY is not set")

    DOCUMENTS_DIR.mkdir(parents=True, exist_ok=True)

    bundle = _load_extraction_bundle(job_id)
    source_pack = _build_source_pack(bundle)

    client = AsyncOpenAI(api_key=api_key)

    # ---- Section plan (multi-call) ----
    sections: List[Dict[str, str]] = [
        {
            "name": "1) Executive Summary (Plain Language)",
            "instructions": (
                "Write a short executive summary of the product and what users achieve.\n"
                "Include:\n"
                "- What the product is (one paragraph)\n"
                "- Who it is for (bullets)\n"
                "- Primary outcomes (bullets)\n"
                "- 3–6 key capabilities (bullets)\n"
            ),
        },
        {
            "name": "2) Personas & Roles",
            "instructions": (
                "Infer likely personas from the source pack.\n"
                "Create 3–6 personas maximum.\n"
                "For each persona include:\n"
                "- Persona name/title\n"
                "- Goals\n"
                "- Pain points\n"
                "- Permissions/role (if applicable)\n"
                "- Success metrics (what 'good' looks like)\n"
                "If personas are unclear, propose sensible defaults and mark as assumptions."
            ),
        },
        {
            "name": "3) Core User Journeys (Step-by-step)",
            "instructions": (
                "Write the core journeys as numbered step flows.\n"
                "You MUST cover:\n"
                "- New user onboarding journey\n"
                "- Main value journey (booking / purchase / subscription / whatever the core goal is)\n"
                "- Admin/operator journey (if relevant)\n"
                "- Provider/instructor/merchant journey (if relevant)\n\n"
                "For each journey include:\n"
                "- Trigger (what starts it)\n"
                "- Steps (numbered)\n"
                "- System behaviors (emails/notifications/payments/permissions)\n"
                "- Completion criteria\n"
                "- Failure/edge cases\n"
                "Keep it understandable for founders."
            ),
        },
        {
            "name": "4) UI Touchpoints (Screens & Navigation)",
            "instructions": (
                "List the screens/pages needed to support the journeys.\n"
                "Group screens by persona.\n"
                "For each screen include:\n"
                "- Purpose\n"
                "- Key components\n"
                "- Main actions\n"
                "- Data shown\n"
                "If UI/UX data is missing, propose a reasonable layout and mark assumptions."
            ),
        },
        {
            "name": "5) Edge Cases, Constraints, and Open Questions",
            "instructions": (
                "Consolidate edge cases, constraints, and open questions.\n"
                "Split into:\n"
                "- Edge cases (bullets)\n"
                "- Constraints (budget, timeline, compliance, geo, languages, etc.)\n"
                "- Open questions (prioritized)\n"
                "Be practical and actionable."
            ),
        },
        {
            "name": "6) Acceptance Criteria & Success Metrics",
            "instructions": (
                "Write acceptance criteria for the MVP using 'Given/When/Then' style where helpful.\n"
                "Also provide success metrics for launch:\n"
                "- Product metrics\n"
                "- Business metrics\n"
                "- Quality/operations metrics\n"
                "Keep it realistic and aligned with the journeys."
            ),
        },
    ]

    # ---- Generate sections sequentially (stable quality) ----
    rendered_sections: List[str] = []
    for s in sections:
        md = await _write_section(
            client,
            model=model,
            source_pack=source_pack,
            section_name=s["name"],
            instructions=s["instructions"],
        )
        # ensure each section has a heading
        if not md.lstrip().startswith("#"):
            md = f"## {s['name']}\n\n{md}"
        rendered_sections.append(md.strip())

    doc = (
        f"# User Journeys Document\n\n"
        f"**Job ID:** {job_id}\n\n"
        f"> This document is generated from chat discovery + extracted knowledge files.\n\n"
        + "\n\n---\n\n".join(rendered_sections)
        + "\n"
    )

    out_path = DOCUMENTS_DIR / f"{job_id}_user_journeys.md"
    out_path.write_text(doc, encoding="utf-8")

    return {"path": str(out_path), "content": doc}


# -----------------------------
# CLI usage (optional)
# -----------------------------
if __name__ == "__main__":
    import anyio

    JOB_ID = os.getenv("JOB_ID", "").strip()
    if not JOB_ID:
        raise SystemExit("Set JOB_ID env var, e.g. JOB_ID=... python user_journeys_doc.py")

    result = anyio.run(generate_user_journeys_document, job_id=JOB_ID)
    print("Saved:", result["path"])
