from langchain_groq import ChatGroq
from ai_assistant.config import settings


def get_chat_model(temperature: float = 0.7):
    return ChatGroq(
            api_key=settings.GROQ_API_KEY,
            model=settings.GROQ_LLM_MODEL,
            temperature=temperature
    )

