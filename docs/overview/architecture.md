# System Architecture

Three concentric layers. Each is independently scalable and has a single responsibility.

## The Three Layers

```text
┌──────────────────────────────────────────────────┐
│              PRODUCT LAYER                       │
│   Next.js frontend ← WebSocket ← Redis pub/sub  │
└────────────────────┬─────────────────────────────┘
                     │
┌────────────────────▼─────────────────────────────┐
│            ORCHESTRATION LAYER                   │
│   FastAPI ← LangGraph StateGraphs (per tier)     │
│   Tomas → C‑Suite → Directors → Specialists      │
│   RabbitMQ: routing_key = agent.domain.slug      │
└────────────────────┬─────────────────────────────┘
                     │
┌────────────────────▼─────────────────────────────┐
│              EXECUTION LAYER                     │
│   Celery workers consuming RabbitMQ queues       │
│   Tools: MCP servers, file system, terminals     │
│   Memory: Redis (hot) + Postgres (cold) + pgvector│
└──────────────────────────────────────────────────┘
```

## Execution Flow

```text
User message
   → FastAPI WebSocket handler
   → Tomas LangGraph StateGraph
       [classify_intent]
       [plan_delegation]  → which C‑Suite agents needed?
       [dispatch]         → publish to RabbitMQ: "csuite.cto"

         → CTO LangGraph StateGraph (Celery worker)
             [break_into_epics]
             [dispatch] → publish to "director.frontend"

               → Frontend Director LangGraph
                   [decompose_to_stories]
                   [dispatch] → publish to "specialist.nextjs"

                     → Next.js Specialist LangGraph
                         [retrieve_context]   ← pgvector RAG on docs
                         [plan_execution]
                         [execute_tools]      ← write code, run terminal
                         [validate_criteria]  ← check acceptance criteria
                         [return_result]

                   ← result bubbles up through chain
               ← director aggregates results
           ← CTO synthesizes
       ← Tomas narrates to user via WebSocket
```

## Key Principle: No Direct Agent Calls

Agents never call each other directly. They publish to RabbitMQ with a `routing_key` derived from the target agent's domain slug. FastAPI workers subscribe per domain. This means every tier is horizontally scalable, independently deployable, and fully decoupled.

## Redis Responsibilities

```text
redis:session:{session_id}          ← full conversation context
redis:agent:state:{agent_id}        ← current execution state
redis:ws:channel:{session_id}      ← WebSocket pub/sub stream
redis:approval:pending:{session_id}← queued HITL actions
redis:rate_limit:{agent_id}         ← per‑agent rate limiting
redis:digest:{user_id}:{date}       ← cached morning digest
```