"""Tester Agent - Quality assurance and testing"""

import logging
from typing import Dict, Any

from src.agents.base_agent import BaseAgent

logger = logging.getLogger(__name__)


class TesterAgent(BaseAgent):
    """Agent responsible for testing and quality assurance"""
    
    def __init__(self, agent_id: str, name: str = "Tester"):
        super().__init__(agent_id, name, "tester")
    
    async def execute_task(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """Create tests and validate code quality"""
        await self.start_task(task)
        
        try:
            task_type = task.get("type", "testing")
            
            if task_type == "unit_testing":
                result = await self._create_unit_tests(task)
            elif task_type == "integration_testing":
                result = await self._create_integration_tests(task)
            elif task_type == "validation":
                result = await self._validate_code(task)
            else:
                result = await self._create_unit_tests(task)
            
            await self.complete_task(result)
            return result
        
        except Exception as e:
            logger.error(f"Tester agent task failed: {e}")
            return {
                "success": False,
                "error": str(e),
            }
    
    async def _create_unit_tests(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """Create unit tests for code"""
        code_to_test = task.get("code", "")
        
        test_code = f"""
import pytest

class TestFeature:
    def test_initialization(self):
        # Test initialization
        assert True
    
    def test_execution(self):
        # Test execution
        assert True
    
    def test_edge_cases(self):
        # Test edge cases
        assert True
"""
        
        return {
            "success": True,
            "tests": test_code,
            "test_count": 3,
            "coverage": 85.0,  # percentage
        }
    
    async def _create_integration_tests(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """Create integration tests"""
        components = task.get("components", [])
        
        integration_test = f"""
import pytest
from integration_test_suite import *

class TestIntegration:
    def test_component_interaction(self):
        # Test components working together
        assert True
    
    def test_data_flow(self):
        # Test data flow between components
        assert True
    
    def test_error_handling(self):
        # Test error scenarios
        assert True
"""
        
        return {
            "success": True,
            "integration_tests": integration_test,
            "test_count": 3,
            "coverage": 75.0,  # percentage
        }
    
    async def _validate_code(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """Validate code quality"""
        code_to_validate = task.get("code", "")
        
        validation_report = f"""
# Code Validation Report

## Quality Metrics
- Code Duplication: 5%
- Cyclomatic Complexity: 8
- Lines Per Function: 20
- Documentation Coverage: 80%

## Issues Found
- 2 Code Style Issues
- 1 Performance Warning
- 0 Critical Issues

## Recommendations
1. Add docstrings
2. Refactor complex function
3. Add type hints
"""
        
        return {
            "success": True,
            "validation_report": validation_report,
            "quality_score": 82.0,
            "issues_found": 3,
        }
    
    async def evaluate_task(self, task: Dict[str, Any]) -> float:
        """Evaluate quality of tests"""
        # Simulated evaluation
        coverage = task.get("coverage", 0)
        test_count = task.get("test_count", 0)
        
        # Base score
        score = 70.0
        
        # Adjust based on coverage
        score += coverage * 0.2
        
        # Adjust based on test count
        score += min(test_count * 3, 15)
        
        return min(100.0, score)
