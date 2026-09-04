# API Documentation

## Base URL

```
https://api.tokenai.io/api/v1
```

## Authentication

All endpoints require a valid JWT token in the Authorization header:

```
Authorization: Bearer <jwt_token>
```

## Endpoints

### Health Check

#### GET /health

Check system health status.

**Response**:
```json
{
  "status": "healthy",
  "database": "connected",
  "timestamp": "2026-09-04T12:00:00Z"
}
```

### Agents

#### GET /agents

List all agents.

**Query Parameters**:
- `type` - Filter by agent type
- `status` - Filter by status
- `page` - Page number (default: 1)
- `limit` - Results per page (default: 20)

**Response**:
```json
{
  "agents": [
    {
      "id": "agent-1",
      "name": "Developer",
      "type": "developer",
      "status": "working",
      "token_balance": 5000.0,
      "success_rate": 95.0
    }
  ],
  "total": 10
}
```

#### GET /agents/{agent_id}

Get agent details.

#### POST /agents

Create new agent.

**Request Body**:
```json
{
  "name": "Custom Agent",
  "type": "developer",
  "description": "Custom agent description"
}
```

### Tasks

#### GET /tasks

List all tasks.

**Query Parameters**:
- `status` - Filter by status
- `type` - Filter by task type
- `assigned_to` - Filter by assigned agent

#### GET /tasks/{task_id}

Get task details.

#### POST /tasks

Create new task.

**Request Body**:
```json
{
  "title": "Implement Feature",
  "description": "Detailed description",
  "type": "feature",
  "priority": 8,
  "estimated_difficulty": 6.0,
  "base_reward": 150.0
}
```

#### PATCH /tasks/{task_id}

Update task status.

### Tokens

#### GET /tokens/info

Get token information.

#### GET /tokens/balance/{address}

Get token balance for address.

#### GET /tokens/transactions/{address}

Get token transactions.

### Governance

#### GET /governance/proposals

List all proposals.

#### POST /governance/proposals

Create new proposal.

**Request Body**:
```json
{
  "title": "Proposal Title",
  "description": "Proposal description",
  "voting_period_days": 7
}
```

#### POST /governance/proposals/{proposal_id}/vote

Vote on proposal.

**Request Body**:
```json
{
  "choice": "for",
  "voting_power": 1000.0
}
```

## Error Responses

All errors follow standard HTTP status codes:

```json
{
  "detail": "Error message",
  "type": "ErrorType",
  "status": 400
}
```

## Rate Limiting

- 1000 requests per hour per API key
- 10 requests per second burst

## Pagination

All list endpoints support pagination:

```
?page=1&limit=20&sort=created_at&order=desc
```
