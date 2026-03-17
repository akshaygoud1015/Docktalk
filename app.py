import streamlit as st

st.title("DocTalk")

uploaded_file = st.file_uploader("Upload PDF")

query = st.text_input("Ask a question")

if query:
    results = query_docs(query)
    answer = generate_answer(query, results)
    st.write(answer)