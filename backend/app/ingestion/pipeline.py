### Responsible for orchestration and workflow
### This file is where steps are chained together
### This is where we verify outputs between stages
# Embedding is a stage, not a primitive -- so it belogs here

from backend.app.ingestion.chunker import chunker
from backend.app.ingestion.loader import load_documents
from sentence_transformers import SentenceTransformer
from backend.app.database.init_qdrant import init_qdrant
from qdrant_client.models import PointStruct
from qdrant_client import QdrantClient
import uuid as u

def run_ingestion():
    documents = load_documents()
    chunks = chunker(documents)
# Embedding sanity check
    model = SentenceTransformer("all-MiniLM-L6-v2")
    chunks_txt = [c.page_content for c in chunks]
# Safety check: avoid chunks[0] crash & encoding of an empty list
    if not chunks_txt:
        raise ValueError("No chunks were produced. Check loader/chunker output.")
# Embed in batch
    embeddings = model.encode(chunks_txt)
# Building out the points
    qdrant = init_qdrant()
    collection_name = "rag_documents"
    
    points = []
    for i, (chunk, vector) in enumerate(zip(chunks, embeddings)):
        source = chunk.metadata.get("source", "unknown_source")
        raw_id = f"{source}::{i:06d}"
        chunk_id = str(u.uuid5(u.NAMESPACE_URL, raw_id))  # Made into a UUID - expected from Qdrant.

        points.append(
            PointStruct(
                id = chunk_id,
                vector = vector.tolist(),
                payload = {
                    "source": source,
                    "chunk index": i,
                    "text": chunk.page_content,
                },
            )
        )
# Call the Qdrant upsert
    qdrant.upsert(collection_name = collection_name, points = points)
    print(f"Upserted {len(points)} chunks into '{collection_name}'.")

# Retrieval sanity check
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

    print("\n")
    print(f"Chunks to embed: {len(chunks_txt)}")
    print(f"Embedding returned: {len(embeddings)}")
    print(f"Single embedding length (Dimension): {len(embeddings[0])}")
    print(f"First chunk preview", chunks_txt[0][:200])

    return chunks

if __name__ == "__main__":
    run_ingestion()