"""Task scheduler tests"""

import pytest
from src.task_system.scheduler import TaskScheduler


@pytest.mark.asyncio
async def test_enqueue_task():
    """Test task enqueueing"""
    scheduler = TaskScheduler()
    
    task = await scheduler.enqueue_task(
        task_id="task-1",
        task_type="feature",
        description="Implement feature",
        priority=8,
        base_reward=150.0,
    )
    
    assert task["id"] == "task-1"
    assert task["status"] == "pending"
    assert len(scheduler.task_queue) == 1


@pytest.mark.asyncio
async def test_task_priority_ordering():
    """Test task priority ordering"""
    scheduler = TaskScheduler()
    
    await scheduler.enqueue_task("task-1", "feature", "Low priority", priority=1)
    await scheduler.enqueue_task("task-2", "feature", "High priority", priority=10)
    await scheduler.enqueue_task("task-3", "feature", "Medium priority", priority=5)
    
    # Highest priority should be first
    assert scheduler.task_queue[0]["id"] == "task-2"
    assert scheduler.task_queue[1]["id"] == "task-3"
    assert scheduler.task_queue[2]["id"] == "task-1"


@pytest.mark.asyncio
async def test_assign_task():
    """Test task assignment"""
    scheduler = TaskScheduler()
    
    task = await scheduler.enqueue_task(
        "task-1",
        "feature",
        "Implement feature",
    )
    
    assigned = await scheduler.assign_task("task-1", "agent-1")
    
    assert assigned["assigned_agent_id"] == "agent-1"
    assert assigned["status"] == "assigned"
    assert "task-1" in scheduler.active_tasks


@pytest.mark.asyncio
async def test_complete_task():
    """Test task completion"""
    scheduler = TaskScheduler()
    
    task = await scheduler.enqueue_task(
        "task-1",
        "feature",
        "Implement feature",
    )
    
    await scheduler.assign_task("task-1", "agent-1")
    
    result = {"success": True, "code": "..."}
    completed = await scheduler.complete_task("task-1", result, quality_score=85.0)
    
    assert completed["status"] == "completed"
    assert completed["quality_score"] == 85.0
    assert "task-1" in [t["id"] for t in scheduler.completed_tasks]


@pytest.mark.asyncio
async def test_queue_status():
    """Test queue status"""
    scheduler = TaskScheduler()
    
    await scheduler.enqueue_task("task-1", "feature", "Task 1")
    await scheduler.enqueue_task("task-2", "feature", "Task 2")
    
    status = scheduler.get_queue_status()
    
    assert status["pending_tasks"] == 2
    assert status["active_tasks"] == 0
    assert status["total_tasks"] == 2
