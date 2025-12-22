### Responsible for orchestration and workflow
### This file is where steps are chained together
### This is where we verify outputs between stages
# Embedding is a stage, not a primitive -- so it belogs here

from chunker import chunker
from loader import load_documents
from sentence_transformers import SentenceTransformer

def run_ingestion():
    documents = load_documents()
    chunks = chunker(documents)
# Embedding sanity check
    model = SentenceTransformer("all-MiniLM-L6-v2")
    chunks_txt = [c.page_content for c in chunks]
# Safety check: avoid chunks[0] crash & encoding of an empty list
    if not chunks_txt:
        raise ValueError("No chunks wer produced. Check loader/chunker output.")
# Embed in batch
    embeddings = model.encode(chunks_txt)

    print(f"Chunks to embed: {len(chunks_txt)}")
    print(f"Embedding returned: {len(embeddings)}")
    print(f"Single embedding length: {len(embeddings[0])}")
    print(f"First chunk preview", chunks_txt[0][:200])

    return chunks

if __name__ == "__main__":
    run_ingestion()