# Tech Stack

## Core Technologies

| Technology | Role | Owns |
|------------|------|------|
| Next.js 14 + Shadcn + Tailwind | Frontend | App shell, chat UI, canvas tabs, Agile board, command menu, auth pages |
| FastAPI | Backend API + Orchestration | REST/WebSocket endpoints, LangGraph graph invocation, session management, approval routing |
| LangChain | Agent Tool Layer | Tool definitions, MCP server connectors, document loaders, chain primitives |
| LangGraph | Agent Execution | StateGraph definitions per agent tier, interrupt nodes for HITL, conditional routing |
| Redis | Hot State + Streaming | Session context, WebSocket pub/sub, approval queues, rate limiting, digest cache |
| RabbitMQ | Async Task Dispatch | Agent‑to‑agent work queues, domain‑routed messages, dead‑letter queues |
| PostgreSQL + pgvector | Persistent Storage + RAG | All core entities, agent registry, agile items, semantic search on codebase + docs |
| NVIDIA Build APIs | LLM Inference | Model routing per agent tier — heavier models for CEO/C‑Suite, lighter for specialists |
| Traefik | Reverse Proxy + SSL | HTTPS for asktomas.com, service routing, Let's Encrypt cert management |
| AWS Free Tier | Infrastructure | EC2 for compute, RDS (optional), S3 for artifacts, initial deployment target |

## LangGraph — Why It's Central

LangGraph's `StateGraph` gives each agent tier a stateful, resumable execution graph. The critical feature for AskTomas is the **interrupt node** — when an agent hits a hard‑approval action, the graph suspends, persists its state to Redis, and waits. When the user approves, the graph resumes from the exact point it stopped. This is the technical foundation of the HITL system.

## NVIDIA Build — Model Routing

```text
Tier        Model                                    Reason
────────────────────────────────────────────────────────────
CEO         nvidia/llama-3.1-nemotron-70b-instruct   Complex synthesis, user‑facing
C‑Suite     nvidia/llama-3.1-nemotron-70b-instruct   Strategic reasoning
Directors   nvidia/llama-3.1-70b-instruct            Decomposition, structured output
Specialists nvidia/llama-3.1-8b-instruct             Fast execution, high volume
```