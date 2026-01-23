import uuid
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, desc
from fastapi import HTTPException, status
from app.models import User, Chat, Message, ChatContext
from app.auth import hash_password, verify_password

# -------- Users --------
async def create_user(db: AsyncSession, email: str, username: str, password: str, first_name: str | None, last_name: str | None,
                      country: str | None, phone: str | None) -> User:
    existing = await db.execute(select(User).where((User.email == email) | (User.username == username)))
    if existing.scalar_one_or_none():
        raise HTTPException(status_code=400, detail="Email or username already exists")

    # user = User(email=email, username=username, password_hash=hash_password(password))
    # app/crud.py (inside create_user)
    user = User(
        email=email,
        username=username,
        password_hash=hash_password(password),
        first_name=first_name,
        last_name=last_name,
        country=country,
        phone=phone,
    )

    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user

async def authenticate_user(db: AsyncSession, username: str, password: str) -> User:
    q = await db.execute(select(User).where(User.username == username))
    user = q.scalar_one_or_none()
    if not user or not verify_password(password, user.password_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    return user

# -------- Chats --------
async def create_chat(db: AsyncSession, user_id: uuid.UUID, name: str) -> Chat:
    chat = Chat(user_id=user_id, name=name, assigned_to="web_discovery")
    db.add(chat)
    await db.commit()
    await db.refresh(chat)
    return chat

async def list_chats(db: AsyncSession, user_id: uuid.UUID) -> list[Chat]:
    q = await db.execute(select(Chat).where(Chat.user_id == user_id).order_by(desc(Chat.updated_at)))
    return list(q.scalars().all())

async def get_chat_owned(db: AsyncSession, user_id: uuid.UUID, chat_id: uuid.UUID) -> Chat:
    q = await db.execute(select(Chat).where(Chat.id == chat_id, Chat.user_id == user_id))
    chat = q.scalar_one_or_none()
    if not chat:
        raise HTTPException(status_code=404, detail="Chat not found")
    return chat

async def set_chat_assignment(db: AsyncSession, user_id: uuid.UUID, chat_id: uuid.UUID, assigned_to: str | None) -> Chat:
    chat = await get_chat_owned(db, user_id, chat_id)
    chat.assigned_to = assigned_to
    await db.commit()
    await db.refresh(chat)
    return chat


# -------- Messages --------
async def add_message(db: AsyncSession, user_id: uuid.UUID, chat_id: uuid.UUID, role: str, content: str, meta: dict | None) -> Message:
    await get_chat_owned(db, user_id, chat_id)
    msg = Message(chat_id=chat_id, role=role, content=content, meta=meta)
    db.add(msg)
    await db.commit()
    await db.refresh(msg)
    return msg

async def get_messages(db: AsyncSession, user_id: uuid.UUID, chat_id: uuid.UUID, limit: int, offset: int) -> list[Message]:
    await get_chat_owned(db, user_id, chat_id)
    q = await db.execute(
        select(Message)
        .where(Message.chat_id == chat_id)
        .order_by(Message.created_at.asc())
        .limit(limit)
        .offset(offset)
    )
    return list(q.scalars().all())

# -------- Context --------
async def get_context(db: AsyncSession, user_id: uuid.UUID, chat_id: uuid.UUID) -> ChatContext | None:
    await get_chat_owned(db, user_id, chat_id)
    q = await db.execute(select(ChatContext).where(ChatContext.chat_id == chat_id))
    return q.scalar_one_or_none()


async def upsert_context(db: AsyncSession, user_id: uuid.UUID, chat_id: uuid.UUID, data: dict) -> ChatContext:
    await get_chat_owned(db, user_id, chat_id)

    q = await db.execute(select(ChatContext).where(ChatContext.chat_id == chat_id))
    ctx = q.scalar_one_or_none()

    if ctx is None:
        # For new row, just create it with provided fields
        ctx = ChatContext(chat_id=chat_id, **data)
        db.add(ctx)
    else:
        # ✅ merge "extra" instead of replacing (only if provided)
        if "extra" in data and data["extra"] is not None:
            existing = ctx.extra or {}
            incoming = data["extra"] or {}
            # merge: incoming keys overwrite existing keys
            ctx.extra = {**existing, **incoming}
            data.pop("extra")  # remove so it's not processed again below

        # ✅ update only provided fields
        for k, v in data.items():
            setattr(ctx, k, v)

    await db.commit()
    await db.refresh(ctx)
    return ctx

# async def upsert_context(db: AsyncSession, user_id: uuid.UUID, chat_id: uuid.UUID, data: dict) -> ChatContext:
#     await get_chat_owned(db, user_id, chat_id)

#     q = await db.execute(select(ChatContext).where(ChatContext.chat_id == chat_id))
#     ctx = q.scalar_one_or_none()

#     if ctx is None:
#         ctx = ChatContext(chat_id=chat_id, **data)
#         db.add(ctx)
#     else:
#         for k, v in data.items():
#             setattr(ctx, k, v)

#     await db.commit()
#     await db.refresh(ctx)
#     return ctx

import uuid
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import ChatSummary
from app.crud import get_chat_owned  # adjust import if needed

MAX_SUMMARY_CHARS = 1000  # keep short-term memory bounded

def _append_summary(existing: str | None, new_chunk: str | None) -> str | None:
    chunk = (new_chunk or "").strip()
    if not chunk:
        return existing  # nothing new to add

    prev = (existing or "").strip()
    combined = f"{prev}\n{chunk}".strip() if prev else chunk

    # Trim to last MAX_SUMMARY_CHARS chars (keeps most recent memory)
    if len(combined) > MAX_SUMMARY_CHARS:
        combined = combined[-MAX_SUMMARY_CHARS:]

    return combined


async def get_chat_summary(db: AsyncSession, user_id: uuid.UUID, chat_id: uuid.UUID) -> ChatSummary | None:
    await get_chat_owned(db, user_id, chat_id)
    q = await db.execute(select(ChatSummary).where(ChatSummary.chat_id == chat_id))
    return q.scalar_one_or_none()


async def upsert_chat_summary(
    db: AsyncSession,
    user_id: uuid.UUID,
    chat_id: uuid.UUID,
    new_summary: str | None,   # this is the *chunk* from LLM
) -> ChatSummary:
    await get_chat_owned(db, user_id, chat_id)

    q = await db.execute(select(ChatSummary).where(ChatSummary.chat_id == chat_id))
    row = q.scalar_one_or_none()

    if row is None:
        row = ChatSummary(chat_id=chat_id, summary=_append_summary(None, new_summary))
        db.add(row)
    else:
        row.summary = _append_summary(row.summary, new_summary)

    await db.commit()
    await db.refresh(row)
    return row

# from sqlalchemy import select
# from app.models import ChatSummary

# async def get_chat_summary(db: AsyncSession, user_id: uuid.UUID, chat_id: uuid.UUID) -> ChatSummary | None:
#     await get_chat_owned(db, user_id, chat_id)
#     q = await db.execute(select(ChatSummary).where(ChatSummary.chat_id == chat_id))
#     return q.scalar_one_or_none()

# async def upsert_chat_summary(db: AsyncSession, user_id: uuid.UUID, chat_id: uuid.UUID, new_summary: str | None) -> ChatSummary:
#     await get_chat_owned(db, user_id, chat_id)
#     q = await db.execute(select(ChatSummary).where(ChatSummary.chat_id == chat_id))
#     row = q.scalar_one_or_none()

#     if row is None:
#         row = ChatSummary(chat_id=chat_id, summary=new_summary)
#         db.add(row)
#     else:
#         row.summary = new_summary

#     await db.commit()
#     await db.refresh(row)
#     return row


async def patch_context(db: AsyncSession, user_id: uuid.UUID, chat_id: uuid.UUID, patch: dict) -> ChatContext:
    await get_chat_owned(db, user_id, chat_id)

    ctx = await get_context(db, user_id, chat_id)
    if ctx is None:
        ctx = ChatContext(chat_id=chat_id)
        db.add(ctx)
        await db.flush()

    for k, v in patch.items():
        if v is None:
            continue
        if not hasattr(ctx, k):
            continue
        setattr(ctx, k, v)

    await db.commit()
    await db.refresh(ctx)
    return ctx
