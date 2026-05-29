from fastapi import FastAPI

app = FastAPI(title ="Vector search")


app.include_router(seacher.router)


@app.get("/")
def health_check():
    return {"status": "online", "message": "API do MVP funcionando."}
