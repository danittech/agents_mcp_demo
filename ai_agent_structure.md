# AI Agent with FastAPI, LangGraph & MCP

## Project Structure

```
ai-agent-project/
├── .env.example
├── .gitignore
├── pyproject.toml
├── README.md
├── docker-compose.yml
├── Dockerfile
├── Makefile
├── app/
│   ├── __init__.py
│   ├── main.py                 # FastAPI application entry point
│   ├── api/
│   │   ├── __init__.py
│   │   ├── v1/
│   │   │   ├── __init__.py
│   │   │   ├── router.py       # Main API router
│   │   │   ├── agent.py        # Agent endpoints
│   │   │   └── health.py       # Health check endpoints
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py           # Configuration management
│   │   ├── logging.py          # Logging setup
│   │   └── dependencies.py     # Dependency injection
│   ├── services/
│   │   ├── __init__.py
│   │   ├── llm.py             # LLM service
│   │   └── mcp_client.py      # MCP client service
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── graph.py           # LangGraph agent definition
│   │   ├── state.py           # Agent state models
│   │   └── tools.py           # Custom tools
│   ├── mcp_servers/
│   │   ├── __init__.py
│   │   ├── math_server.py     # Example MCP server
│   │   └── weather_server.py  # Example MCP server
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── agent.py           # Agent request/response schemas
│   │   └── common.py          # Common schemas
│   └── utils/
│       ├── __init__.py
│       └── helpers.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_api/
│   └── test_agents/
└── docs/
    └── API.md
```

## Quick Start

### 1. Prerequisites
- Python 3.12+
- Docker & Docker Compose (optional)
- OpenAI API key or other LLM provider

### 2. Installation

```bash
# Clone the repository
git clone <your-repo>
cd ai-agent-project

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -e ".[dev]"

# Copy environment file
cp .env.example .env
# Edit .env with your API keys
```

### 3. Run the Application

```bash
# Development mode
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Or using Make
make dev

# Using Docker
docker-compose up --build
```

### 4. Access the API
- API Documentation: http://localhost:8000/docs
- Health Check: http://localhost:8000/health
- Agent Endpoint: http://localhost:8000/api/v1/agent/invoke

## Key Features

- ✅ FastAPI with async support
- ✅ LangGraph for stateful agent workflows
- ✅ MCP (Model Context Protocol) integration
- ✅ OpenAI/Anthropic LLM support
- ✅ Pydantic v2 for validation
- ✅ Structured logging
- ✅ Docker support
- ✅ Type hints throughout
- ✅ Comprehensive testing setup
- ✅ Development tools (ruff, mypy, pytest)

## Architecture

```
Client Request → FastAPI → LangGraph Agent → MCP Tools → External Services
                    ↓           ↓              ↓
                 Logging    State Mgmt    Tool Registry
```

## Next Steps

1. Configure your LLM provider in `.env`
2. Add custom tools in `app/agents/tools.py`
3. Create MCP servers in `app/mcp_servers/`
4. Customize the agent graph in `app/agents/graph.py`
5. Add your business logic
