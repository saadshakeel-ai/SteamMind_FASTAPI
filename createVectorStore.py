from langchain_community.vectorstores import FAISS
from langchain_text_splitters import  RecursiveCharacterTextSplitter
from langchain_community.document_loaders import Docx2txtLoader
from langchain_core.documents import Document
from nodes.models import embedding_model
import os

INDEX_NAME = "steaminds-vector-store"

loader = Docx2txtLoader("data/Final CHATBOT data requirements.docx")
docs = loader.load()

splitter = RecursiveCharacterTextSplitter(
    separators=[
        r"\n\d+\.\s",
        "\n\n",
        "\n",
        " ",
        ""
    ],
    is_separator_regex=True,
    chunk_size=1000,        
    chunk_overlap=150,
    keep_separator="start",
    strip_whitespace=True
)
chunks = splitter.split_documents(docs)
print(f"Number of chunks: {len(chunks)}")

vector_store = FAISS.from_documents(
    chunks, embedding_model
)

vector_store.save_local(INDEX_NAME)
print(f"Vector store saved to: {os.path.abspath(INDEX_NAME)}")
