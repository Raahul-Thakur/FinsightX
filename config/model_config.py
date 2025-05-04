MODEL_CONFIG = {
    "llm": {
        "provider": "groq",
        "model": "mistral-7b-instruct",
    },
    "embedding_model": {
        "name": "all-MiniLM-L6-v2",
        "provider": "sentence-transformers"
    },
    "summarizer": {
        "use_groq": True,
        "fallback_model": "TinyLlama"
    },
    "sentiment_model": {
        "name": "ProsusAI/finbert",
        "provider": "huggingface"
    }
}
