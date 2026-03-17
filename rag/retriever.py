import chromadb

client = chromadb.Client()
collection = client.create_collection("docs")

for i, chunk in enumerate(chunks):
    collection.add(
        documents=[chunk],
        embeddings=[get_embedding(chunk)],
        ids=[str(i)]
    )