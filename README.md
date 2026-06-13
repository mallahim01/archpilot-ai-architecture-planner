# ArchPilot AI

ArchPilot AI is a concept-stage backend for an AI-assisted software architecture planning product. The system guides a user through a structured discovery conversation, captures requirements in stages, maintains durable conversation context, and generates architecture-ready requirement documentation.

The product idea is simple: a user describes a product they want to build, the assistant asks focused follow-up questions, captures product scope, roles, user journeys, UI signals, integrations, and tech-stack direction, then produces a detailed requirements document that can be used as the foundation for system architecture and implementation planning.

## What This Project Does

This repository contains a FastAPI backend that supports:

- User signup, login, and JWT-based authentication.
- Authenticated chat sessions.
- Persistent chat messages.
- Structured chat context for product discovery.
- Rolling chat summaries for compact long-term memory.
- A staged LLM workflow for web product architecture discovery.
- Background requirement-document generation.
- Persisted generated artifacts per chat.

The current implementation focuses mainly on web product discovery, with prompt stages for:

1. Product discovery and direction.
2. UI signals and feature definition.
3. User roles and user journeys.
4. Tech stack proposal and agreement.
5. Requirement document generation.

## Product Concept

Architecture Product is intended to behave like an AI architecture consultant. Instead of asking the user to fill a long static form, it runs a guided conversation and extracts architecture-relevant information over multiple turns.

The assistant is designed to:

- Accept incomplete or rough product ideas.
- Make sensible assumptions when the user gives limited detail.
- Ask fewer, higher-value questions.
- Store useful facts in structured context.
- Move through a predictable architecture discovery pipeline.
- Generate a detailed requirement document from the conversation.

This makes the product useful for founders, product owners, agencies, and engineering teams who need early architecture clarity before implementation begins.

## High-Level Architecture

```mermaid
flowchart LR
    User[User or Frontend Client] --> API[FastAPI Backend]
    API --> Auth[JWT Auth Layer]
    API --> Chat[Chat and Context APIs]
    Chat --> DB[(PostgreSQL)]
    Chat --> StageRunner[Stage LLM Runner]
    StageRunner --> OpenAI[OpenAI Responses API]
    StageRunner --> DB
    API --> Jobs[Background Requirement Job]
    Jobs --> OpenAI
    Jobs --> DB
    DB --> Artifacts[Generated Requirement Docs]
```

For a deeper architecture breakdown, see [ARCHITECTURE.md](ARCHITECTURE.md).

## Repository Structure

```text
.
+-- app/
|   +-- main.py                         # FastAPI application and route definitions
|   +-- db.py                           # Async SQLAlchemy engine and session setup
|   +-- models.py                       # Database models
|   +-- schemas.py                      # Pydantic request and response schemas
|   +-- auth.py                         # Password hashing and JWT helpers
|   +-- deps.py                         # FastAPI auth dependency
|   +-- crud.py                         # User, chat, message, context, summary operations
|   +-- crud_jobs.py                    # Job persistence helpers
|   +-- crud_artifacts.py               # Generated artifact persistence helpers
|   +-- llm/
|   |   +-- web_runner.py               # Stage-specific OpenAI call runner
|   |   +-- web_stages.py               # Ordered web discovery pipeline
|   |   +-- requirements_llm.py         # Requirement document generation flow
|   |   +-- llm.py                      # Older/general orchestrator and agent registry
|   |   +-- registry.py                 # Agent type registry concept
|   |   +-- agents/
|   |       +-- web_ecommerce.py        # E-commerce agent prompt concept
|   +-- web_llm_prompts/
|   |   +-- web_discovery.py            # Product discovery prompt
|   |   +-- web_ui_features.py          # UI and feature signal prompt
|   |   +-- web_user_journeys.py        # Roles and user journeys prompt
|   |   +-- web_tech_stack.py           # Tech stack proposal prompt
|   +-- workflows/
|       +-- requirements_job.py         # Background job for document generation
+-- test.py                             # Manual API smoke-test script
+-- requirements.txt                    # Python dependency list
+-- README.md                           # Project documentation
+-- ARCHITECTURE.md                     # Detailed architecture documentation
```

## Core Domain Model

The backend is centered around authenticated users and their architecture-planning chats.

| Model | Purpose |
| --- | --- |
| `User` | Stores account identity, profile fields, password hash, and creation time. |
| `Chat` | Represents one architecture-planning conversation owned by a user. |
| `Message` | Stores full user and assistant message history for a chat. |
| `ChatContext` | Stores structured architecture context such as initial details, UI details, journeys, tech stack, and extra JSON. |
| `ChatSummary` | Stores a bounded rolling memory summary for the chat. |
| `Job` | Tracks background generation tasks such as requirement-document generation. |
| `ChatArtifact` | Stores generated artifacts, currently requirement documents. |

## Main API Capabilities

### Authentication

- `POST /auth/signup`
- `POST /auth/login`
- `GET /auth/me`

Users authenticate with username and password. Passwords are hashed using Argon2. Login returns a bearer token that is used by protected routes.

### Chats

- `POST /chats`
- `GET /chats`
- `GET /chats/{chat_id}`
- `PUT /chats/{chat_id}/assignment`

Each chat belongs to one user. New chats default to the `web_discovery` stage.

### Messages

- `POST /chats/{chat_id}/messages`
- `GET /chats/{chat_id}/messages`

Messages are stored separately from the generated context so that the product can preserve both the raw conversation and the distilled architecture facts.

### Context

- `GET /chats/{chat_id}/context`
- `PUT /chats/{chat_id}/context`

Context stores structured fields that are useful for architecture generation:

- `initial_details`
- `ui_details`
- `user_journeys`
- `tech_stack`
- `extra`

### Conversational AI Response

- `POST /response`

This is the main product workflow endpoint. It verifies ownership, reads the current stage, loads summary and context, stores the user message, calls the stage-specific LLM prompt, stores the assistant response, appends summary, patches context, and advances the workflow when appropriate.

### Jobs and Artifacts

- `GET /jobs/{job_id}`
- `GET /chats/{chat_id}/artifacts/requirements`

Requirement generation is performed as a FastAPI background task. The job status can be polled and the generated Markdown document can be retrieved after completion.

## Staged LLM Workflow

The active web workflow is defined in `app/llm/web_stages.py`:

```text
web_discovery
  -> web_ui_features
  -> web_user_journeys
  -> web_tech_stack
  -> web_generate_requirements
```

Each stage has a dedicated system prompt under `app/web_llm_prompts/`. The prompts require strict JSON responses with fields such as:

- `response`
- `summary`
- `context_patch`
- `advance`

This allows the backend to separate conversational output from machine-readable workflow control.

## Requirement Document Generation

When the user completes the tech-stack stage and the system advances into generation, the backend creates a `requirements_doc` job and runs `run_requirements_job`.

The background job:

1. Verifies chat ownership.
2. Marks the job as running.
3. Loads chat context, rolling summary, and recent messages.
4. Calls the LLM once to extract structured requirements JSON.
5. Calls the LLM again to convert those requirements into a Markdown document.
6. Stores the document as a `ChatArtifact`.
7. Adds an assistant message saying the document is ready.
8. Marks the job as done.

## Configuration

Runtime configuration is defined in `app/settings.py` and environment variables.

| Variable | Purpose | Default in code |
| --- | --- | --- |
| `DATABASE_URL` | Async PostgreSQL connection string | `postgresql+asyncpg://admin:admin123@127.0.0.1:5432/myapp_db` |
| `JWT_SECRET` | Secret used to sign JWT tokens | `change-me-super-secret` |
| `JWT_ALG` | JWT signing algorithm | `HS256` |
| `JWT_EXPIRE_HOURS` | Token lifetime in hours | `24` |
| `OPENAI_API_KEY` | API key used by LLM runners | Required, no default |

The LLM modules read `OPENAI_API_KEY` directly from the environment.

## Local Setup

### 1. Create a virtual environment

```bash
python -m venv .venv
```

### 2. Activate the environment

On Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

On macOS or Linux:

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

Based on current imports, the app also expects these packages if they are not already installed:

```bash
pip install openai argon2-cffi httpx
```

### 4. Configure environment variables

Example `.env` values:

```env
DATABASE_URL=postgresql+asyncpg://admin:admin123@127.0.0.1:5432/myapp_db
JWT_SECRET=replace-this-in-real-deployments
JWT_ALG=HS256
JWT_EXPIRE_HOURS=24
OPENAI_API_KEY=your-openai-api-key
```

### 5. Run the API

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

FastAPI documentation will be available at:

```text
http://127.0.0.1:8000/docs
```

## Manual Smoke Test

The repository includes `test.py`, which uses `httpx` to call signup, login, chat creation, message creation, and context endpoints.

Run it after the API and database are available:

```bash
python test.py
```

The script is intended as a local smoke test, not a full automated test suite.

## Current Implementation Status

This repository represents an MVP/concept backend rather than a production-ready product.

Implemented:

- FastAPI backend.
- Async SQLAlchemy database access.
- PostgreSQL-oriented models.
- JWT authentication.
- Chat persistence.
- Structured architecture context.
- Stage-based LLM prompts.
- Requirement-document generation job.

Still expected for production:

- Alembic migrations instead of startup `create_all`.
- Complete automated tests.
- Production dependency lockfile.
- Secure secret management.
- Frontend client.
- Robust job queue such as Celery, RQ, Dramatiq, or a cloud queue.
- Observability, tracing, and structured logs.
- Rate limiting and abuse protection.
- Better error handling around LLM JSON parsing.
- Deployment configuration.

## Why This Project Is Interesting

The repository demonstrates a practical architecture for turning a free-form conversation into structured software-planning artifacts. It combines:

- Conversational UX.
- Deterministic workflow stages.
- LLM-powered extraction.
- Persistent structured context.
- Background artifact generation.

That combination is a strong foundation for an AI product-planning assistant that can eventually generate requirements, system designs, database plans, API specifications, implementation roadmaps, and architecture diagrams.
