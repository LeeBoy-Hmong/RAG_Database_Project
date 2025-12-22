### Get raw documents
### Knows nothing about embeddings
### Should never import models

from langchain_community.document_loaders import TextLoader, DirectoryLoader
import os
'''Load all text files from the docs file path'''
def load_documents(dir_path="backend/app/ingestion/docs"):  # 
    print(f"Documents are loading from {dir_path}...")
# Check if documents in the particular directory exist
    if not os.path.exists(dir_path):
        raise FileNotFoundError(f"The directory {dir_path} could not be found. Please ensure the file exist.")
# Load all .txt files from the document directory
    doc_loader = DirectoryLoader(
        path = dir_path,
        glob = "*.txt",
        loader_cls = TextLoader,
        loader_kwargs={
            "encoding": "UTF-8",  # Needs to be passed in - Windows Python is not utilizing the correct encoder. 
        },
    )

    documents = doc_loader.load()
# Raise error is the document (.txt files) do not exist
    if len(documents) == 0:
        raise FileNotFoundError(f"Can not find the particular file(s) you are looking for. Please ensure files exist.")
    
    for i, doc in enumerate(documents[:2]):
        print(f"\nDocument {i+1}:")
        print(f"Source: {doc.metadata['source']}")
        print(f"Content length: {len(doc.page_content)}")
        print(f"Content Preview: {doc.page_content[:100]}")
        print(f"Metadata: {doc.metadata}")
    
    return documents

if __name__ == "__main__":
    load_documents()
