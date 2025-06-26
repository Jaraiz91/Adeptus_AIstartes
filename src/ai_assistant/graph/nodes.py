
from ai_assistant.graph.state import AdeptusAssistantState
from ai_assistant.graph.utils.chains import get_router_chain



def router_node(state: AdeptusAssistantState):
    router_chain = get_router_chain()
    response = router_chain.ainvoke(messages= state['messages'])
    return {'workflow': response.workflow, 'tipo_pregunta': response.tipo_pregunta}


def answer_node(state: AdeptusAssistantState):
