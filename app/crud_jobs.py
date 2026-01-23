import uuid
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Job


async def create_job(db: AsyncSession, user_id: uuid.UUID, chat_id: uuid.UUID, job_type: str) -> Job:
    job = Job(user_id=user_id, chat_id=chat_id, job_type=job_type, status="queued", progress=0)
    db.add(job)
    await db.commit()
    await db.refresh(job)
    return job


async def get_job_owned(db: AsyncSession, user_id: uuid.UUID, job_id: uuid.UUID) -> Job:
    q = await db.execute(select(Job).where(Job.id == job_id, Job.user_id == user_id))
    job = q.scalar_one_or_none()
    if not job:
        raise ValueError("Job not found")  # replace with HTTPException in route
    return job


async def set_job_status(db: AsyncSession, job_id: uuid.UUID, status: str, progress: int | None = None, error: str | None = None) -> None:
    q = await db.execute(select(Job).where(Job.id == job_id))
    job = q.scalar_one()
    job.status = status
    if progress is not None:
        job.progress = progress
    job.error = error
    await db.commit()
