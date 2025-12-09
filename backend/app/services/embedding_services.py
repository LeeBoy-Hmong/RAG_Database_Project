from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2") # Dimension 384

def embed_text(text: str):
    return model.encode(text)

model2 = SentenceTransformer("multi-qa-MiniLM-L6-cos-v1")  # Dimension 384

def embed_text2(text: str):
    return model2.encode(text)

model3 = SentenceTransformer("all-MPNet-base-v2")  # Dimension 768

def embed_txt3(text: str):
    return model3.encode(text)