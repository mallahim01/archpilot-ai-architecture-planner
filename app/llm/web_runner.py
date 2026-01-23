import os, json
from openai import OpenAI

from app.web_llm_prompts.web_discovery import WEB_DISCOVERY_SYSTEM
from app.web_llm_prompts.web_ui_features import WEB_UI_FEATURES_SYSTEM
from app.web_llm_prompts.web_user_journeys import WEB_USER_JOURNEYS_SYSTEM
from app.web_llm_prompts.web_tech_stack import WEB_TECH_STACK_SYSTEM

# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
# if not os.getenv("OPENAI_API_KEY"):
#     raise ValueError("OPENAI_API_KEY is not set")
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise RuntimeError("OPENAI_API_KEY is not set")

client = OpenAI(api_key=api_key)
# api_key='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'
# client = OpenAI(api_key=api_key)

SYSTEM_BY_STAGE = {
    "web_discovery": WEB_DISCOVERY_SYSTEM,
    "web_ui_features": WEB_UI_FEATURES_SYSTEM,
    "web_user_journeys": WEB_USER_JOURNEYS_SYSTEM,
    "web_tech_stack": WEB_TECH_STACK_SYSTEM,
}

def web_call_stage_llm(stage: str, payload: dict) -> dict:
    system = SYSTEM_BY_STAGE.get(stage, WEB_DISCOVERY_SYSTEM)
    print("""LLM CALL""")
    print("SYSTEM:")
    print(system)
    print("PAYLOAD")
    print(payload)

    resp = client.responses.create(
        model="gpt-5.2",
        input=[
            {"role": "system", "content": system},
            {"role": "user", "content": json.dumps(payload, ensure_ascii=False)},
        ],
    )
    text = resp.output_text.strip()
    print("TEXT:")
    print(text)
    try:
        return json.loads(text)
    except Exception:
        return {"response": text, "summary": "", "context_patch": None, "advance": False}
