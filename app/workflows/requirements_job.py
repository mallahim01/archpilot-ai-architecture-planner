import uuid
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
import anyio
from app.db import async_session_maker
from app import crud
from app.crud_jobs import set_job_status
from app.crud_artifacts import upsert_artifact
from app.llm.requirements_llm import generate_requirements_doc


ARTIFACT_TYPE = "requirements_doc"


async def run_requirements_job(user_id: uuid.UUID, chat_id: uuid.UUID, job_id: uuid.UUID) -> None:
    async with async_session_maker() as db:  # type: AsyncSession
        try:
            # Safety: ensure chat belongs to this user
            await crud.get_chat_owned(db, user_id, chat_id)

            await set_job_status(db, job_id, status="running", progress=5)

            # Load context + messages (use enough history)
            ctx_row = await crud.get_context(db, user_id, chat_id)
            summary_row = await crud.get_chat_summary(db, user_id, chat_id)
            messages = await crud.get_messages(db, user_id, chat_id, limit=200, offset=0)

            ctx_obj = {
                "initial_details": getattr(ctx_row, "initial_details", None) if ctx_row else None,
                "ui_details": getattr(ctx_row, "ui_details", None) if ctx_row else None,
                "user_journeys": getattr(ctx_row, "user_journeys", None) if ctx_row else None,
                "tech_stack": getattr(ctx_row, "tech_stack", None) if ctx_row else None,
                "extra": (getattr(ctx_row, "extra", None) or {}) if ctx_row else {},
            }

            await set_job_status(db, job_id, status="running", progress=20)

            # # Generate doc with TWO sample OpenAI calls inside
            # doc_md = generate_requirements_doc(
            #     chat_context=ctx_obj,
            #     rolling_summary=(summary_row.summary if summary_row else ""),
            #     messages=[{"role": m.role, "content": m.content} for m in reversed(messages)],  # oldest->newest
            # )
            payload_messages = [{"role": m.role, "content": m.content} for m in reversed(messages)]  # oldest->newest
            doc_md = await anyio.to_thread.run_sync(
                generate_requirements_doc,
                ctx_obj,
                (summary_row.summary if summary_row else ""),
                payload_messages,
            )

            await set_job_status(db, job_id, status="running", progress=85)

            # Save artifact
            await upsert_artifact(db, chat_id, ARTIFACT_TYPE, doc_md)

            # Optional: also add a message to chat history saying it's ready
            await crud.add_message(
                db, user_id, chat_id, "assistant",
                "✅ Your requirement document is ready. You can open it from the Requirements tab.",
                meta={"artifact": ARTIFACT_TYPE}
            )

            await set_job_status(db, job_id, status="done", progress=100)

        except Exception as e:
            await set_job_status(db, job_id, status="failed", error=str(e))
            # Don't raise further; background tasks should not crash server.
            return
