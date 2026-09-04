"""Governance tests"""

import pytest
from datetime import datetime, timedelta
from src.token_system.governance import GovernanceEngine


def test_create_proposal():
    """Test proposal creation"""
    governance = GovernanceEngine()
    
    proposal = governance.create_proposal(
        title="Increase Agent Rewards",
        description="Proposal to increase base reward amount",
        creator_id="agent-1",
    )
    
    assert proposal["title"] == "Increase Agent Rewards"
    assert proposal["status"] == "active"
    assert proposal["votes_for"] == 0.0


def test_cast_vote():
    """Test vote casting"""
    governance = GovernanceEngine()
    
    proposal = governance.create_proposal(
        title="Test Proposal",
        description="Test",
        creator_id="agent-1",
    )
    
    vote = governance.cast_vote(
        proposal_id=proposal["id"],
        voter_id="agent-2",
        voting_power=1000.0,
        choice="for",
    )
    
    assert vote["choice"] == "for"
    assert vote["voting_power"] == 1000.0


def test_finalize_proposal_passed():
    """Test proposal finalization - passed"""
    governance = GovernanceEngine()
    
    proposal = governance.create_proposal(
        title="Test Proposal",
        description="Test",
        creator_id="agent-1",
    )
    
    # Simulate votes
    proposal["votes_for"] = 60.0
    proposal["votes_against"] = 40.0
    proposal["total_votes"] = 100.0
    
    finalized = governance.finalize_proposal(proposal)
    
    assert finalized["status"] == "passed"
    assert finalized["approval_percentage"] == 60.0


def test_finalize_proposal_rejected():
    """Test proposal finalization - rejected"""
    governance = GovernanceEngine()
    
    proposal = governance.create_proposal(
        title="Test Proposal",
        description="Test",
        creator_id="agent-1",
    )
    
    # Simulate votes
    proposal["votes_for"] = 30.0
    proposal["votes_against"] = 70.0
    proposal["total_votes"] = 100.0
    
    finalized = governance.finalize_proposal(proposal)
    
    assert finalized["status"] == "rejected"
