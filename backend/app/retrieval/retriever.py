
from backend.app.database.init_qdrant import init_qdrant
from backend.app.services.embedding_services import model as embedder
from qdrant_client.qdrant_client import QdrantClient, models
from typing import Sequence
from dotenv import load_dotenv
import os
import re

load_dotenv()
'''
test_query = "What is this document about?"
q_vector = model.encode(test_query).tolist()

hits = qdrant.query_points(
    collection_name = collection_name,
    query = q_vector,
    limit = 3
)

print("\nTop 3 hits")
for rank, hit in enumerate(hits, start = 1):
    # hit is a tuple in your environment
    # Try the common patterns:
    if hasattr(hit[0], "payload"):        # (point, score)
        point, score = hit[0], hit[1]
    elif hasattr(hit[1], "payload"):      # (score, point)
        score, point = hit[0], hit[1]
    else:
        # fallback: just print the tuple so you can see it
        print(f"{rank}) hit tuple = {hit}")
        continue

    payload = hit.payload or {}
    preview = payload.get("text", "")[:160].replace("\n", " ")
    print(f"{rank}) score={hit.score:.4f} source={payload.get('source')} chunk ={payload.get('chunk_index')}")
    print(f"    preview: {preview}\n")
'''
'''What are we attempting to do...
The system must turn input words into embeddings, compare them to the stored vector and find similarities. 
'''

## Text Normalization
# Trim spaces - collapse multiple spaces - remove weird invisible characters
# print("Start Script...") - run me to test program
# class Retrieval:
#    def __init__(self):
#        self.embedder = embedder  # Imported the model to ensure ownership inside the class.

def clean_input(question: str):
    rem_whitespace = question.strip()
    rem_metachar = re.sub(r'[^\w\s]', "", rem_whitespace) # Remove anything that's not a word or whitespace
    collapsed = " ".join(rem_metachar.split())  # transform back to regular spacing
    return collapsed

# Create a function method for an embed_query - need to turn the clean text into a vector (float)
def embed_query(clean_question: str) -> Sequence[float]:  # Changed from list[float] which is mutable & specific to Sequence[float] to allow flexibility
    return embedder.encode(clean_question)
        
# Create a function method for a search.
def search_query(question: Sequence[float]):
    clean = clean_input(question)
    vector_query = embed_query(clean)
    qdrant = os.getenv("LOCAL_QDRANT")
    hits = qdrant.query_points(
        collection_name = "rag_documents",
        query_vector = vector_query,
        limit = 3
    )
    return hits

# Create a function method for format hits.

# Create a function method for what's retrieved.

# if __name__ == "__main__":
#     cleaner = Retrieval()

