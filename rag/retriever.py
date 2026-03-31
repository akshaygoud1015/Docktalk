import chromadb
from rag.embeddings import get_embedding

client = chromadb.Client()
collection = client.get_or_create_collection("docs")

def add_chunks(chunks):
    for i, chunk in enumerate(chunks):
        collection.add(
            documents=[chunk],
            embeddings=[get_embedding(chunk)],
            ids=[str(i)]
        )

def query_docs(query, k=5):
    query_embedding = get_embedding(query)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=k
    )

    return results['documents'][0]