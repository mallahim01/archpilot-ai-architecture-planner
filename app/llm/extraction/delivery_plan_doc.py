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
        "SOURCE PACK (Delivery & Planning)\n"
        "-------------------------------\n\n"
        f"[DISCOVERY]\n{bundle['discovery']}\n\n"
        f"[FEATURES & JOURNEYS]\n{bundle['features_journeys']}\n\n"
        f"[TECH STACK]\n{bundle['tech_stack']}\n\n"
        f"[BUDGET & TIMELINE INPUT]\n{bundle['budget_timeline']}\n\n"
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
        "You are a senior delivery manager and solution architect.\n"
        "You write professional planning documents for founders, CTOs, and clients.\n"
        "Rules:\n"
        "- Be realistic and implementation-focused\n"
        "- Explain trade-offs clearly\n"
        "- Use structured bullets and tables (Markdown)\n"
        "- If data is missing, state assumptions explicitly\n"
        "- Output Markdown only (no code blocks)\n"
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


async def generate_delivery_plan_document(
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
            "Executive Delivery Overview",
            "Summarize how the product will be delivered end-to-end.\n"
            "Include overall timeline, delivery philosophy (MVP → iterations), and success definition."
        ),
        (
            "Assumptions & Constraints",
            "List all assumptions used for planning (scope stability, team size, decision speed).\n"
            "Also list constraints: budget, timeline, compliance, integrations, geography."
        ),
        (
            "Phased Timeline & Milestones",
            "Break delivery into phases (e.g., Discovery, Foundation, Core Build, Monetization, Hardening).\n"
            "For each phase include:\n"
            "- Duration\n"
            "- Key deliverables\n"
            "- Exit criteria"
        ),
        (
            "Team & Effort Breakdown",
            "Describe the delivery team composition.\n"
            "Include roles (PM, FE, BE, QA, DevOps, Design) and effort allocation by phase."
        ),
        (
            "Budget Allocation & Cost Drivers",
            "Provide a realistic budget breakdown.\n"
            "Split costs by:\n"
            "- Engineering\n"
            "- Design\n"
            "- Infrastructure\n"
            "- Third-party services\n"
            "- Contingency\n"
            "Explain main cost drivers and optimization levers."
        ),
        (
            "Delivery Risks & Mitigation Plan",
            "List major delivery risks (technical, product, organizational).\n"
            "For each risk provide mitigation strategies."
        ),
        (
            "Go-Live & Post-Launch Plan",
            "Describe launch preparation, rollout strategy, monitoring, and post-launch iterations.\n"
            "Include support, maintenance, and future roadmap signals."
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
        f"# Delivery Plan, Milestones & Budget\n\n"
        f"**Job ID:** {job_id}\n\n"
        f"> This document explains how the product will be delivered, funded, and launched.\n\n"
        + "\n\n---\n\n".join(rendered)
        + "\n"
    )

    out_path = DOCUMENTS_DIR / f"{job_id}_delivery_plan.md"
    out_path.write_text(doc, encoding="utf-8")

    return {"path": str(out_path), "content": doc}
