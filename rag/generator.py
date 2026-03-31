import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3.2"

def generate_answer(query, context_chunks):
    context = "\n\n".join(context_chunks)

    prompt = (
        f"Answer the question based ONLY on the context below. "
        f"If the answer is not in the context, say 'I don't know'.\n\n"
        f"Context:\n{context}\n\n"
        f"Question:\n{query}"
    )

    response = requests.post(OLLAMA_URL, json={
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    })

    response.raise_for_status()
    return response.json()["response"]