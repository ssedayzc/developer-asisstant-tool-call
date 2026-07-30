from pathlib import Path

from pydantic import ValidationError

from llm.client import llm
from llm.schemas import ToolPlan


ROOT = Path(__file__).resolve().parent.parent
PROMPT_PATH = ROOT / "prompts" / "planner_prompt.txt"
PROMPT = PROMPT_PATH.read_text(encoding="utf-8")


def create_tool_plan(
    user_message: str,
) -> tuple[str, ToolPlan]:
    if not user_message.strip():
        raise ValueError(
            "Kullanıcı mesajı boş olamaz."
        )

    response = llm.generate(
        messages=[
            {
                "role": "system",
                "content": PROMPT,
            },
            {
                "role": "user",
                "content": user_message,
            },
        ],
        schema=ToolPlan.model_json_schema(),
        think=True,
    )

    thinking = response.message.thinking or ""
    content = response.message.content or ""

    try:
        plan = ToolPlan.model_validate_json(content)
    except ValidationError as exc:
        raise RuntimeError(
            "Planner geçerli bir ToolPlan üretemedi.\n\n"
            f"Model çıktısı:\n{content}\n\n"
            f"Doğrulama hatası:\n{exc}"
        ) from exc

    return thinking, plan