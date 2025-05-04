import chromadb

client = chromadb.Client()
collection = client.get_or_create_collection("finsightx_kb")

def add_to_db(doc_id: str, text: str, embedding):
    collection.add(ids=[doc_id], documents=[text], embeddings=[embedding])

def query(text: str, embed_fn) -> dict:
    query_embedding = embed_fn(text)
    return collection.query(query_embeddings=[query_embedding], n_results=3)
