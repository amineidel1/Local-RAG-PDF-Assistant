from pathlib import Path
import chromadb

BASE_DIR = Path(__file__).resolve().parent.parent

CHROMA_PATH = BASE_DIR / "data" / "chroma_db"

print("Path:", CHROMA_PATH)

client = chromadb.PersistentClient(
    path=str(CHROMA_PATH)
)

collections = client.list_collections()

print(collections)