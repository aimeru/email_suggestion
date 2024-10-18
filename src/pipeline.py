from src.llm import process_text_with_llm
from src.models import AiResponse


def suggestion_pipeline(context, manifest):
    try:
        response: AiResponse = process_text_with_llm(context, manifest)
        return response
    except Exception as e:
        # raise f"Process Failed: {e}"
        return f"Process Failed: {e}"
