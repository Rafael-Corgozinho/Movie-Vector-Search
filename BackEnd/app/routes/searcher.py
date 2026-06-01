from fastapi import APIRouter
from app.services.search_service import search_movies
from app.schemas import SearchResponse

router = APIRouter()

@router.get("/search", response_model=SearchResponse)
def search(query: str, limit: int = 5):
    results = search_movies(query=query, n_results=limit)
    return {"results": results}