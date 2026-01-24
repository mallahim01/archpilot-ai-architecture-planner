import uuid
from fastapi import FastAPI, Depends,HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.db import Base, engine, get_db
from app.schemas import (
    SignupIn, LoginIn, TokenOut, UserOut,
    ChatCreateIn, ChatOut,
    MessageCreateIn, MessageOut,
    ContextUpsertIn, ContextOut,
)
from app.auth import create_access_token
from app.deps import get_current_user
from app.models import User
from app import crud
from app.crud_jobs import get_job_owned
from app.schemas import ChatResponseIn, ChatResponseOut
from app.llm.llm import call_llm
from app.llm.web_runner import web_call_stage_llm
from app.llm.web_stages import web_next_stage
from fastapi import BackgroundTasks, HTTPException
import uuid

from app.crud_jobs import create_job, get_job_owned
from app.crud_artifacts import get_artifact
from app.workflows.requirements_job import run_requirements_job
from app.schemas import JobOut, RequirementDocOut


app = FastAPI(title="FastAPI Chat Backend")

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)   # ⚠️ DEV ONLY, to re-initialize db
        await conn.run_sync(Base.metadata.create_all)

# @app.on_event("startup")
# async def startup():
#     # For quick local dev (no Alembic). For production, use Alembic migrations.
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)

# -------- Auth --------
@app.post("/auth/signup", response_model=UserOut)
async def signup(payload: SignupIn, db: AsyncSession = Depends(get_db)):
    user = await crud.create_user(
    db,
    payload.email,
    payload.username,
    payload.password,
    payload.first_name,
    payload.last_name,
    payload.country,
    payload.phone,
)

    # user = await crud.create_user(db, payload.email, payload.username, payload.password)
    return user

@app.post("/auth/login", response_model=TokenOut)
async def login(payload: LoginIn, db: AsyncSession = Depends(get_db)):
    user = await crud.authenticate_user(db, payload.username, payload.password)
    token, expires_in = create_access_token(subject=user.username)
    return TokenOut(access_token=token, expires_in_seconds=expires_in)

@app.get("/auth/me", response_model=UserOut)
async def me(current_user: User = Depends(get_current_user)):
    return current_user

# -------- Chats --------
@app.post("/chats", response_model=ChatOut)
async def create_chat(payload: ChatCreateIn, db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
    chat = await crud.create_chat(db, current_user.id, payload.name)
    return chat

@app.get("/chats", response_model=list[ChatOut])
async def list_chats(db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
    return await crud.list_chats(db, current_user.id)

@app.get("/chats/{chat_id}", response_model=ChatOut)
async def get_chat(chat_id: uuid.UUID, db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
    return await crud.get_chat_owned(db, current_user.id, chat_id)

# -------- Messages --------
@app.post("/chats/{chat_id}/messages", response_model=MessageOut)
async def add_message(
    chat_id: uuid.UUID,
    payload: MessageCreateIn,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return await crud.add_message(db, current_user.id, chat_id, payload.role, payload.content, payload.meta)

@app.get("/chats/{chat_id}/messages", response_model=list[MessageOut])
async def get_messages(
    chat_id: uuid.UUID,
    limit: int = 50,
    offset: int = 0,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    limit = min(max(limit, 1), 200)
    offset = max(offset, 0)
    return await crud.get_messages(db, current_user.id, chat_id, limit, offset)

# -------- Context --------
@app.get("/chats/{chat_id}/context", response_model=ContextOut | None)
async def get_context(
    chat_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    
    ctx = await crud.get_context(db, current_user.id, chat_id)
    return ctx

# @app.put("/chats/{chat_id}/context", response_model=ContextOut)
# async def put_context(
#     chat_id: uuid.UUID,
#     payload: ContextUpsertIn,
#     db: AsyncSession = Depends(get_db),
#     current_user: User = Depends(get_current_user),
# ):
#     ctx = await crud.upsert_context(db, current_user.id, chat_id, payload.model_dump())
#     return ctx
@app.put("/chats/{chat_id}/context", response_model=ContextOut)
async def put_context(
    chat_id: uuid.UUID,
    payload: ContextUpsertIn,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    # ✅ Only include fields actually provided in the request body
    data = payload.model_dump(exclude_unset=True)

    ctx = await crud.upsert_context(db, current_user.id, chat_id, data)
    return ctx

# @app.post("/response", response_model=ChatResponseOut)
# async def response_route(
#     payload: ChatResponseIn,
#     db: AsyncSession = Depends(get_db),
#     current_user: User = Depends(get_current_user),
# ):
#     chat_id = payload.chat_id
#     user_msg = payload.message

#     # 1) ensure chat belongs to user
#     await crud.get_chat_owned(db, current_user.id, chat_id)

#     # 2) get rolling summary (short-term memory)
#     summary_row = await crud.get_chat_summary(db, current_user.id, chat_id)
#     rolling_summary = summary_row.summary if summary_row else None

#     # 3) call LLM -> JSON: {response, summary}
#     llm_out = call_llm(user_msg, rolling_summary)
#     assistant_text = str(llm_out.get("response", "")).strip()
#     new_summary = llm_out.get("summary", rolling_summary)

#     # 4) store messages in history
#     await crud.add_message(db, current_user.id, chat_id, "user", user_msg, meta={"source": "response_route"})
#     await crud.add_message(db, current_user.id, chat_id, "assistant", assistant_text, meta={"source": "response_route"})

#     # 5) store updated rolling summary (short term memory)
#     await crud.upsert_chat_summary(db, current_user.id, chat_id, new_summary)

#     return ChatResponseOut(response=assistant_text, summary=new_summary)

from app.llm.llm import run_orchestrator, run_agent, AGENTS
from app.schemas import ChatResponseIn, ChatResponseOut
# plus your existing imports
from fastapi import BackgroundTasks, HTTPException

@app.post("/response", response_model=ChatResponseOut)
async def response_route(
    payload: ChatResponseIn,
    background_tasks: BackgroundTasks,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    chat = await crud.get_chat_owned(db, current_user.id, payload.chat_id)

    stage = (chat.assigned_to or "web_discovery").strip()

    # summary + context snapshot for prompt
    summary_row = await crud.get_chat_summary(db, current_user.id, chat.id)
    rolling_summary = summary_row.summary if summary_row else None

    ctx_row = await crud.get_context(db, current_user.id, chat.id)
    ctx_obj = {
        "initial_details": getattr(ctx_row, "initial_details", None) if ctx_row else None,
        "ui_details": getattr(ctx_row, "ui_details", None) if ctx_row else None,
        "user_journeys": getattr(ctx_row, "user_journeys", None) if ctx_row else None,
        "tech_stack": getattr(ctx_row, "tech_stack", None) if ctx_row else None,
        "extra": (getattr(ctx_row, "extra", None) or {}) if ctx_row else {},
    }

    user_msg = payload.message
    print("User message......")

    # store user message
    await crud.add_message(db, current_user.id, chat.id, "user", user_msg, meta={"stage": stage})

    result = web_call_stage_llm(stage, {
        "rolling_summary": rolling_summary or "",
        "chat_context": ctx_obj,
        "user_message": user_msg,
    })

    assistant_text = (result.get("response") or "").strip()
    summary_chunk = (result.get("summary") or "").strip()
    context_patch = result.get("context_patch")
    advance = bool(result.get("advance", False))

    # store assistant
    await crud.add_message(db, current_user.id, chat.id, "assistant", assistant_text, meta={"stage": stage})

    # append summary chunk
    await crud.upsert_chat_summary(db, current_user.id, chat.id, summary_chunk)

    # patch context
    if isinstance(context_patch, dict) and context_patch:
        await crud.patch_context(db, current_user.id, chat.id, context_patch)

    # read summary after update
    updated_summary = await crud.get_chat_summary(db, current_user.id, chat.id)


    # deterministic stage advance
    if advance:
        nxt = web_next_stage(stage)
        await crud.set_chat_assignment(db, current_user.id, chat.id, nxt)
        

        if nxt == "web_generate_requirements":
            # ✅ 1) Reuse if already generated
            existing_job_id = getattr(chat, "latest_requirements_job_id", None)
            if existing_job_id and requirements_bundle_exists(str(existing_job_id)):
                return ChatResponseOut(
                    response="✅ I already generated your documents earlier. You can open them now.",
                    summary=updated_summary.summary if updated_summary else None,
                    action="generate_requirements",
                    action_status="ready",  # or "done"
                    job_id=existing_job_id,
                )

            # ✅ 2) Otherwise create job + run
            print("Creating a job.....")
            job = await create_job(db, current_user.id, chat.id, "requirements_doc")
            background_tasks.add_task(run_requirements_job, current_user.id, chat.id, job.id)
            print("JOB ID:", job.id)

            return ChatResponseOut(
                response="Perfect — I’m preparing your requirement document now. It will appear shortly.",
                summary=updated_summary.summary if updated_summary else None,
                action="generate_requirements",
                action_status="queued",
                job_id=job.id,
            )

    return ChatResponseOut(
        response=assistant_text,
        summary=updated_summary.summary if updated_summary else None,
    )
    
    # #     return ChatResponseOut(
    # #         response="Perfect — I’m preparing your requirement document now. It will appear shortly.",
    # #         summary= "",
    # #         action="generate_requirements",
    # #         action_status="queued",
    # #         job_id=job.id,
    # #     )

    # # return ChatResponseOut(
    # #     response="Job not created...",
    # #     summary="",
    # # )


# @app.post("/response", response_model=ChatResponseOut)
# async def response_route(
#     payload: ChatResponseIn,
#     db: AsyncSession = Depends(get_db),
#     current_user: User = Depends(get_current_user),
# ):
#     chat = await crud.get_chat_owned(db, current_user.id, payload.chat_id)

#     stage = (chat.assigned_to or "web_discovery").strip()

#     # summary + context snapshot for prompt
#     summary_row = await crud.get_chat_summary(db, current_user.id, chat.id)
#     rolling_summary = summary_row.summary if summary_row else None

#     ctx_row = await crud.get_context(db, current_user.id, chat.id)
#     ctx_obj = {
#         "initial_details": getattr(ctx_row, "initial_details", None) if ctx_row else None,
#         "ui_details": getattr(ctx_row, "ui_details", None) if ctx_row else None,
#         "user_journeys": getattr(ctx_row, "user_journeys", None) if ctx_row else None,
#         "tech_stack": getattr(ctx_row, "tech_stack", None) if ctx_row else None,
#         "extra": (getattr(ctx_row, "extra", None) or {}) if ctx_row else {},
#     }

#     user_msg = payload.message

#     # store user message
#     await crud.add_message(db, current_user.id, chat.id, "user", user_msg, meta={"stage": stage})

#     result = web_call_stage_llm(stage, {
#         "rolling_summary": rolling_summary or "",
#         "chat_context": ctx_obj,
#         "user_message": user_msg,
#     })

#     assistant_text = (result.get("response") or "").strip()
#     summary_chunk = (result.get("summary") or "").strip()
#     context_patch = result.get("context_patch")
#     advance = bool(result.get("advance", False))

#     # store assistant
#     await crud.add_message(db, current_user.id, chat.id, "assistant", assistant_text, meta={"stage": stage})

#     # append summary chunk (your append semantics)
#     await crud.upsert_chat_summary(db, current_user.id, chat.id, summary_chunk)

#     # patch context
#     if isinstance(context_patch, dict) and context_patch:
#         await crud.patch_context(db, current_user.id, chat.id, context_patch)

#     # deterministic stage advance
#     updated_summary = await crud.get_chat_summary(db, current_user.id, chat.id)
#     if advance:
#         nxt = web_next_stage(stage)
#         await crud.set_chat_assignment(db, current_user.id, chat.id, nxt)  # nxt may be None (means done)
#         if nxt == "web_generate_requirements":
#             # return immediately with action for frontend
#             return ChatResponseOut(
#                 response="Perfect — I’m preparing your requirement document now. It will appear shortly.",
#                 summary=updated_summary.summary if updated_summary else None,
#                 action="generate_requirements",
#                 action_status="queued",
#             )

    
#     return ChatResponseOut(
#         response=assistant_text,
#         summary=updated_summary.summary if updated_summary else None,
#     )


@app.get("/jobs/{job_id}", response_model=JobOut)
async def get_job(job_id: uuid.UUID, db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
    try:
        job = await get_job_owned(db, current_user.id, job_id)
    except ValueError:
        raise HTTPException(status_code=404, detail="Job not found")

    return JobOut(
        id=job.id,
        chat_id=job.chat_id,
        job_type=job.job_type,
        status=job.status,
        progress=job.progress,
        error=job.error,
    )


@app.get("/chats/{chat_id}/artifacts/requirements", response_model=RequirementDocOut)
async def get_requirements_doc(chat_id: uuid.UUID, db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
    # ensure ownership
    await crud.get_chat_owned(db, current_user.id, chat_id)

    row = await get_artifact(db, chat_id, "requirements_doc")
    if not row:
        raise HTTPException(status_code=404, detail="Requirements doc not found")

    return RequirementDocOut(chat_id=chat_id, artifact_type=row.artifact_type, content=row.content)



@app.put("/chats/{chat_id}/assignment", response_model=ChatOut)
async def set_assignment(
    chat_id: uuid.UUID,
    assigned_to: str | None = None,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    if assigned_to is not None and assigned_to not in AGENTS and assigned_to != "orchestrator":
        raise HTTPException(status_code=400, detail=f"Invalid assigned_to. Allowed: orchestrator, {list(AGENTS.keys())}")

    chat = await crud.set_chat_assignment(db, current_user.id, chat_id, None if assigned_to == "orchestrator" else assigned_to)
    return chat
