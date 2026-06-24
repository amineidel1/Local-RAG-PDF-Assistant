from sentence_transformers import SentenceTransformer
from chunking import create_chunks
import chromadb
from pathlib import Path

# Charger le modèle embeddings
model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

BASE_DIR = Path(__file__).resolve().parent.parent

CHROMA_PATH = BASE_DIR / "data" / "chroma_db"

client = chromadb.PersistentClient(
    path=str(CHROMA_PATH)
)

collection = client.get_or_create_collection(
    name="pdf_documents"
)

# Exemple texte
sample_text = """
Amine Idelhaj is an AI Engineer.

He holds a Master's degree in Data and Intelligence for Smart Systems.

He works on Machine Learning, NLP, RAG systems and Large Language Models.
"""

# Création des chunks
chunks = create_chunks(sample_text)

print(f"Chunks created: {len(chunks)}")

# Génération des embeddings
embeddings = model.encode(chunks)

# Sauvegarde dans ChromaDB
collection.add(
    documents=chunks,
    embeddings=embeddings.tolist(),
    ids=[f"chunk_{i}" for i in range(len(chunks))]
)

print("Stored successfully in ChromaDB")