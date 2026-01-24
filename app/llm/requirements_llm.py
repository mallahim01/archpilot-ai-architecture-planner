import os
from pathlib import Path
import json
import anyio
import asyncio
from app.llm.extraction.web_knowledge_extractor import extract_knowledge_from_chat
from app.llm.extraction.save_extraction import save_extracted_knowledge_to_files
from app.llm.extraction.founder_brief import generate_founder_brief_document
from app.llm.extraction.requirements_doc import generate_requirements_document
from app.llm.extraction.user_journeys_doc import generate_user_journeys_document
from app.llm.extraction.delivery_plan_doc import generate_delivery_plan_document
from app.llm.extraction.risk_assumptions_doc import generate_risk_assumptions_document

async def generate_requirements_doc(
    job_id: str,
    chat_context: dict,
    rolling_summary: str,
    messages: list[dict],  # you said: oldest -> newest
) -> str:
    print("Inside job data extraction.........")
    print("Messages:")
    # print(messages)
    print("#########################")
    
    extracted = ''

    extracted = await extract_knowledge_from_chat(
        chat_context=chat_context,
        rolling_summary=rolling_summary or "",
        messages=messages,          # IMPORTANT: pass as-is
        model="gpt-4o",
        batch_size=4,
        max_parallel=6,
    )

    print("EXTRACTED KNOWLEDGE:")
    print(json.dumps(extracted, indent=2, ensure_ascii=False))
    # ✅ Save 6 documents + full json snapshot
    base_dir = Path(__file__).parent / "extraction" / "data"
    paths = save_extracted_knowledge_to_files(
        job_id=job_id,
        extracted=extracted,
        base_dir=base_dir,
    )

    print("Saved extraction files:")
    for k, p in paths.items():
        print(f"  {k}: {p}")
    print("JOB ID:")
    print(str(job_id))
    print("Generating Founder brief:")
    paths = await generate_founder_brief_document(job_id=str(job_id), model="gpt-4o")
    print(paths["md_path"])
    
    print("Generating Requirement document:")
    paths = await generate_requirements_document(
    job_id=str(job_id),
    model="gpt-4o",
    debug_preview=True,
    )
    print("Saved:", paths["md_path"])
    
    print("Generating User Journyes:")
    result = await generate_user_journeys_document(job_id=str(job_id), model="gpt-4o")
    print(result["path"])
    
    print("Generating Delivery Plan:")
    result = await generate_delivery_plan_document(job_id=str(job_id), model="gpt-4o")
    print(result["path"])
    
    print("Generating Risk Assumptions:")
    result = await generate_risk_assumptions_document(job_id=str(job_id), model="gpt-4o")
    print(result["path"])
    

    # Return JSON string for now (you’re storing it in DB artifact)
    return json.dumps(
        {
            "job_id": job_id,
            "saved_files": paths,
            "extracted": extracted,
        },
        ensure_ascii=False,
        indent=2,
    )

    # # return as json string for now
    # return json.dumps(extracted, ensure_ascii=False, indent=2)


# def generate_requirements_doc(chat_context: dict, rolling_summary: str, messages: list[dict]) -> str:
    
#     print("MESSAGES:")
#     print(messages)
#     print("######################")
#     # --- Call 1: extract structured requirements ---
#     sys1 = (
#         "You are a senior product analyst. Extract a structured requirements JSON.\n"
#         "Return STRICT JSON only."
#     )

#     user1 = {
#         "rolling_summary": rolling_summary,
#         "chat_context": chat_context,
#         "messages": messages[-80:],  # keep last N to avoid huge prompt
#     }

#     # r1 = client.responses.create(
#     #     model="gpt-5.2",
#     #     input=[
#     #         {"role": "system", "content": sys1},
#     #         {"role": "user", "content": f"Extract requirements JSON from:\n{user1}"},
#     #     ],
#     # )
#     # requirements_json = r1.output_text.strip()
    
#     # print("First background call:")
#     # print(requirements_json)

#     # # --- Call 2: convert to markdown doc ---
#     # sys2 = (
#     #     "You are a senior solutions architect.\n"
#     #     "Using the provided requirements JSON, write a high-quality Markdown requirement document.\n"
#     #     "Include: Overview, Goals, Scope, Personas, User Journeys, Functional Requirements, Non-Functional, Assumptions, Open Questions.\n"
#     #     "Return Markdown only."
#     # )

#     # r2 = client.responses.create(
#     #     model="gpt-5.2",
#     #     input=[
#     #         {"role": "system", "content": sys2},
#     #         {"role": "user", "content": f"Requirements JSON:\n{requirements_json}"},
#     #     ],
#     # )

#     # doc_md = r2.output_text.strip()
#     # print("CALL @2")
#     # print(doc_md)
#     doc_md = 'abc'
#     print("JOB COMPLETED...............")
#     return doc_md
