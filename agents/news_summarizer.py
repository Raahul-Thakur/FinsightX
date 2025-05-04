from llm.summarizer import summarize
from tools.autorag_tool import query_equity_kb

def summarize_market_news(news_text: str) -> str:
    # You can use summarizer directly or summarize context if preloaded into KB
    context = query_equity_kb(news_text)
    return summarize(context or news_text)
