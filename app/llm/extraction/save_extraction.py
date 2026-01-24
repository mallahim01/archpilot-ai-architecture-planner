from __future__ import annotations
import json
from pathlib import Path
from typing import Any, Dict, List

CATEGORIES = {
    "discovery": "discovery",
    "ui_ux": "ui_ux",
    "features_journeys": "features_journeys",
    "tech_stack": "tech_stack",
    "budget_timeline": "budget_timeline",
    "open_questions": "open_questions",
}

def _as_md_lines(items: List[str]) -> str:
    if not items:
        return ""
    # preserve long details, one per bullet
    return "\n".join([f"- {x.strip()}" for x in items if (x or "").strip()]) + "\n"

def save_extracted_knowledge_to_files(
    *,
    job_id: str,
    extracted: Dict[str, Any],
    base_dir: str | Path,
) -> Dict[str, str]:
    """
    Writes 6 files:
      {job_id}_discovery.md
      {job_id}_ui_ux.md
      {job_id}_features_journeys.md
      {job_id}_tech_stack.md
      {job_id}_budget_timeline.md
      {job_id}_open_questions.md

    Returns: dict(category -> absolute file path)
    """
    base = Path(base_dir)
    base.mkdir(parents=True, exist_ok=True)

    out_paths: Dict[str, str] = {}

    for key, suffix in CATEGORIES.items():
        items = extracted.get(key, []) or []
        fp = base / f"{job_id}_{suffix}.md"
        fp.write_text(_as_md_lines(items), encoding="utf-8")
        out_paths[key] = str(fp.resolve())

    # also store a full JSON snapshot for debugging/replay
    json_fp = base / f"{job_id}_full.json"
    json_fp.write_text(json.dumps(extracted, ensure_ascii=False, indent=2), encoding="utf-8")
    out_paths["full_json"] = str(json_fp.resolve())

    return out_paths
