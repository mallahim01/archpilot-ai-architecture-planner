import uuid
from typing import Any
from datetime import datetime
from pydantic import BaseModel, EmailStr, Field

# -------- Auth --------
class SignupIn(BaseModel):
    email: EmailStr
    username: str = Field(min_length=3, max_length=60)
    password: str = Field(min_length=8, max_length=128)
    first_name: str | None = Field(default=None, max_length=80)
    last_name: str | None = Field(default=None, max_length=80)
    country: str | None = Field(default=None, max_length=80)
    phone: str | None = Field(default=None, max_length=40)

class LoginIn(BaseModel):
    username: str
    password: str

class TokenOut(BaseModel):
    access_token: str
    token_type: str = "bearer"
    expires_in_seconds: int

class UserOut(BaseModel):
    id: uuid.UUID
    email: EmailStr
    username: str
    first_name: str | None
    last_name: str | None
    country: str | None
    phone: str | None
    created_at: datetime

# -------- Chats --------
class ChatCreateIn(BaseModel):
    name: str = Field(default="New chat", max_length=200)
    assigned_to: str | None = None

class ChatOut(BaseModel):
    id: uuid.UUID
    name: str
    assigned_to: str | None
    created_at: datetime
    updated_at: datetime

# -------- Messages --------
class MessageCreateIn(BaseModel):
    role: str = Field(pattern="^(user|assistant|system|tool)$")
    content: str
    meta: dict | None = None

class MessageOut(BaseModel):
    id: uuid.UUID
    role: str
    content: str
    meta: dict | None
    created_at: datetime

# -------- Context --------
class ContextUpsertIn(BaseModel):
    initial_details: str | None = None
    ui_details: str | None = None
    user_journeys: str | None = None
    tech_stack: str | None = None
    extra: dict | None = None

class ContextOut(ContextUpsertIn):
    chat_id: uuid.UUID
    updated_at: datetime

class ChatResponseIn(BaseModel):
    chat_id: uuid.UUID
    message: str = Field(min_length=1)
    action: str | None = None         # e.g. "generate_requirements"
    action_status: str | None = None  # "queued" | "running" | "done" | "failed"
    job_id: uuid.UUID | None = None

class ChatResponseOut(BaseModel):
    response: str
    # mirrors LLM stage output
    context_patch: dict[str, Any] | None = None
    advance: bool = False

    # optional but recommended: helps UI/stage tracking
    assigned_to: str | None = None
    action: str | None = None         # e.g. "generate_requirements"
    action_status: str | None = None  # "queued" | "running" | "done" | "failed"
    job_id: uuid.UUID | None = None
    
    
class JobOut(BaseModel):
    id: uuid.UUID
    chat_id: uuid.UUID
    job_type: str
    status: str
    progress: int
    error: str | None = None


class RequirementDocOut(BaseModel):
    chat_id: uuid.UUID
    artifact_type: str
    content: str
