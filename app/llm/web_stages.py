from dataclasses import dataclass
from typing import Optional, Literal

ActionType = Optional[Literal["requirement_doc", "architecture_doc"]]

@dataclass(frozen=True)
class StageTransition:
    next_stage: str
    action: ActionType = None


def web_next_transition(current: str) -> StageTransition:
    """
    Deterministic pipeline transition.
    Returns:
      - next_stage: where chat should be assigned
      - action: optional job trigger (requirements_doc / architecture_doc)
    """
    current = (current or "web_discovery").strip()

    if current == "web_discovery":
        return StageTransition("web_ui_features")

    if current == "web_ui_features":
        return StageTransition("web_user_journeys")

    if current == "web_user_journeys":
        return StageTransition("web_budget_timeline")

    if current == "web_budget_timeline":
        return StageTransition("web_tech_stack")

    # ✅ After tech stack: trigger requirements generation ONCE
    if current == "web_tech_stack":
        return StageTransition(
            next_stage="web_architecture_finalization",
            action="requirement_doc",
        )

    # ✅ When architecture is approved: trigger architecture job ONCE
    if current == "web_architecture_finalization":
        return StageTransition(
            next_stage="web_post_arch_discussion",
            action="architecture_doc",
        )

    # final stage stays final
    return StageTransition("web_post_arch_discussion")


# WEB_PIPELINE = [
#     "web_discovery",
#     "web_ui_features",
#     "web_user_journeys",
#     "web_budget_timeline",
#     "web_tech_stack",
#     "web_generate_requirements",
# ]

# def web_next_stage(current: str) -> str:
#     try:
#         idx = WEB_PIPELINE.index(current)
#     except ValueError:
#         return "web_discovery"
#     nxt = idx + 1
#     if nxt >= len(WEB_PIPELINE):
#         print("Return web_generate_requirements")
#         return "web_generate_requirements"
#     print("Returning stage:")
#     print(WEB_PIPELINE[nxt])
#     return WEB_PIPELINE[nxt]
