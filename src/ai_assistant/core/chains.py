from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_groq import ChatGroq

from ai_assistant.core.prompts import ROUTER_PROMPT
from ai_assistant.utils.helpers import get_chat_model



def get_router_chain():
    model = get_chat_model()
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", ROUTER_PROMPT),
            (MessagesPlaceholder(variable_name="messages"))
        ]
    )
    chain = prompt | model
    return chain