---
title: FinSightX - Financial Agent Suite
colorFrom: blue
colorTo: green
sdk: streamlit
sdk_version: 1.29.0
app_file: ui/streamlit_app.py
pinned: false
license: apache-2.0
short_description: Multi-agent AI assistant for finance, news, and analysis.
---

# 📊 FinSightX – AI-Powered Financial Analyst Suite

**FinSightX** is an intelligent, agent-powered financial assistant built using Groq's ultra-fast LLaMA 3.1 models, AutoRAG, and open-source tools. It allows users to query equities, summarize news, run macroeconomic forecasts, test quant strategies, track regulatory changes, and receive client-style advisory responses — all in one lightweight app.

> 💡 Built with Groq API, Hugging Face Transformers, ChromaDB, and Streamlit.

---

## 🚀 Features

| Agent | Role |
|-------|------|
| **EquityAnalystAgent** | Answers stock-specific financial questions using live data and sentiment |
| **NewsSummarizerAgent** | Summarizes market headlines via LLM and retrieval |
| **MacroStrategistAgent** | Forecasts macroeconomic trends using NeuralProphet |
| **QuantBacktesterAgent** | Runs quant strategies using historical price data |
| **ReguRadarAgent** | Scans for key regulatory disclosures |
| **ClientAdvisorAgent** | Provides personalized financial advice based on user tone and goals |

---

## 🛠️ Tech Stack

- **LLM**: `llama-3.1-8b-instant` via Groq API (OpenAI-compatible)
- **Embedding**: `all-MiniLM-L6-v2` (SentenceTransformers)
- **Sentiment Analysis**: `ProsusAI/finbert`
- **Vector DB**: ChromaDB (local)
- **Forecasting**: NeuralProphet
- **Backtesting**: `bt` package
- **UI**: Streamlit

---

## ⚙️ Setup Instructions

1. Clone the repo  
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a .env file:
    ```bash
    GROQ_API_KEY=your_groq_key
    GROQ_API_URL=https://api.groq.com/openai/v1/chat/completions
    ```
4. Run the app:
    ```bash
    streamlit run ui/streamlit_app.py
    ```

## 📉 Current Limitations

- ChromaDB does not yet include 10-K/10-Q or earnings data
- Macro indicators (CPI, interest rates) not integrated
- No real-time alerts or portfolio memory
- No backtest visualization (plotly optional)
- LLaMA 3.1 license is research-only (not commercial)

---

## 📂 Future Improvements

### 📄 Financial Documents to Integrate

| Document                     | Use                                          |
|------------------------------|-----------------------------------------------|
| 10-K / 10-Q                  | Full financial analysis and risk sections     |
| 8-K                          | Instant updates on events, deals, or risks    |
| Earnings Transcripts         | Management commentary and guidance            |
| Investor Presentations       | Visual and forward-looking insights           |
| Proxy Statements (DEF 14A)   | Governance and voting info                    |

### 📊 Financial Metrics to Add

- Free cash flow  
- ROE / ROIC  
- Altman Z-Score  
- Piotroski F-Score  
- Debt/equity & profitability ratios  

### 🌐 Macroeconomic Indicators

| Indicator                | Source                            |
|--------------------------|------------------------------------|
| CPI, GDP, Unemployment   | FRED API / IMF / World Bank        |
| Fed rates, Inflation     | TradingEconomics / OpenBB          |
| Currency / Commodities   | Yahoo Finance / forex-python       |

### 🔌 Tools & Libraries to Integrate

- `sec-api.io` or `sec-edgar-downloader` (for 10-Ks)  
- `openbb` (for macro + financial aggregation)  
- `plotly` (for backtesting visualization)  
- `redis` or `duckdb` (for memory/session tracking)  

---

## 🔮 Future Agent Extensions

| Agent Name             | Description                                                            |
|------------------------|------------------------------------------------------------------------|
| `PortfolioBuilderAgent`| Recommends custom portfolio allocations based on user goals            |
| `RiskMonitorAgent`     | Tracks volatility, drawdowns, exposure and market risk                 |
| `AlertAgent`           | Notifies users of macro shifts, earnings releases, or regulatory events|

---

## 📘 License

Currently for **research and educational purposes only**.  
If using Groq-hosted LLaMA 3.1, ensure compliance with Meta’s licensing.

---

## 👨‍💻 Author

Developed by **Rahul Thakur**  
Want to collaborate or contribute? Fork, star, and connect!