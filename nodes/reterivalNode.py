from .state import State
from .vectorStore import vector_store

def reterivalNode(state: State) -> State:
    q = state["query"]
    docs = vector_store.similarity_search(q, k=3)
    refined_context = "\n".join([doc.page_content for doc in docs])
    # print("Documents Retrieved: ", docs)
    print(len(docs),"Documents Retrieved")
    return {"refined_context": refined_context}