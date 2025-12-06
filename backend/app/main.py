from fastapi import FastAPI
from app.database.init_qdrant import init_qdrant

app = FastAPI()

@app.on_event("startup")
def startup_event():
    init_qdrant()

 
@app.get("/health")
def health():
    return({"status": "ok"})
