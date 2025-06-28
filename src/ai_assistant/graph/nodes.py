
from langchain_core.messages import AIMessage, HumanMessage, RemoveMessage
from langchain_core.runnables import RunnableConfig


from ai_assistant.graph.state import AdeptusAssistantState
from ai_assistant.graph.utils.chains import get_router_chain, get_conversation_chain
from ai_assistant.graph.utils.helpers import get_context , get_summary_model, get_text_to_speech
from ai_assistant.config import settings

async def router_node(state: AdeptusAssistantState):
    router_chain = get_router_chain()
    response = await router_chain.ainvoke(messages= state['messages'])
    return {'workflow': response.workflow, 'tipo_pregunta': response.tipo_pregunta, 'pregunta': response.pregunta}


async def text_node(state: AdeptusAssistantState, config: RunnableConfig):
    conversation_chain = get_conversation_chain(summary=state['summary'])
    context = await get_context(question_type=state['tipo_pregunta'],question=state['pregunta'])
    response = conversation_chain.ainvoke({
        "messages": state['messages'],
        "contexto": context
    },
    config=config
    )
    return {"messages": AIMessage(content=response)}


async def summarize_conversation_node(state: AdeptusAssistantState):
    model = get_summary_model()
    summary = state.get("summary", "")

    if summay:
        summary_message = (
            f"Este es el resumen de la conversación hasta ahora con el usuario: {summary}\n\n"
            "Extiende el resumen teniendo en cuenta los nuevos mensajes de arriba:"
        )
    else:
        summary_message = (
            "Crea un resumen de la conversación con el usuario."
            "El resumen debe ser una descripción corta de la conversación hasta ahora,"
            "sin embargo debe contener toda la información relevante."
        )
    
    messages = state['messages'] + [HumanMessage(content=summary_message)]
    response = await model.ainvoke(messages)

    delete_messages = [RemoveMessage(id=m.id) for m in state['messages'][:-settings.TOTAL_MESSAGES_AFTER_SUMMARY]]

    return {'summary': response.content, 'messages': delete_messages}


async def audio_node(state: AdeptusAssistantState, config: RunnableConfig):
    conversation_chain = get_conversation_chain(summary=state['summary'])
    context = await get_context(question_type=state['tipo_pregunta'],question=state['pregunta'])
    text_to_speech_module = get_text_to_speech()

    response = await chain.aivoke(
        {
            'messages': state['messages'],
            'context': context
        },
        config
    )
    output_audio = await text_to_speech_module.synthesize(response)

    return {'messages': response, 'audio_buffer': output_audio}