# SteamMind RAG API

A FastAPI-based Retrieval-Augmented Generation (RAG) system using LangGraph, FAISS, and LLMs (Groq/Google).

## Project Structure

```text
FastAPI_SteamMind/
├── data/                      # Source documents (e.g., .docx)
├── nodes/                     # LangGraph processing nodes
│   ├── evalRetrivalNode.py    # Evaluates document relevance
│   ├── generateNode.py        # Generates final LLM response
│   ├── models.py              # LLM and Embedding model config
│   ├── reterivalNode.py       # FAISS search logic
│   ├── state.py               # Graph state definition
│   ├── SystemPrompt.py        # Prompts for the AI
│   └── vectorStore.py         # FAISS loading utilities
├── steaminds-vector-store/    # Local FAISS index files
├── main.py                    # FastAPI entry point
├── crag.py                    # LangGraph workflow definition
├── createVectorStore.py       # Script to build the vector store
├── pyproject.toml             # uv project configuration
└── .env                       # API keys (ignored by git)
```

## How to Run

Follow these steps to set up and run the project:

### 1. Install Dependencies
This project uses `uv` for fast package management.

```bash
# Install uv if you haven't already
pip install uv

# Sync and install project dependencies
uv sync
```

### 2. Configure Environment Variables
Create a `.env` file in the root directory and add your API keys:

```text
GROQ_API_KEY=your_groq_api_key_here
GOOGLE_API_KEY=your_google_api_key_here
```

### 3. (Optional) Create Vector Store
If the `steaminds-vector-store` folder is missing or you want to update it with new data from the `data/` folder:

```bash
uv run createVectorStore.py
```

### 4. Run the API
Start the FastAPI server:

```bash
uv run main.py
```

The API will be available at `http://localhost:8000`. You can test the response endpoint at `POST /get_response`.
