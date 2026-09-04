"""Governance engine"""

import logging
from typing import Dict, Any, List, Optional
from datetime import datetime, timedelta
from enum import Enum

from src.config import settings

logger = logging.getLogger(__name__)


class GovernanceEngine:
    """Engine for governance and voting"""
    
    def __init__(self):
        self.voting_period_days = settings.GOVERNANCE_VOTING_PERIOD_DAYS
        self.min_quorum = settings.GOVERNANCE_MIN_QUORUM
        self.approval_threshold = settings.GOVERNANCE_APPROVAL_THRESHOLD
    
    def create_proposal(
        self,
        title: str,
        description: str,
        creator_id: str,
        voting_period_days: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Create a governance proposal"""
        if voting_period_days is None:
            voting_period_days = self.voting_period_days
        
        now = datetime.utcnow()
        voting_ends_at = now + timedelta(days=voting_period_days)
        
        proposal = {
            "id": f"proposal-{int(now.timestamp() * 1000)}",
            "title": title,
            "description": description,
            "creator_id": creator_id,
            "status": "active",
            "votes_for": 0.0,
            "votes_against": 0.0,
            "votes_abstain": 0.0,
            "total_votes": 0.0,
            "voting_starts_at": now.isoformat(),
            "voting_ends_at": voting_ends_at.isoformat(),
            "created_at": now.isoformat(),
        }
        
        logger.info(f"Proposal created: {proposal['id']}")
        return proposal
    
    def cast_vote(
        self,
        proposal_id: str,
        voter_id: str,
        voting_power: float,
        choice: str,  # "for", "against", "abstain"
    ) -> Dict[str, Any]:
        """Cast a vote on a proposal"""
        if choice not in ["for", "against", "abstain"]:
            raise ValueError("Invalid vote choice")
        
        vote = {
            "id": f"vote-{int(datetime.utcnow().timestamp() * 1000)}",
            "proposal_id": proposal_id,
            "voter_id": voter_id,
            "choice": choice,
            "voting_power": voting_power,
            "created_at": datetime.utcnow().isoformat(),
        }
        
        logger.info(f"Vote cast: {vote['id']} - {choice}")
        return vote
    
    def finalize_proposal(
        self,
        proposal: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Finalize voting on a proposal"""
        total_votes = proposal.get("total_votes", 0)
        votes_for = proposal.get("votes_for", 0)
        votes_against = proposal.get("votes_against", 0)
        
        # Check quorum
        quorum_met = (total_votes / 100) >= self.min_quorum  # Assuming 100 total stakeholders
        
        # Calculate approval percentage
        if total_votes > 0:
            approval_percentage = (votes_for / total_votes) * 100
        else:
            approval_percentage = 0
        
        # Determine outcome
        if not quorum_met:
            status = "rejected"
            reason = "Quorum not met"
        elif approval_percentage >= self.approval_threshold:
            status = "passed"
            reason = f"Approved with {approval_percentage:.1f}% votes"
        else:
            status = "rejected"
            reason = f"Failed with {approval_percentage:.1f}% votes"
        
        proposal["status"] = status
        proposal["executed"] = False
        proposal["finalized_at"] = datetime.utcnow().isoformat()
        proposal["finalization_reason"] = reason
        proposal["approval_percentage"] = approval_percentage
        
        logger.info(f"Proposal {proposal['id']} finalized: {status}")
        return proposal
    
    def execute_proposal(
        self,
        proposal: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Execute a passed proposal"""
        if proposal.get("status") != "passed":
            raise ValueError("Can only execute passed proposals")
        
        # Simulated execution
        proposal["executed"] = True
        proposal["executed_at"] = datetime.utcnow().isoformat()
        proposal["execution_result"] = "success"
        
        logger.info(f"Proposal {proposal['id']} executed")
        return proposal
    
    def get_proposal_status(
        self,
        proposal: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Get current proposal status"""
        voting_ends_at = datetime.fromisoformat(proposal["voting_ends_at"])
        now = datetime.utcnow()
        
        if now > voting_ends_at:
            voting_status = "closed"
        else:
            time_remaining = voting_ends_at - now
            voting_status = f"active - {time_remaining.days}d remaining"
        
        return {
            "proposal_id": proposal["id"],
            "status": proposal["status"],
            "voting_status": voting_status,
            "votes_for": proposal["votes_for"],
            "votes_against": proposal["votes_against"],
            "votes_abstain": proposal["votes_abstain"],
            "total_votes": proposal["total_votes"],
        }
