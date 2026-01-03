# (c) Danit Consultancy and Development, September-2023, danittech@yahoo.com

"""LangGraph agent definition."""
import structlog
from langchain_core.messages import HumanMessage, AIMessage
from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode

from app.agents.state import AgentState
from app.agents.tools import get_tools
from app.services.llm import get_llm

logger = structlog.get_logger(__name__)


def create_agent_graph():
    llm = get_llm()
    tools = get_tools()
    llm_with_tools = llm.bind_tools(tools)
    
    workflow = StateGraph(AgentState)
    
    async def call_model(state: AgentState) -> dict:
        logger.info("calling_model")
        response = await llm_with_tools.ainvoke(state["messages"])
        return {"messages": [response]}
    
    workflow.add_node("agent", call_model)
    workflow.add_node("tools", ToolNode(tools))
    workflow.add_edge(START, "agent")
    
    def should_continue(state: AgentState) -> str:
        last_message = state["messages"][-1]
        if hasattr(last_message, "tool_calls") and last_message.tool_calls:
            return "tools"
        return END
    
    workflow.add_conditional_edges("agent", should_continue, ["tools", END])
    workflow.add_edge("tools", "agent")
    
    return workflow.compile()


_agent = None


def get_agent():
    global _agent
    if _agent is None:
        _agent = create_agent_graph()
    return _agent


async def invoke_agent(query: str, session_id: str | None = None) -> dict:
    logger.info("invoking_agent", query=query)
    agent = get_agent()
    
    initial_state = {"messages": [HumanMessage(content=query)]}
    result = await agent.ainvoke(initial_state)
    
    final_message = result["messages"][-1]
    response = {
        "response": final_message.content if isinstance(final_message, AIMessage) else str(final_message),
        "message_count": len(result["messages"]),
        "session_id": session_id,
    }
    
    return response
