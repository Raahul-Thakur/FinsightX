import sys
import os
import streamlit as st
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from agents.equity_analyst import answer_equity_question
from agents.news_summarizer import summarize_market_news
from agents.macro_strategist import analyze_macro_trends
from agents.quant_backtester import run_simple_backtest
from agents.regu_radar import monitor_regulatory_changes
from agents.client_advisor import advise_client

st.set_page_config(page_title="FinSightX", layout="wide")

st.title("FinSightX: AI-Powered Financial Agent Suite")

agent = st.sidebar.selectbox(
    "Choose Agent",
    [
        "Home",
        "Equity Analyst",
        "News Summarizer",
        "Macro Strategist",
        "Quant Backtester",
        "ReguRadar",
        "Client Advisor"
    ]
)


if agent == "Home":
    st.header("A Multi-Agent Financial Intelligence Assistant")
    st.markdown("""
    A **modular industry-grade application** where agents collaborate to handle:

    - **Equity Research**
    - **News Summarization**
    - **Macroeconomic Analysis**
    - **Quantitative Backtesting**
    - **Regulatory Updates**
    - **Client Portfolio Q&A**
    """)

elif agent == "Equity Analyst":
    st.subheader("Equity Analyst")
    st.markdown("""
    ### Role:
    Analyzes individual stocks or companies using:
    - Financial filings (e.g., 10-K, 10-Q)
    - Earnings call summaries
    - Market sentiment

    ### Capabilities:
    - Retrieve documents from a knowledge base using **AutoRAG**
    - Run sentiment analysis (FinBERT)
    - Generate insight using LLM (Groq Mistral)
    - Summarize risks, opportunities, and outlook

    ### Example Use Cases:
    - "What’s the market sentiment around Tesla this quarter?"
    - "Give me an analysis of Apple’s earnings call."
    """)
    query = st.text_input("Enter your financial query about a stock or company:")
    if st.button("Analyze"):
        with st.spinner("Analyzing equity..."):
            response = answer_equity_question(query)
        st.markdown(response)

elif agent == "News Summarizer":
    st.subheader("News Summarizer")
    st.markdown("""
    ### Role:
    Digest and summarize **real-time or bulk market news** to extract insights and relevance.

    ### Capabilities:
    - Accept raw headlines or long-form articles
    - Retrieve context (e.g., related documents or sectors)
    - Summarize using LLM (via Groq or fallback)

    ### Use Cases:
    - "Summarize today’s financial news relevant to energy stocks."
    - "Give me a brief on Nvidia's latest product announcement."
    """)
    news = st.text_area("Paste financial news or headlines:")
    if st.button("Summarize News"):
        with st.spinner("Summarizing..."):
            summary = summarize_market_news(news)
        st.markdown(summary)

elif agent == "Macro Strategist":
    st.subheader("Macro Trend Forecaster")
    st.markdown("""
    ### Role:
    Analyzes **macroeconomic indicators** and helps in trend forecasting.

    ### Capabilities:
    - Forecasts economic time series (CPI, GDP, unemployment) using `neuralprophet`
    - Returns structured future outlooks
    - Used in multi-agent reasoning for “market climate”

    ### Use Cases:
    - "Forecast US inflation for the next 3 months."
    - "What does the GDP trend look like post-2023?"
    """)
    st.markdown("Upload a time series CSV with columns `ds` (date) and `y` (value).")
    uploaded_file = st.file_uploader("Upload CSV", type=["csv"])
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        if st.button("Forecast"):
            with st.spinner("Forecasting..."):
                forecast_result = analyze_macro_trends(df)
            st.write("Forecasted Value:")
            st.json(forecast_result)

elif agent == "Quant Backtester":
    st.subheader("Quant Strategy Backtester")
    st.markdown("""
    ### Role:
    Tests trading strategies on historical price data.

    ### Capabilities:
    - Define and run strategies using `bt` or `vectorbt`
    - Simple moving average crossovers, rebalancing, etc.
    - Return backtest performance metrics

    ### Use Cases:
    - "Backtest an SMA crossover on AAPL from 2020 to 2023."
    - "Run a balanced ETF strategy on SPY, QQQ, and VTI."

    > This agent focuses on backtesting, not execution or portfolio construction (those can be added later).
    """)
    tickers = st.text_input("Enter tickers (comma-separated)", value="AAPL,MSFT")
    sma_short = st.number_input("Short SMA", value=20)
    sma_long = st.number_input("Long SMA", value=50)
    if st.button("Run Backtest"):
        with st.spinner("Backtesting strategy..."):
            result = run_simple_backtest(
                tickers=[t.strip() for t in tickers.split(",")],
                sma_short=sma_short,
                sma_long=sma_long
            )
        st.write("Backtest completed. Check your terminal/logs for output.")
        st.markdown("Note: Visual performance plots not yet integrated in Streamlit.")

elif agent == "ReguRadar":
    st.subheader("ReguRadar – Regulatory Monitor")
    st.markdown("""
    ### Role:
    Monitors and interprets **regulatory updates** that may affect sectors, firms, or compliance requirements.

    ### Capabilities:
    - AutoRAG over legal and regulatory filings (e.g., RBI circulars, SEC rules)
    - LLM summarization to extract impact
    - Optional: track historical regulatory shifts

    ### Use Cases:
    - "Has the RBI changed anything that affects crypto investors?"
    - "Summarize the SEC’s latest ESG compliance memo."
    """)
    reg_query = st.text_area("Paste a regulatory update or query:")
    if st.button("Analyze Regulation"):
        with st.spinner("Scanning for relevance..."):
            reg_response = monitor_regulatory_changes(reg_query)
        st.markdown(reg_response)

elif agent == "Client Advisor":
    st.subheader("Client Advisor")
    st.markdown("""
    ### Role:
    Acts as a **virtual financial advisor**, helping individual users based on their queries and emotional tone.

    ### Capabilities:
    - Understand user intent + emotion using FinBERT
    - Generate personalized advice using Groq LLM
    - Can be expanded into user profile tracking (e.g., risk appetite, goals)

    ### Use Cases:
    - "Should I invest in tech during a recession? I’m scared of losing money."
    - "I’ve retired and need a low-risk investment plan."

    > In the future, this can evolve into a memory-based portfolio coach.
    """)
    user_msg = st.text_area("What does your client say?")
    if st.button("Advise"):
        with st.spinner("Analyzing sentiment and crafting advice..."):
            advice = advise_client(user_msg)
        st.markdown(advice)
