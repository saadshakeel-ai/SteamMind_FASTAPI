from .state import State
from .models import chat_model
from langchain_core.prompts import ChatPromptTemplate

def transformQuery(state: State):
    query = state["query"]
    messages = state.get("messages", [])
    # print("Messages: ", messages)
    if not messages:
        return {
            "query" : query
        }
    
    system_prompt = """You are an AI assistant tasked with re-writing user questions to be standalone and optimized for vector database search.
GUIDELINES:
1. Use the chat history to resolve pronouns (e.g., "he", "it", "they") and references (e.g., "that", "the previous one").
2. Ensure the resulting question contains the specific subject or entity being discussed (e.g., replace "him" with "John Doe").
3. DO NOT answer the question. Only re-write it.
4. If the question is already standalone and clear, return it exactly as it is without any changes.
5. Preserve technical terms and specific names (like 'SteamMinds') exactly.
OUTPUT:
Return ONLY the re-written question text and nothing else."""

    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("placeholder", "{chat_history}"),
        ("human", "Question: {question}")
    ])

    chain = prompt | chat_model
    response = chain.invoke({
        "chat_history" : messages,
        "question" : query
    })
    # print("Response: ", response, "\n\n")
    print(f"Original: {query}\n")
    print(f"Transformed: {response.content}\n")
    return {
        "query" : response.content
    }

        