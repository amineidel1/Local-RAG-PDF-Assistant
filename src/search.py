from sentence_transformers import SentenceTransformer
import chromadb
from pathlib import Path

# Charger modèle embeddings
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

question = "What is Amine's degree?"

query_embedding = model.encode(question)

results = collection.query(
    query_embeddings=[
        query_embedding.tolist()
    ],
    n_results=1
)

print(results["documents"][0][0])