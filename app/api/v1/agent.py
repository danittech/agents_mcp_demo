# (c) Danit Consultancy and Development, January-2026, danittech@yahoo.com

""" Agent API endpoints """

import structlog
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from app.agents.graph import invoke_agent

logger = structlog.get_logger(__name__)
router = APIRouter()

# ----------------------------------------------------------------------------------------

class AgentRequest(BaseModel):
    query: str = Field(..., min_length=1)
    session_id: str | None = None

class AgentResponse(BaseModel):
    response: str
    message_count: int
    session_id: str | None = None

# ----------------------------------------------------------------------------------------

@router.post("/invoke", response_model=AgentResponse)
async def invoke_agent_endpoint(request: AgentRequest) -> AgentResponse:
    try:
        logger.info("agent_invoked", query=request.query)
        result = await invoke_agent(request.query, request.session_id)
        return AgentResponse(**result)
    except Exception as e:
        logger.error("agent_error", error=str(e))
        raise HTTPException(status_code=500, detail=str(e))

# ----------------------------------------------------------------------------------------

@router.get("/status")
async def agent_status():
    from app.core.config import settings
    from app.agents.tools import get_tools
    tools = get_tools()
    return {
        "status": "operational",
        "llm_provider": settings.LLM_PROVIDER,
        "tool_count": len(tools),
    }
