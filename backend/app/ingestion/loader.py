from langchain_community.document_loaders import TextLoader, DirectoryLoader
import os
from dotenv import load_dotenv

load_dotenv()

'''Load all text files from the docs file path'''
def load_documents(dir_path="docs"):
    print(f"Documents are loading from {dir_path}...")
# Check if documents in the particular directory exist
    if not os.path.exists(dir_path):
        raise FileNotFoundError(f"The directory {dir_path} could not be found. Please ensure the file exist.")
# Load all .txt files from the document directory
    doc_loader = DirectoryLoader(
        path = dir_path,
        glob = "*.txt",
        loader_cls = TextLoader
    )

    documents = doc_loader.load()
# Raise error is the document (.txt files) do not exist
    if len(documents) == 0:
        raise FileNotFoundError(f"Can not find the particular file(s) you are looking for. Please ensure files exist.")
    
    return documents

if __name__ == "__main__":
    load_documents()
