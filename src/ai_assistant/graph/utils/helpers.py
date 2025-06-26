from langchain_groq import ChatGroq
from ai_assistant.config import settings
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings



def get_chat_model(temperature: float = 0.7):
    return ChatGroq(
            api_key=settings.GROQ_API_KEY,
            model=settings.GROQ_LLM_MODEL,
            temperature=temperature
    )

def get_context(question_type):
    if question_type == 'General':
        file =  open(settings.RULES_SUMMARY_PATH, 'r') 
        context = file.read()
    elif question_type == 'Especifica':
        context = 'hola'


