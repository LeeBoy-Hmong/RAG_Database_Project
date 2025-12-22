### Responsible for orchestration and workflow
### This file is where steps are chained together
### This is where we verify outputs between stages
# Embedding is a stage, not a primitive -- so it belogs here

from chunker import chunker
from loader import load_documents

def run_ingestion():
    documents = load_documents()
    chunks = chunker(documents)

    print(f"Loaded Documents: {len(documents)}")
    print(f"Loaded Chunks: {len(chunks)}")
    print(f"Sample Chunk Preview", chunks[0].page_content[:200])

    return chunks

if __name__ == "__main__":
    run_ingestion()