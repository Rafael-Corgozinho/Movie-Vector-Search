from fastapi import APIRouter
from app.services.search_service import search_movies
# Caso possua um schema definido, mantenha a importação: from app.schemas import SearchResponse

router = APIRouter()

@router.get("/search") # Adicione response_model=SearchResponse caso esteja validando com Pydantic
def search(query: str, limit: int = 5):
    # O serviço já retorna a lista limpa de dicionários
    results = search_movies(query=query, n_results=limit)
    
    return {"results": results}