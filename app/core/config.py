# (c) Danit Consultancy and Development, January-2026, danittech@yahoo.com

""" Application configuration """

from typing import List
from pydantic_settings import BaseSettings, SettingsConfigDict

# ----------------------------------------------------------------------------------------

class Settings(BaseSettings):

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
        extra="ignore",  # Allow extra fields in .env without errors
    )

    # Application
    PROJECT_NAME: str = "AI Agent API"
    ENVIRONMENT: str = "development"
    DEBUG: bool = True

    # API
    ALLOWED_ORIGINS: List[str] = ["http://localhost:3000", "http://localhost:8000"]

    # LLM Configuration
    LLM_PROVIDER: str = "openai"
    OPENAI_API_KEY: str = ""
    ANTHROPIC_API_KEY: str = ""
    DEFAULT_LLM_MODEL: str = "gpt-4o"
    DEFAULT_TEMPERATURE: float = 0.7
    MAX_TOKENS: int = 4096

    # Database (optional)
    DATABASE_URL: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/ai_agent"

    # Logging
    LOG_LEVEL: str = "INFO"
    LOG_FORMAT: str = "console"

    # Observability (optional)
    LANGSMITH_API_KEY: str = ""
    LANGSMITH_PROJECT: str = "ai-agent-project"
    ENABLE_TRACING: bool = False

# ----------------------------------------------------------------------------------------

settings = Settings()
