
from langchain_core.messages import AIMessage, HumanMessage, RemoveMessage
from langchain_core.runnables import RunnableConfig


from ai_assistant.graph.state import AdeptusAssistantState
from ai_assistant.graph.utils.chains import get_router_chain, get_conversation_chain
from ai_assistant.graph.utils.helpers import get_context 


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