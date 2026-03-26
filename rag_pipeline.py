import pandas as pd
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from transformers import pipeline

def create_rag():
    # Load Excel
    df = pd.read_excel("data/serverbasket_full_data.xlsx")

    texts = []
    for _, row in df.iterrows():
        text = " ".join([str(value) for value in row])
        texts.append(text)

    # Create vector DB
    embeddings = HuggingFaceEmbeddings()
    db = FAISS.from_texts(texts, embeddings)

    # Load model
    generator = pipeline("text-generation", model="google/flan-t5-base")

    # Ask function (IMPORTANT: inside create_rag)
    def ask(query):
        docs = db.similarity_search(query, k=2)
        context = " ".join([d.page_content for d in docs])

        prompt = f"Answer based on context:\n{context}\nQuestion: {query}"

        result = generator(prompt, max_length=200)
        return result[0]['generated_text']

    return ask   # ✅ INSIDE FUNCTION