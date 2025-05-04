from tools.autorag_tool import query_equity_kb
from llm.groq_llm import call_groq_mistral

def monitor_regulatory_changes(text: str) -> str:
    context = query_equity_kb(text)
    prompt = (
        f"The following text contains a regulatory update:\n{context}\n\n"
        f"Summarize the key implications for investors and compliance."
    )
    return call_groq_mistral(prompt)
