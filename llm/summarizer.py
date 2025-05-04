from config.model_config import MODEL_CONFIG
from llm.groq_llm import call_groq_mistral
# from llm.tinyllama_runner import tinyllama_chat  # fallback if needed

def summarize(text: str) -> str:
    prompt = f"Summarize the following article:\n{text}"

    if MODEL_CONFIG["summarizer"]["use_groq"]:
        return call_groq_mistral(prompt)
    else:
        return "🪫 Fallback LLM not enabled"  # or: tinyllama_chat(prompt)
