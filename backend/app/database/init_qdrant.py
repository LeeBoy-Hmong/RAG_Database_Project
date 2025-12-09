from qdrant_client import QdrantClient, models
from app.services.embedding_services import model, model2, model3

def init_qdrant():
    qdrant = QdrantClient(url="http://localhost:6333")
    embedding_dim = model.get_sentence_embedding_dimension()
    # print(The embedding dimension of this model is: {embedding_dim} ")
    qdrant.recreate_collection(
        collection_name= "document-vectors",
        vectors_config= models.VectorParams(size=embedding_dim, distance=models.Distance.COSINE)
    )

'''def init_qdrant2():
    qdrant = QdrantClient("http://localmachine:6333")
    embedding_dim = model2.get_sentence_embedding_dimension()
    qdrant.recreate_collection(
        collection_name ="new-document",
        vectors_config = models.VectorParams(size=embedding_dim, distance=models.Distance.COSINE)
    )'''

'''def init_qdrant3():
    qdrant = QdrantClient("https://localhost:6333")
    embedding_dim = model3.get_sentence_embedding_dimension()
    qdrant.recreate_collection(
        collection_name="document3-collection",
        vectors_config = models.VectorParams(size=embedding_dim, distance=models.Distance.COSINE)
    )'''