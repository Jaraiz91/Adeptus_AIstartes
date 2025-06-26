
from ai_assistant.graph.state import AdeptusAssistantState
from ai_assistant.core.chains import get_router_chain



def router(state: AdeptusAssistantState):
    router_chain = get_router_chain()
    response = router_chain.ainvoke(messages= state['messages'])
    return {'workflow': response.workflow, 'tipo_pregunta': response.tipo_pregunta}

