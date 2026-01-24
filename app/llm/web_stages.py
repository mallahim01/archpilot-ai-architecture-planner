WEB_PIPELINE = [
    "web_discovery",
    "web_ui_features",
    "web_user_journeys",
    "web_budget_timeline",
    "web_tech_stack",
    "web_generate_requirements",
]

def web_next_stage(current: str) -> str:
    try:
        idx = WEB_PIPELINE.index(current)
    except ValueError:
        return "web_discovery"
    nxt = idx + 1
    if nxt >= len(WEB_PIPELINE):
        print("Return web_generate_requirements")
        return "web_generate_requirements"
    print("Returning stage:")
    print(WEB_PIPELINE[nxt])
    return WEB_PIPELINE[nxt]
