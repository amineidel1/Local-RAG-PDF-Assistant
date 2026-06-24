import chromadb
from sentence_transformers import SentenceTransformer
import ollama
from pathlib import Path

model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

BASE_DIR = Path(__file__).resolve().parent.parent

CHROMA_PATH = BASE_DIR / "data" / "chroma_db"

client = chromadb.PersistentClient(
    path=str(CHROMA_PATH)
)

collection = client.get_collection(
    "pdf_documents"
)

question = input("Question: ")

query_embedding = model.encode(question)

results = collection.query(
    query_embeddings=[
        query_embedding.tolist()
    ],
    n_results=1
)

context = results["documents"][0][0]

prompt = f"""
Answer the question using ONLY the context below.

Context:
{context}

Question:
{question}
"""

response = ollama.chat(
    model="qwen2.5:7b",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

print("\nAnswer:")
print(response["message"]["content"])

