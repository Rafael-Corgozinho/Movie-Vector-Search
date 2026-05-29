from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

# Validação de dados de entrada com Pydantic
class SearchQuery(BaseModel):
    query: str

@router.post("/search")
def search_movies(payload: SearchQuery):
    # O payload.query contém a string (ex: "Quero algo como Se7en")
    # Futuramente, a chamada para o Sentence Transformer e ChromaDB entrará aqui.
    
    return {
        "query_recebida": payload.query,
        "mock_resultados": ["Filme A", "Filme B"]
    }