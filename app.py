import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

from rag.loader import extract_text
from rag.chunker import chunk_text
from rag.retriever import add_chunks, query_docs
from rag.generator import generate_answer

st.title("DocTalk")

uploaded_file = st.file_uploader("Upload PDF")

if uploaded_file:
    text = extract_text(uploaded_file)
    chunks = chunk_text(text)

    add_chunks(chunks)
    st.success("Document processed!")

query = st.text_input("Ask a question")

if query:
    results = query_docs(query)
    answer = generate_answer(query, results)
    st.write(answer)