from transformers import pipeline

sentiment_pipe = pipeline("sentiment-analysis", model="ProsusAI/finbert")

def analyze_sentiment(text: str) -> str:
    result = sentiment_pipe(text)
    return result[0]["label"] if result else "NEUTRAL"
