.PHONY: help install dev test lint format clean

help:
	@echo "Available commands:"
	@echo "  make install - Install dependencies"
	@echo "  make dev     - Run development server"
	@echo "  make test    - Run tests"
	@echo "  make lint    - Run linting"
	@echo "  make format  - Format code"

install:
	pip install --upgrade pip
	pip install -e ".[dev]"

dev:
	uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

test:
	pytest -v --cov=app

lint:
	ruff check app tests
	mypy app

format:
	ruff format app tests

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
