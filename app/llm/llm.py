import json
from openai import OpenAI
import os
# from dotenv import load_dotenv
# api_key = os.getenv("OPENAI_API_KEY")
# if not api_key:
#     raise ValueError("OPENAI_API_KEY is not set in your environment or .env file")
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise RuntimeError("OPENAI_API_KEY is not set")

client = OpenAI(api_key=api_key)

# ===== Agent Registry =====
AGENTS = {
    "web_app": "You are the Web App Architecture Agent. Produce architecture, DB schema hints, API routes, and deployment notes for web apps.",
    "mobile_app": "You are the Mobile App Architecture Agent. Focus on iOS/Android choices, backend APIs, auth, push, analytics, and offline sync.",
    "web_mobile": "You are the Web+Mobile Architecture Agent. Ensure shared backend, auth, APIs, and consistent domain model.",
    "chatbots": "You are the Chatbots Agent. Focus on WhatsApp/Instagram/Web widget bots, webhooks, message templates, flows, rate limits, and infra.",
    "voice": "You are the Voice/Calling Agent. Focus on voice pipelines, telephony providers, ASR/TTS, latency, streaming, call flows, compliance.",
    "rag": "You are the RAG/Knowledge Systems Agent. Focus on ingestion, chunking, embeddings, vector DB, retrieval, eval, security, and ops.",
    "identity_ai": "You are the Identity AI Agent. Focus on authentication, authorization, IAM, RBAC/ABAC, SSO, audit logs, privacy, compliance.",
    "workflow_automation": "You are the Workflow Automation Agent. Focus on orchestration (n8n/Airflow/Temporal), triggers, retries, idempotency, observability.",
    "product_combo": "You are the Product Combos Agent. Help choose combinations like WhatsApp+Web, WhatsApp+Mobile, Web+App and define MVP scope."
}

# ===== Orchestrator prompt =====
ORCHESTRATOR_SYSTEM = f"""
You are the Orchestrator for a software-architecture assistant.

Your job:
1) Ask clarifying questions until the user's intent is clear.
2) Once intent is clear, assign the chat to ONE agent from the allowed list below.
3) Keep 'summary' VERY short (max 20 words) and ONLY new durable info from this turn (it will be appended by server).

Return STRICT JSON with keys:
- response: string
- summary: string (may be empty)
- assigned_to: string | null

Allowed assigned_to values:
{list(AGENTS.keys())}

Rules for assigned_to:
- If intent NOT clear, assigned_to must be null.
- If intent is clear, pick the best single agent key.
- If user wants multiple areas, choose the closest primary and ask followups.
""".strip()


def call_llm(system_prompt: str, payload: dict) -> dict:
    print("""LLM CALL""")
    print("SYSTEM:")
    print(system_prompt)
    print("PAYLOAD")
    print(payload)
    resp = client.responses.create(
        model="gpt-5.2",
        input=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": json.dumps(payload, ensure_ascii=False)},
        ],
    )
    text = resp.output_text.strip()
    print("TEXT")
    print(text)
    try:
        return json.loads(text)
    except Exception:
        return {"response": text, "summary": "", "assigned_to": None}


def run_orchestrator(user_message: str, rolling_summary: str | None, chat_context: dict | None = None) -> dict:
    payload = {
        "rolling_summary": rolling_summary or "",
        "chat_context": chat_context or {},
        "user_message": user_message,
    }
    return call_llm(ORCHESTRATOR_SYSTEM, payload)


def run_agent(agent_key: str, user_message: str, rolling_summary: str | None, chat_context: dict | None = None) -> dict:
    agent_system = f"""
You are an architecture assistant agent: {agent_key}.
Answer the user's request with practical architecture guidance.
Return STRICT JSON with keys:
- response: string
- summary: string (max 20 words; durable info only; may be empty)
- assigned_to: null
""".strip()

    payload = {
        "agent": agent_key,
        "rolling_summary": rolling_summary or "",
        "chat_context": chat_context or {},
        "user_message": user_message,
    }
    return call_llm(agent_system, payload)

# # SYSTEM = (
# #     "You are an assistant inside a chat app backend. "
# #     "Return STRICT JSON with keys: response (string), summary (string). "
# #     "summary must be a short rolling memory of the chat (1-3 sentences) that can be used next turn."
# # )

# SYSTEM = (
#     "You are an assistant inside a chat app backend.\n"
#     "Return STRICT JSON with keys:\n"
#     "1) response: string\n"
#     "2) summary: string\n\n"
#     "Rules for summary:\n"
#     "- VERY short\n"
#     "- This is NOT the full conversation summary.\n"
#     "- It is ONLY a tiny memory chunk from THIS TURN that will be appended to existing memory by the server.\n"
#     "- Max 20 words.\n"
#     "- Only include durable info worth remembering (preferences, goals, decisions, constraints).\n"
# )
# def call_llm(user_message: str, rolling_summary: str | None) -> dict:
#     prompt = {
#         "rolling_summary": rolling_summary or "",
#         "user_message": user_message
#     }
#     print("Prompt:")
#     print(prompt)
#     resp = client.responses.create(
#         model="gpt-5.2",
#         input=[
#             {"role": "system", "content": SYSTEM},
#             {"role": "user", "content": f"Input:\n{json.dumps(prompt, ensure_ascii=False)}"}
#         ],
#     )

#     text = resp.output_text.strip()
#     print("########################")
#     print(text)
#     print("########################")

#     # basic safe parse
#     try:
#         return json.loads(text)
#     except Exception:
#         # fallback: best-effort extraction
#         return {"response": text, "summary": rolling_summary or ""}
