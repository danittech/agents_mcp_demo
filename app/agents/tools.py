# (c) Danit Consultancy and Development, September-2023, danittech@yahoo.com

"""Custom tools for the agent."""
from typing import List
import structlog
from langchain_core.tools import tool

logger = structlog.get_logger(__name__)


@tool
def calculator(expression: str) -> str:
    """Evaluate a mathematical expression."""
    try:
        result = eval(expression, {"__builtins__": {}})
        logger.info("calculator_used", expression=expression, result=result)
        return str(result)
    except Exception as e:
        return f"Error: {str(e)}"


@tool
def get_current_time() -> str:
    """Get the current time in ISO format."""
    from datetime import datetime
    return datetime.now().isoformat()


def get_tools() -> List:
    return [calculator, get_current_time]
