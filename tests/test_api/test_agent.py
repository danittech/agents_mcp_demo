"""Agent API tests."""
import pytest


@pytest.mark.asyncio
async def test_agent_invoke(client):
    response = await client.post(
        "/api/v1/agent/invoke",
        json={"query": "What is 2+2?"}
    )
    assert response.status_code == 200
    data = response.json()
    assert "response" in data
    assert "message_count" in data


@pytest.mark.asyncio
async def test_agent_status(client):
    response = await client.get("/api/v1/agent/status")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "operational"
