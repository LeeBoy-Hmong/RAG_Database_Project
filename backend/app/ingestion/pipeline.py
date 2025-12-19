from chunker import chunker
from loader import load_documents

documents = load_documents()
chunks = chunker(documents)

print(chunks[0].page_content[:200])