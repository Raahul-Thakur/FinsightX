from tools.autorag_tool import query_equity_kb
from llm.groq_llm import call_groq_mistral

SAFE_RESPONSE = "No reliable regulatory context found. Provide a specific rule, agency, or filing to analyze."


def monitor_regulatory_changes(text: str) -> str:
    context = query_equity_kb(text)
    if not context:
        return SAFE_RESPONSE
    prompt = (
        f"You are a compliance analyst. Evidence from the knowledge base:\n{context}\n\n"
        f"Summarize the regulatory change and investor impact. If context is thin, say it explicitly and avoid speculation."
    )
    return call_groq_mistral(prompt)
