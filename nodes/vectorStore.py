from langchain_community.vectorstores import FAISS
from .models import embedding_model

INDEX_NAME = "steaminds-vector-store"

vector_store = FAISS.load_local(
    folder_path=f"{INDEX_NAME}",
    embeddings=embedding_model,
    index_name="index",
    allow_dangerous_deserialization=True
)
