# AI Agent with FastAPI, LangGraph & MCP

A modern, production-ready AI agent application built with Python 3.12, FastAPI, LangGraph, and Model Context Protocol (MCP).

## 🚀 Features

- **FastAPI** - High-performance async API framework
- **LangGraph** - Stateful, graph-based agent orchestration
- **MCP (Model Context Protocol)** - Standardized tool integration
- **Multi-LLM Support** - OpenAI and Anthropic (Claude)
- **Structured Logging** - JSON logging with structlog
- **Type Safety** - Full type hints with mypy
- **Docker Support** - Production-ready containerization

## 📋 Prerequisites

- Python 3.12+
- Docker & Docker Compose (optional)
- OpenAI API key or Anthropic API key

## 🛠️ Installation

```bash
# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -e ".[dev]"

# Copy environment file
cp .env.example .env
# Edit .env with your API keys
```

## 🎯 Quick Start

1. Configure your API key in `.env`
2. Run: `make dev` or `uvicorn app.main:app --reload`
3. Visit: http://localhost:8000/docs
4. Test the `/api/v1/agent/invoke` endpoint

## 📚 API Example

```bash
curl -X POST http://localhost:8000/api/v1/agent/invoke \
  -H "Content-Type: application/json" \
  -d '{"query": "What is 25 * 4?", "session_id": "test"}'
```

## 🔧 Development

```bash
make install      # Install dependencies
make dev          # Run development server
make test         # Run tests
make lint         # Run linting
make format       # Format code
```

## 🐳 Docker

```bash
docker-compose up --build
```

## 📝 License

MIT License
