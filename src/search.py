from sentence_transformers import SentenceTransformer
import chromadb

# Charger modèle embeddings
model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

# Connexion ChromaDB
client = chromadb.PersistentClient(
    path="./data/chroma_db"
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