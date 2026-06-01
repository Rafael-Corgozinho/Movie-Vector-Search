import pandas as pd
import chromadb
from pathlib import Path
from sentence_transformers import SentenceTransformer

BASE_DIR = Path(__file__).resolve().parent.parent
CSV_PATH = BASE_DIR / "data" / "netflix_titles.csv"
CHROMA_PATH = BASE_DIR / "data" / "chroma_db"

def build_database():
    print("Carregando CSV...")
    df = pd.read_csv(CSV_PATH)
    df = df.fillna("")

    df["overview"] = (
        "Title: " + df["title"] +
        ". Genres: " + df["listed_in"] +
        ". Cast: " + df["cast"] +
        ". Description: " + df["description"]
    )

    print("Carregando modelo...")
    model = SentenceTransformer("all-MiniLM-L6-v2")

    print("Gerando embeddings...")
    embeddings = model.encode(
        df["overview"].tolist(),
        show_progress_bar=True
    )

    print("Criando ChromaDB...")
    client = chromadb.PersistentClient(path=str(CHROMA_PATH))

    collection = client.get_or_create_collection(name="movies")

    # Prepara as listas de dados
    ids = df.index.astype(str).tolist()
    documents = df["overview"].tolist()
    embeddings_list = embeddings.tolist()
    metadatas = [
        {
            "title": row["title"],
            "genre": row["listed_in"],
            "cast": row["cast"],
            "description": row["description"]
        }
        for _, row in df.iterrows()
    ]

    # Define um tamanho seguro para o lote (abaixo do limite de 5461)
    batch_size = 5000
    
    print(f"Inserindo {len(ids)} registros em lotes de {batch_size}...")

    # Faz um loop para inserir os dados em partes
    for i in range(0, len(ids), batch_size):
        fim = min(i + batch_size, len(ids))
        print(f" -> Adicionando lote do índice {i} ao {fim}...")
        
        collection.add(
            ids=ids[i:fim],
            documents=documents[i:fim],
            embeddings=embeddings_list[i:fim],
            metadatas=metadatas[i:fim]
        )

    print("Banco criado com sucesso!")

if __name__ == "__main__":
    build_database()