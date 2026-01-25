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


ARCH_SECTIONS: List[SectionSpec] = [
    SectionSpec(
        key="01_exec_summary",
        title="Executive Summary (Founder-Friendly)",
        goal="Explain the architecture in plain language for founders/business owners: what components exist and why.",
        format=(
            "1–2 pages max. Use short paragraphs + bullet lists. "
            "Explain the big picture: frontend/backend/db/storage/auth/payments/notifications/observability."
        ),
    ),
    SectionSpec(
        key="02_arch_overview",
        title="Architecture Overview",
        goal="Describe the end-to-end system at a high level and how requests flow through major components.",
        format=(
            "Include: System goals, key constraints, architectural style (monolith/modular monolith/microservices), "
            "major components list, and a request lifecycle overview."
        ),
    ),
    SectionSpec(
        key="03_modules_boundaries",
        title="Domain Modules and Service Boundaries",
        goal="Convert features/journeys into a clean module map (bounded contexts).",
        format=(
            "List modules (e.g., Auth/RBAC, Users, Catalog/Courses, Booking, Orders, Payments, Admin, Notifications, Analytics). "
            "For each: responsibilities, main entities, main APIs, and data owned."
        ),
    ),
    SectionSpec(
        key="04_data_model",
        title="Data Model and Database Schema (Conceptual + Proposed Tables)",
        goal="Define entities, relationships, constraints, indices, and how data is stored.",
        format=(
            "Provide: Entity list, relationships, and then a Proposed Schema section. "
            "For each table: columns (type), PK/FK, constraints, indexes, and notes. "
            "Do NOT omit important junction tables."
        ),
    ),
    SectionSpec(
        key="05_api_surface",
        title="API Surface (All Endpoints)",
        goal="Produce a complete API list covering every major feature and flow.",
        format=(
            "Group endpoints by module. For each endpoint: Method + Path, Auth/Roles, Purpose, "
            "Request (fields), Response (fields), Errors, Notes (idempotency/rate limits/pagination). "
            "Be exhaustive. If something is unknown, add as Assumption + Open Question."
        ),
    ),
    SectionSpec(
        key="06_auth_rbac",
        title="Authentication, Authorization, and RBAC Model",
        goal="Define auth approach and role permissions across endpoints and data.",
        format=(
            "Include: auth provider strategy (based on tech_stack), token/session approach, RBAC roles, "
            "permissions matrix, and enforcement points (middleware/guards/policies)."
        ),
    ),
    SectionSpec(
        key="07_integrations",
        title="External Integrations and Webhooks",
        goal="Detail payment, email, storage, video, calendars, or any third-party integrations from extraction.",
        format=(
            "For each integration: why, data exchanged, events, retry strategy, webhook verification, failure handling."
        ),
    ),
    SectionSpec(
        key="08_async_jobs",
        title="Async Jobs, Queues, and Background Workflows",
        goal="Describe background processing: document generation, emails, webhooks, media processing, etc.",
        format=(
            "Include: queue choice (or baseline), job types, statuses, retries/backoff, deduplication, and observability."
        ),
    ),
    SectionSpec(
        key="09_observability",
        title="Observability (Logging, Metrics, Tracing, Alerts)",
        goal="Define what to log/measure and how to debug production incidents.",
        format=(
            "Include: structured logs, correlation IDs, metrics (latency, error rate), tracing, dashboards, alert thresholds."
        ),
    ),
    SectionSpec(
        key="10_security_compliance",
        title="Security, Compliance, and Data Protection",
        goal="Threat model mindset: auth, secrets, encryption, PII, audit logs, and compliance needs (GDPR etc).",
        format=(
            "Include: OWASP concerns, rate limiting, abuse prevention, secrets management, encryption, "
            "data retention, audit logs, admin actions, and backup strategy."
        ),
    ),
    SectionSpec(
        key="11_scalability_reliability",
        title="Scalability, Reliability, and Performance Plan",
        goal="How the system scales and stays reliable under growth.",
        format=(
            "Include: caching strategy, DB indexing, pagination, CDN, horizontal scaling, multi-tenancy if applicable, "
            "SLA/SLO ideas, and failure modes."
        ),
    ),
    SectionSpec(
        key="12_deployment",
        title="Deployment Topology and Environments",
        goal="Define production deployment (based on tech stack), environments, CI/CD, and config.",
        format=(
            "Include: environments (dev/stage/prod), deployment steps, IaC recommendation, secrets, "
            "migration strategy, rollbacks, and versioning."
        ),
    ),
    SectionSpec(
        key="13_open_questions",
        title="Architecture Decisions, Risks, and Open Questions",
        goal="List decisions to confirm, tradeoffs, and remaining questions to finalize the architecture.",
        format=(
            "Provide: Decisions (with options), Risks (with mitigation), and Open Questions (P0/P1/P2)."
        ),
    ),
]


# -----------------------------
# Prompts
# -----------------------------
ARCH_SYSTEM = """\
You are AI Ventex — a principal solutions architect + staff backend engineer.

Audience:
- Founder / business owner (non-technical) for the Executive Summary section
- Engineering team for the rest (very technical and detailed)

Style rules:
- Extremely detailed, structured, practical, and production-minded.
- DO NOT be salesy.
- DO NOT invent product facts. If something is missing, mark it clearly as:
  - Assumption (reasonable default)
  - Open Question (needs confirmation)
- Preserve every extracted detail. Expand into a complete architecture proposal.
- Be explicit about what is derived vs assumed.

Output rules:
- Return MARKDOWN only (no code fences).
- Write ONLY the requested section content (not the whole document).
- If you include tables, keep them simple Markdown tables.
- Use clear headings, nested bullets, and consistent formatting.
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
- Maximum detail. Include every feature, rule, flow, constraint, role, integration from the input.
- For API Surface: be exhaustive, covering all major product workflows end-to-end.
- If anything is ambiguous: add an Open Question (do not guess silently).
- If proposing defaults: label clearly as Assumption.
- Return Markdown only (no code fences).
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
    # Architecture relies most on discovery + features/journeys + tech_stack.
    return {
        "job_id": pack["job_id"],
        "extraction_files": {
            "discovery": pack["discovery"],
            "features_journeys": pack["features_journeys"],
            "tech_stack": pack["tech_stack"],
            "budget_timeline": pack["budget_timeline"],
            "ui_ux": pack["ui_ux"],
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
async def generate_architecture_document(
    *,
    job_id: str,
    model: str = "gpt-4o",
    out_dir: Path = DOCS_DIR,
    debug_preview: bool = False,
) -> Dict[str, str]:
    """
    Creates ONE Architecture Blueprint document as Markdown via multiple OpenAI calls.
    Saves:
      - {job_id}_architecture.md
    Returns:
      {"md_path": "..."}
    """
    out_dir.mkdir(parents=True, exist_ok=True)

    pack = load_extraction_pack(job_id)
    ctx = build_context_payload(pack)

    client = _get_client()

    parts: List[str] = []
    parts.append(f"# Architecture Blueprint\n\n**Job ID:** `{job_id}`\n")

    # Optional: quick context preview in logs
    if debug_preview:
        print("\n[architecture_doc] Context preview (first 250 chars each):")
        for k, v in ctx["extraction_files"].items():
            vv = (v or "").replace("\n", " ")
            print(f"  - {k}: {vv[:250]}{'...' if len(vv) > 250 else ''}")

    # Table of contents
    toc = ["## Table of Contents"]
    for s in ARCH_SECTIONS:
        toc.append(f"- {s.title}")
    parts.append("\n".join(toc) + "\n")

    # Generate each section sequentially for consistency
    for s in ARCH_SECTIONS:
        print(f"\n--- [architecture_doc] Generating: {s.key} / {s.title} ---")

        user_prompt = SECTION_USER.format(
            title=s.title,
            goal=s.goal,
            format=s.format,
            context_json=json.dumps(ctx, ensure_ascii=False),
        )

        section_md = await _call_openai_markdown(
            client,
            model=model,
            system=ARCH_SYSTEM,
            user=user_prompt,
        )

        # Ensure section heading
        if not section_md.lstrip().startswith("#") and not section_md.lstrip().startswith("##"):
            section_md = f"## {s.title}\n\n{section_md}"

        parts.append(section_md.strip() + "\n")

    final_md = "\n\n".join(parts).strip() + "\n"
    md_path = out_dir / f"{job_id}_architecture.md"
    md_path.write_text(final_md, encoding="utf-8")

    return {"md_path": str(md_path.resolve())}
