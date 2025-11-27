from config.model_config import MODEL_CONFIG
from llm.groq_llm import call_groq_mistral


def summarize(text: str) -> str:
    prompt = (
        "You are a grounded financial summarizer. Only use the supplied text. "
        "If it lacks detail, state that context is limited.\n\n" + text
    )

    if MODEL_CONFIG["summarizer"]["use_groq"]:
        return call_groq_mistral(prompt)
    else:
        return "Fallback LLM not enabled"
