# (c) Danit Consultancy and Development, January-2026, danittech@yahoo.com

"""LLM service."""
import structlog
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic

from app.core.config import settings

logger = structlog.get_logger(__name__)


def get_llm():
    if settings.LLM_PROVIDER == "openai":
        logger.info("initializing_openai", model=settings.DEFAULT_LLM_MODEL)
        return ChatOpenAI(
            api_key=settings.OPENAI_API_KEY,
            model=settings.DEFAULT_LLM_MODEL,
            temperature=settings.DEFAULT_TEMPERATURE,
        )
    elif settings.LLM_PROVIDER == "anthropic":
        logger.info("initializing_anthropic", model=settings.DEFAULT_LLM_MODEL)
        return ChatAnthropic(
            api_key=settings.ANTHROPIC_API_KEY,
            model=settings.DEFAULT_LLM_MODEL,
            temperature=settings.DEFAULT_TEMPERATURE,
        )
    else:
        raise ValueError(f"Unsupported LLM provider: {settings.LLM_PROVIDER}")
