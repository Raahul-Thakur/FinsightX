from llm.summarizer import summarize
from tools.autorag_tool import query_equity_kb

SAFETY_MESSAGE = "No trusted context available to summarize this news. Please share more detail or a company name."


def summarize_market_news(news_text: str) -> str:
    context = query_equity_kb(news_text)
    if not (context or news_text.strip()):
        return SAFETY_MESSAGE
    seed_text = "\n".join(filter(None, [context, news_text]))
    return summarize(seed_text)
