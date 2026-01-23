import os
from openai import OpenAI

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise RuntimeError("OPENAI_API_KEY is not set")

client = OpenAI(api_key=api_key)


def generate_requirements_doc(chat_context: dict, rolling_summary: str, messages: list[dict]) -> str:
    """
    Production-ish MVP: two calls:
    1) Extract structured requirements JSON
    2) Convert to a nice Markdown document
    """
    print("MESSAGES:")
    print(messages)
    print("######################")
    # --- Call 1: extract structured requirements ---
    sys1 = (
        "You are a senior product analyst. Extract a structured requirements JSON.\n"
        "Return STRICT JSON only."
    )

    user1 = {
        "rolling_summary": rolling_summary,
        "chat_context": chat_context,
        "messages": messages[-80:],  # keep last N to avoid huge prompt
    }

    r1 = client.responses.create(
        model="gpt-5.2",
        input=[
            {"role": "system", "content": sys1},
            {"role": "user", "content": f"Extract requirements JSON from:\n{user1}"},
        ],
    )
    requirements_json = r1.output_text.strip()
    
    print("First background call:")
    print(requirements_json)

    # --- Call 2: convert to markdown doc ---
    sys2 = (
        "You are a senior solutions architect.\n"
        "Using the provided requirements JSON, write a high-quality Markdown requirement document.\n"
        "Include: Overview, Goals, Scope, Personas, User Journeys, Functional Requirements, Non-Functional, Assumptions, Open Questions.\n"
        "Return Markdown only."
    )

    r2 = client.responses.create(
        model="gpt-5.2",
        input=[
            {"role": "system", "content": sys2},
            {"role": "user", "content": f"Requirements JSON:\n{requirements_json}"},
        ],
    )

    doc_md = r2.output_text.strip()
    print("CALL @2")
    print(doc_md)
    return doc_md
