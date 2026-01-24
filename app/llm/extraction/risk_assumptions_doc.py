from __future__ import annotations

import os
import json
from pathlib import Path
from typing import Dict, Any, List, Optional

from openai import AsyncOpenAI


EXTRACTION_DATA_DIR = Path(__file__).resolve().parents[1] / "extraction" / "data"
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
    return {
        "discovery": _read_text(EXTRACTION_DATA_DIR / f"{job_id}_discovery.md"),
        "ui_ux": _read_text(EXTRACTION_DATA_DIR / f"{job_id}_ui_ux.md"),
        "features_journeys": _read_text(EXTRACTION_DATA_DIR / f"{job_id}_features_journeys.md"),
        "tech_stack": _read_text(EXTRACTION_DATA_DIR / f"{job_id}_tech_stack.md"),
        "budget_timeline": _read_text(EXTRACTION_DATA_DIR / f"{job_id}_budget_timeline.md"),
        "open_questions": _read_text(EXTRACTION_DATA_DIR / f"{job_id}_open_questions.md"),
        "full_json": _read_json(EXTRACTION_DATA_DIR / f"{job_id}_full.json"),
    }


def _build_source_pack(bundle: Dict[str, Any]) -> str:
    full_json = json.dumps(bundle.get("full_json", {}), ensure_ascii=False)
    if len(full_json) > 10_000:
        full_json = full_json[:10_000] + "\n...TRUNCATED..."

    return (
        "SOURCE CONTEXT (Risks & Assumptions)\n"
        "----------------------------------\n\n"
        f"[DISCOVERY]\n{bundle['discovery']}\n\n"
        f"[UI / UX]\n{bundle['ui_ux']}\n\n"
        f"[FEATURES & JOURNEYS]\n{bundle['features_journeys']}\n\n"
        f"[TECH STACK]\n{bundle['tech_stack']}\n\n"
        f"[BUDGET & TIMELINE]\n{bundle['budget_timeline']}\n\n"
        f"[OPEN QUESTIONS]\n{bundle['open_questions']}\n\n"
        f"[FULL JSON]\n{full_json}\n"
    )


def _clean_md(text: str) -> str:
    t = (text or "").strip()
    if t.startswith("```"):
        t = t.strip("`")
        t = t.replace("markdown\n", "").replace("json\n", "").strip()
    return t


async def _write_section(
    client: AsyncOpenAI,
    *,
    model: str,
    source_pack: str,
    section_title: str,
    instructions: str,
) -> str:
    system = (
        "You are a senior delivery consultant and risk analyst.\n"
        "You write professional risk & assumption logs for founders, CTOs, and delivery teams.\n"
        "Rules:\n"
        "- Be realistic, not optimistic\n"
        "- Explain risks in plain language\n"
        "- Separate assumptions from risks clearly\n"
        "- Use structured bullets and tables (Markdown)\n"
        "- Output Markdown only\n"
    )

    user = (
        f"{source_pack}\n\n"
        f"SECTION: {section_title}\n"
        f"INSTRUCTIONS:\n{instructions}\n"
    )

    resp = await client.responses.create(
        model=model,
        input=[
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
    )

    md = _clean_md(resp.output_text or "")
    if not md.startswith("#"):
        md = f"## {section_title}\n\n{md}"
    return md.strip()


async def generate_risk_assumptions_document(
    *,
    job_id: str,
    model: str = "gpt-4o",
    api_key: Optional[str] = None,
) -> Dict[str, str]:
    api_key = api_key or os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY is not set")

    DOCUMENTS_DIR.mkdir(parents=True, exist_ok=True)

    bundle = _load_extraction_bundle(job_id)
    source_pack = _build_source_pack(bundle)

    client = AsyncOpenAI(api_key=api_key)

    sections = [
        (
            "Planning Assumptions",
            "List all assumptions made during planning.\n"
            "Include assumptions about scope stability, user behavior, decision speed, integrations, and budget."
        ),
        (
            "Business Risks",
            "Identify risks related to market fit, monetization, adoption, and operational sustainability."
        ),
        (
            "Product & UX Risks",
            "Identify risks related to usability, onboarding complexity, role confusion, and user retention."
        ),
        (
            "Technical & Scalability Risks",
            "List risks related to architecture, scalability, performance, third-party dependencies, and technical debt."
        ),
        (
            "Delivery & Timeline Risks",
            "Identify risks that may impact timelines such as scope creep, dependency delays, or unclear ownership."
        ),
        (
            "Security & Compliance Risks",
            "Identify security, data privacy, and compliance risks based on the product context."
        ),
        (
            "Risk Mitigation Summary",
            "Summarize mitigation strategies for the most critical risks.\n"
            "Explain how risks will be monitored and revisited during delivery."
        ),
    ]

    rendered: List[str] = []
    for title, instructions in sections:
        rendered.append(
            await _write_section(
                client,
                model=model,
                source_pack=source_pack,
                section_title=title,
                instructions=instructions,
            )
        )

    doc = (
        f"# Risk & Assumptions Log\n\n"
        f"**Job ID:** {job_id}\n\n"
        f"> This document identifies key assumptions and risks that may impact delivery, cost, or outcomes.\n\n"
        + "\n\n---\n\n".join(rendered)
        + "\n"
    )

    out_path = DOCUMENTS_DIR / f"{job_id}_risk_assumptions.md"
    out_path.write_text(doc, encoding="utf-8")

    return {"path": str(out_path), "content": doc}
