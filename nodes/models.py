from langchain_groq import ChatGroq
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()
chat_model = ChatGroq(model="openai/gpt-oss-120b")
eval_model = ChatGroq(model="llama-3.3-70b-versatile")
embedding_model = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")