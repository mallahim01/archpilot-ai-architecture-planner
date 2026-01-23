import uuid
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import ChatArtifact


async def upsert_artifact(db: AsyncSession, chat_id: uuid.UUID, artifact_type: str, content: str) -> ChatArtifact:
    q = await db.execute(
        select(ChatArtifact).where(ChatArtifact.chat_id == chat_id, ChatArtifact.artifact_type == artifact_type)
    )
    row = q.scalar_one_or_none()
    if row is None:
        row = ChatArtifact(chat_id=chat_id, artifact_type=artifact_type, content=content)
        db.add(row)
    else:
        row.content = content
    await db.commit()
    await db.refresh(row)
    return row


async def get_artifact(db: AsyncSession, chat_id: uuid.UUID, artifact_type: str) -> ChatArtifact | None:
    q = await db.execute(
        select(ChatArtifact).where(ChatArtifact.chat_id == chat_id, ChatArtifact.artifact_type == artifact_type)
    )
    return q.scalar_one_or_none()
