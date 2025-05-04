from tools.sentiment_tool import analyze_sentiment
from llm.groq_llm import call_groq_mistral

def advise_client(user_input: str) -> str:
    sentiment = analyze_sentiment(user_input)
    prompt = (
        f"A client asked a financial question: '{user_input}'\n"
        f"Their emotional tone is: {sentiment}.\n"
        f"As a financial advisor, provide a thoughtful and empathetic response."
    )
    return call_groq_mistral(prompt)
