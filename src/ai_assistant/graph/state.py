from langgraph.graph import MessagesState


class AdeptusAssistantState(MessagesState):
    """State class for the WH40k rules assistant workflow.
    
    Extends MessageState to track conversation history and maintains the last message received.
    
    Attributes:
        workflow (str) : The current workflow the assistant is in. Can be "conversation" or "audio".
        audio_buffer (bytes): The audio buffer to be used for speech-to-text conversion.
        summary (str): The summary of the conversation"""
    
    workflow: str
    audio_buffer: bytes
    summary: str