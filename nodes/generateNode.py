from .state import State
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from .models import chat_model
from .SystemPrompt import get_system_prompt
from langchain_core.messages import HumanMessage, AIMessage

def generate(state: State) -> State:

    system_prompt = get_system_prompt()
    history = state.get("messages", [])
    answer_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "Question: {question}\n\n Context:\n{refined_context}"),
    ]
)
    response = (answer_prompt | chat_model).invoke(
        {
            "question": state["query"],
            "refined_context": state["refined_context"],
            "chat_history" : history,
        }
    )
    print("\n\nResponse : ",response.content)
    return {
        "response": response.content,
        "messages": [
            HumanMessage(content=state["query"]),
            AIMessage(content=response.content)
        ]
    }