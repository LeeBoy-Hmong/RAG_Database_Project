from fastapi import FastAPI
from qdrant_client import QdrantClient, models
from sentence_transformers import SentenceTransformer

qdrant = QdrantClient(url="http://localhost:6333")
model = SentenceTransformer("all-MiniLM-L6-v2")

embedding_dim = model.get_sentence_embedding_dimension()
#print(The embedding dimension of this model is: {embedding_dim} ")  #Test run what my embedding dimension is prior to setting the configuration.

@app.on_event("startup")
def __init__qdrant():
    qdrant.recreate_collection(  # Better practice for production than .create_collection
        collection_name="document-vectors",
        vectors_config=models.VectorParams(size=embedding_dim, distance=models.Distance.COSINE)  # Configuration prep for 'all-mpmet-basae-v2' model
    )

@app.get("health")
def health():
    return({"status": "ok"})
