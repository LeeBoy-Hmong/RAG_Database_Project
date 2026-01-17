### Responsible for splitting documents
### Should stay dumb and resusable
### No ML models should be here

from langchain_text_splitters import RecursiveCharacterTextSplitter
# Recursive chunking - preserves structures and starts with paragraph. Drops to sentences chunking.
# Semantic coherence is kept, although some coherence may be lost.
def chunker(documents):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 500,
        chunk_overlap = 100,
        )
    chunked_docs = text_splitter.split_documents(documents)
    return chunked_docs

# Create a function with the recursivecharactertextsplitter.
# Create a variable to assigning to the module function.
# Utilize the chunk_size and the chunk_overlap parameters.
# initialize the run with another variable, attache the split_document() method to it.
