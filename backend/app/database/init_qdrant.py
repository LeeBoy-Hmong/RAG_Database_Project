from qdrant_client import QdrantClient, models
from app.services.embedding_services import model

def init_qdrant():
    qdrant = QdrantClient(url="http://localhost:6333")
    embedding_dim = model.get_sentence_embedding_dimension()
    # print(The embedding dimension of this model is: {embedding_dim} ")
    qdrant.recreate_collection(
        collection_name= "document-vectors",
        vectors_config= models.VectorParams(size=embedding_dim, distance=models.Distance.COSINE)
    )