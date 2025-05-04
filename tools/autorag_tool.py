from embeddings.embedder import get_embedding
from embeddings.vector_store import query

def query_equity_kb(text: str) -> str:
    results = query(text, get_embedding)
    return "\n".join(results["documents"][0]) if results and results["documents"] else "No relevant documents found."
