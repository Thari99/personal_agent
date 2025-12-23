from langgraph.graph import StateGraph
from agent.state import AgentState
from agent.nodes import (
    observe_task,
    think_task,
    decide_action,
    act_notify,
    remember

)

def build_agent():
    graph = StateGraph(AgentState)

    graph.add_node("observe",observe_task)
    graph.add_node("think",think_task)
    graph.add_node("act",act_notify)
    graph.add_node("remember",remember)

    graph.set_entry_point("observe")

    graph.add_edge("observe","think")

    graph.add_conditional_edges(
        "think",
        decide_action,
        {
            "act":"act",
            "observe":"observe"
        }
    )

    graph.add_edge("act","remember")
    graph.add_edge("remember","observe")

    return graph.compile()