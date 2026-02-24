from typing import TypedDict, List, Annotated
from langchain_core.documents import Document
from langgraph.graph.message import add_messages
from langchain_core.messages import BaseMessage

class State(TypedDict):
    query: str
    documents: List[Document]
    response: str
    refined_context: str
    good_docs:  List[Document]
    messages: Annotated[List[BaseMessage], add_messages]