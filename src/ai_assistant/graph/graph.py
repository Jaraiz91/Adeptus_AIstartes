from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver

from functools import lru_cache

from ai_assistant.graph.state import AdeptusAssistantState
from ai_assistant.graph.edges import select_workflow, should_summarize_conversation
from ai_assistant.graph.nodes import (
    summarize_conversation_node,
    audio_node,
    text_node,
    router_node
)


memory = MemorySaver()

@lru_cache(maxsize=1)
def create_graph():
    builder = StateGraph(AdeptusAssistantState)

    builder.add_node("text_node", text_node)
    builder.add_node("audio_node", audio_node)
    builder.add_node("router_node", router_node)
    builder.add_node("summarize_conversation_node", summarize_conversation_node)

    builder.add_edge(START, "router_node")
    builder.add_conditional_edges("router_node", select_workflow)

    builder.add_conditional_edges("audio_node", should_summarize_conversation)
    builder.add_conditional_edges("text_node", should_summarize_conversation)

    builder.add_edge("summarize_conversation_node", END)

    return builder

graph = create_graph().compile(checkpointer=memory)



