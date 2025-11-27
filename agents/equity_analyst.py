from tools.sentiment_tool import analyze_sentiment
from tools.autorag_tool import query_equity_kb
from tools.company_resolver import resolve_company
from tools.market_data import fetch_public_financials, format_financials
from llm.groq_llm import call_groq_mistral


SAFETY_FALLBACK = (
    "No reliable filings, earnings excerpts, or market data were available for this query. "
    "Please provide a valid ticker or company name so I can search again."
)


def answer_equity_question(query: str) -> str:
    company_info = resolve_company(query)
    sentiment = analyze_sentiment(query)

    context = query_equity_kb(query, company=company_info.company or company_info.ticker)
    vc_context = query_equity_kb(query, company=company_info.company, doc_types=["vc_case"])

    metrics = fetch_public_financials(company_info.ticker) if company_info.is_public and company_info.ticker else None
    metrics_text = format_financials(metrics)

    if not context and not vc_context and not metrics:
        return SAFETY_FALLBACK

    prompt = f"""
You are FinSightX's Equity Analyst. Use only the evidence provided and do not fabricate numbers.
If information is missing, explicitly say so and avoid speculation.

Company resolution: {company_info}
Sentiment of user question: {sentiment}

Retrieved evidence from filings/earnings/VC cases:
{context or 'No SEC filings or earnings excerpts matched.'}
{vc_context or 'No private market case data found.'}

Market metrics (yFinance fallback):
{metrics_text}

Required response format:
- Brief thesis (1-2 bullets)
- Key financial/operational signals (bullet list with doc type labels)
- Risks or uncertainties (avoid inventing data)
- If evidence is thin, say "Insufficient verified context" and stop.
"""
    return call_groq_mistral(prompt)
