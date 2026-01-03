# (c) Danit Consultancy and Development, January-2026, danittech@yahoo.com
# Usage:  make test

"""Pytest configuration."""
import pytest
from httpx import AsyncClient
from app.main import app


@pytest.fixture
async def client():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac
