"""Agent tests"""

import pytest
from src.agents.developer_agent import DeveloperAgent
from src.agents.tester_agent import TesterAgent


@pytest.mark.asyncio
async def test_developer_agent_execution():
    """Test developer agent execution"""
    agent = DeveloperAgent("dev-1", "Developer")
    
    task = {
        "id": "task-1",
        "type": "feature",
        "description": "Implement user authentication",
    }
    
    result = await agent.execute_task(task)
    
    assert result["success"] is True
    assert "code" in result
    assert agent.total_tasks_completed == 1


@pytest.mark.asyncio
async def test_tester_agent_execution():
    """Test tester agent execution"""
    agent = TesterAgent("tester-1", "Tester")
    
    task = {
        "id": "task-2",
        "type": "unit_testing",
        "code": "def add(a, b): return a + b",
    }
    
    result = await agent.execute_task(task)
    
    assert result["success"] is True
    assert "tests" in result
    assert agent.total_tasks_completed == 1


@pytest.mark.asyncio
async def test_agent_status():
    """Test agent status"""
    agent = DeveloperAgent("dev-2", "Developer")
    
    status = agent.get_status()
    
    assert status["agent_id"] == "dev-2"
    assert status["name"] == "Developer"
    assert status["type"] == "developer"
    assert status["status"] == "idle"
