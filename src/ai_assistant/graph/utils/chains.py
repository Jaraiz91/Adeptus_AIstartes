from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from pydantic import BaseModel, Field
from typing import Literal
from langchain_groq import ChatGroq

from ai_assistant.core.prompts import ROUTER_PROMPT, CONVERSATION_PROMPT
from ai_assistant.graph.utils.helpers import get_chat_model

class router_atrtibutes(BaseModel):
    tipo_pregunta : Literal['General', 'Especifica'] = Field(description="Indica si la pregunta es de caracter general si pregunta un resumen sobre las reglas de warhammer 40k o específica si es una pregunta concreta")
    workflow: Literal['audio', 'texto'] = Field(description="Indica si debe responder en texto o en audio")
    pregunta: str = Field(description="pregunta del usuario")


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


def get_conversation_chain(summary: str = ""):
    model = get_chat_model()
    system_message = CONVERSATION_PROMPT

    if summary:
        system_message += f"\n\nAquí está el resumen de la conversación que has mantenido con el usuario: {summary}"

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_message),
            MessagesPlaceholder(variable_name="messages")
        ]
    )
    
    return prompt | model
