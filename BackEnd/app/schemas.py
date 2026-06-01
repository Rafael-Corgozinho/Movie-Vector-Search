from pydantic import BaseModel
from typing import List

class MovieResult(BaseModel):
    title: str
    genre: str
    cast: str
    description: str
    similarity: float

class SearchResponse(BaseModel):
    results: List[MovieResult]