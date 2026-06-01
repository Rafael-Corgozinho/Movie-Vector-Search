import chromadb
from pathlib import Path
from sentence_transformers import SentenceTransformer

BASE_DIR = Path(__file__).resolve().parent.parent
CHROMA_PATH = BASE_DIR / "data" / "chroma_db"

model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.PersistentClient(path=str(CHROMA_PATH))
collection = client.get_collection("movies")

def search_movies(query: str, n_results: int = 5):
    query_embedding = model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results
    )

    movies = []

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]
    distances = results["distances"][0]

    for document, metadata, distance in zip(documents, metadatas, distances):
        movies.append({
            "title": metadata.get("title"),
            "genre": metadata.get("genre"),
            "cast": metadata.get("cast"),
            "description": metadata.get("description"),
            "similarity": round(1 - distance, 4)
        })

    return movies