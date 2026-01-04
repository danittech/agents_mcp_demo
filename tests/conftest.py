# (c) Danit Consultancy and Development, January-2026, danittech@yahoo.com
# Usage:  make test

""" Pytest configuration """

import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app

# ----------------------------------------------------------------------------------------

@pytest.fixture
async def client():
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test"
    ) as ac:
        yield ac
