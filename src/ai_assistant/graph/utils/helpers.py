from langchain_groq import ChatGroq
from ai_assistant.config import settings
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from ai_assistant.modules.speech.text_to_speech import TextToSpeech

async def retrieve_docs(retriever, question):
    retrieved_docs = retriever.ainvoke(question)
    context = ''
    for d in retrieved_docs:
        context += "\n\n"
        context += d.page_content
    return context

def get_chat_model(temperature: float = 0.7):
    return ChatGroq(
            api_key=settings.GROQ_API_KEY,
            model=settings.GROQ_LLM_MODEL,
            temperature=temperature
    )

async def get_context(question_type, question):
    if question_type == 'General':
        file =  open(settings.RULES_SUMMARY_PATH, 'r') 
        context = file.read()
    elif question_type == 'Especifica':
        embedding_model = HuggingFaceEmbeddings(model=settings.RAG_TEXT_EMBEDDING_MODEL_ID)
        retriever = Chroma(
            embedding_function=embedding_model,
            persist_directory=settings.CHROMA_DB_PATH
        ).as_retriever(search_type='mmr', search_kwargs = {'k': 8})
        context = await retrieve_docs(retriever=retriever, question=question)

    else:
        context = ''

    return context


def get_text_to_speech():
    return TextToSpeech()



