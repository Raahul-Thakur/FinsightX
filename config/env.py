import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_API_URL = os.getenv("GROQ_API_URL", "https://api.groq.com/openai/v1/chat/completions")
HF_TOKEN = os.getenv("HF_TOKEN")
CHROMA_DB_PATH = os.getenv("CHROMA_DB_PATH", "./chroma")

print("GROQ_API_KEY Loaded:", bool(GROQ_API_KEY))
