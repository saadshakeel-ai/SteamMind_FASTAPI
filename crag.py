from dotenv import load_dotenv
load_dotenv()

from langgraph.graph import StateGraph, END, START
from nodes.reterivalNode import reterivalNode
from nodes.evalRetrivalNode import eval_retrieval
from nodes.generateNode import generate
from nodes.state import State
from langgraph.checkpoint.memory import MemorySaver

memory = MemorySaver()
graph = StateGraph(State)
graph.add_node("reterivalNode", reterivalNode)
graph.add_node("eval_each_doc", eval_retrieval)
graph.add_node("generate", generate)


graph.add_edge(START, "reterivalNode")
graph.add_edge("reterivalNode", "eval_each_doc")
graph.add_edge("eval_each_doc", "generate")
graph.add_edge("generate", END)

app = graph.compile(checkpointer=memory)

config = {"configurable": {"thread_id": "1"}}
# app

def generateResponse(user_input: str):
    response = app.invoke(
        {
            "query": user_input,
            "messages": [],
            "documents": [],
            "good_docs": [],
            "refined_context": "",
            "response": "",
        },
        config=config
    )
    return response["response"]

