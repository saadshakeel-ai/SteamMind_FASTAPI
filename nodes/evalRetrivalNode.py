from langchain_core.prompts import ChatPromptTemplate
from typing import List
from langchain_core.documents import Document
from pydantic import BaseModel
from .state import State
from .models import eval_model
# Score-Based Doc Eval
class DocEvalScore(BaseModel):
    score: float

LOWER_TH = 0.4
doc_eval_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a strict retrieval evaluator for RAG.\n"
            "You will be given ONE retrieved chunk and a question.\n"
            "Return a relevance score in [0.0, 1.0].\n"
            "- 1.0: chunk alone is sufficient to answer fully/mostly\n"
            "- 0.0: chunk is irrelevant\n"
            "Be conservative with high scores.\n"
            "Output JSON only.",
        ),
        ("human", "Question: {question}\n\nChunk:\n{chunk}"),
    ]
)

doc_eval_chain = doc_eval_prompt | eval_model.with_structured_output(DocEvalScore)

def eval_retrieval(state: State) -> State:
    question = state["query"]
    
    score : List[float] = []
    good : List[Document] =[]

    for doc in state["documents"]:
        doc_eval_chain_out = doc_eval_chain.invoke({
            "question" : question,
            "chunk" : doc.page_content
        })
        score.append(doc_eval_chain_out.score)

        if doc_eval_chain_out.score > LOWER_TH:
            good.append(doc)
    
    refined_context = "\n".join([doc.page_content for doc in good])
    print(len(good),"Good Documents")
    print("\n",refined_context)
    return {
        "good_docs" : good,
        "refined_context" : refined_context
    }