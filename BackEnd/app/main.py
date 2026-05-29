from fastapi import FastAPI

app = FastAPI(title ="Vector search")

@app.get("/")
def health_check():
    return {"status": "online", "message": "API do MVP funcionando."}
