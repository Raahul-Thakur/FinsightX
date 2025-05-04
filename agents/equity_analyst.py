from tools.sentiment_tool import analyze_sentiment
from tools.autorag_tool import query_equity_kb
from llm.groq_llm import call_groq_mistral

def answer_equity_question(query: str) -> str:
    context = query_equity_kb(query)
    sentiment = analyze_sentiment(context)

    prompt = (
        f"Analyze this equity context:\n{context}\n\n"
        f"Sentiment of the data: {sentiment}.\n"
        f"Provide a concise financial analysis and any risks or opportunities."
    )
    return call_groq_mistral(prompt)
