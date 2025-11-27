import chromadb
from chromadb.config import Settings
from config.env import CHROMA_DB_PATH

# Persistent client ensures we keep previously embedded financial documents.
client = chromadb.PersistentClient(path=CHROMA_DB_PATH, settings=Settings(anonymized_telemetry=False))
collection = client.get_or_create_collection("finsightx_kb")


def add_to_db(doc_id: str, text: str, embedding, metadata=None):
    collection.add(
        ids=[doc_id],
        documents=[text],
        embeddings=[embedding],
        metadatas=[metadata or {}],
    )


def query(text: str, embed_fn, where: dict | None = None) -> dict:
    query_embedding = embed_fn(text)
    return collection.query(query_embeddings=[query_embedding], n_results=5, where=where or {})


def count_documents() -> int:
    return collection.count()
