from langgraph.graph import END
from typing_extensions import Literal
from ai_assistant.graph.state import AdeptusAssistantState
from ai_assistant.config import settings



def should_summarize_conversation(state: AdeptusAssistantState) -> Literal["summarize_conversation_node", "__end__"]:
    messages = state['messages']

    if len(messages) > settings.TOTAL_MESSAGES_SUMMARY_TRIGGER:
        return "summarize_conversation_node"
    else:
        return END
    
    
def select_workflow(state: AdeptusAssistantState) -> Literal['conversation_node', 'audio_node']:
    workflow = state['workflow']

    if workflow == 'audio':
        return 'audio_node'
    else:
        return 'conversation_node'
    
