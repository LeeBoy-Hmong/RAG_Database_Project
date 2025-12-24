from qdrant_client import QdrantClient, models
from backend.app.services.embedding_services import model, model2, model3

def init_qdrant():
    qdrant = QdrantClient(url="http://localhost:6333")
    embedding_dim = model.get_sentence_embedding_dimension()
    # print(The embedding dimension of this model is: {embedding_dim} ")
    if not qdrant.collection_exists("rag_documents"):
        qdrant.create_collection(
            collection_name = "rag_documents",
            vectors_config = models.VectorParams(size = embedding_dim, distance = models.Distance.COSINE)
        )
        print("Collection is created!")
    else:
        print("Using existing Collection: 'rag-documents'")
    return qdrant

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


# Create a function that is going to embed you dimension model into the qdrant database.
# Utilize the QdrantClient() function to map out where our client will run. (Hint: You should've already created a docker-compose file to run that local host)
# Create a variable for the embedding dimension - pull the model from "embedding_services.py", that's where you already created your embedding model.
    # To ensure accuracy of dimension input - use the get_sentence_embedding_dimension() method.
# Create a collection for your client, this is where all the new data is going to be stored.
    # Ensure to create a name and fixed you vector parameters.