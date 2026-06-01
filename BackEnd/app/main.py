# app/main.py
from fastapi import FastAPI
from app.routes.searcher import router as search_router

app = FastAPI(title="Movie Vector Search API")

# Inclui as rotas de busca
app.include_router(search_router, prefix="/api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)