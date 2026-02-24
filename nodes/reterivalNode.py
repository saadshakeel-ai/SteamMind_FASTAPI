from .state import State
from .models import embedding_model
from .vectorStore import vector_store

def reterivalNode(state: State) -> State:
    q = state["query"]
    docs = vector_store.similarity_search(q, k=3)
    print(len(docs),"Documents Retrieved")
    return {"documents": docs}