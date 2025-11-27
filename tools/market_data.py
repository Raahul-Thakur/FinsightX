import yfinance as yf


def fetch_public_financials(ticker: str) -> dict | None:
    try:
        tk = yf.Ticker(ticker)
        info = tk.get_info()
        financials = {
            "market_cap": info.get("marketCap"),
            "pe_ratio": info.get("trailingPE") or info.get("forwardPE"),
            "revenue_ttm": info.get("totalRevenue") or info.get("revenueTTM"),
            "gross_margins": info.get("grossMargins"),
            "ebitda": info.get("ebitda"),
        }
        cleaned = {k: v for k, v in financials.items() if v is not None}
        if not cleaned:
            return None
        return cleaned
    except Exception:
        return None


def format_financials(metrics: dict | None) -> str:
    if not metrics:
        return "No market metrics available from yFinance."
    return "\n".join([f"- {k}: {v}" for k, v in metrics.items()])
