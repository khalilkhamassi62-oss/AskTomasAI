# Build Phases

Eight sequential phases, each producing a testable, deployable milestone.

## Phase 01 – Foundation (Weeks 1–2)

- PostgreSQL schema migrations (all tables)
- Agent registry with seed data (full org chart)
- FastAPI project skeleton — routing, middleware, auth
- NextAuth integration with session management
- Docker Compose: Postgres + Redis + RabbitMQ + FastAPI
- Traefik config for asktomas.com SSL

## Phase 02 – Tomas Core (Weeks 3–4)

- Tomas LangGraph StateGraph — classify, plan, respond
- WebSocket streaming from FastAPI to Next.js
- Chat UI component — streaming messages, Tomas avatar
- Session create/load/persist
- Basic company + project CRUD
- Redis session store integration

## Phase 03 – Agent Dispatch Pipeline (Weeks 5–6)

- RabbitMQ producer/consumer architecture
- C‑Suite LangGraph graphs (CTO, CPO, CMO, CFO)
- Director‑tier graphs (Frontend Dir, Backend Dir, etc.)
- Domain‑based routing_key dispatch system
- Result aggregation and bubble‑up chain
- Agent registry loader — hydrate agent config from DB

## Phase 04 – Specialist Layer + Tools (Weeks 7–9)

- All specialist LangGraph graphs
- MCP server integrations (filesystem, GitHub, Vercel)
- pgvector RAG on agent doc_sources
- Tool execution: file write, terminal, API calls
- Acceptance criteria validation node per specialist
- First end‑to‑end execution: user prompt → code written

## Phase 05 – Agile Engine (Weeks 10–11)

- Agile item generation per agent tier
- Acceptance criteria enforcement logic
- Iteration/sprint creation and management
- Agile board API endpoints
- Real‑time Agile item status updates via WebSocket

## Phase 06 – Canvas Tabs (Weeks 12–13)

- Preview tab — iframe staging renderer
- Code tab — file tree + diff viewer
- Agents tab — React Flow live agent graph, activity feed
- Agile tab — tree view + Kanban board
- Providers tab — spend tracking, status indicators
- Tab state sync with active agent execution

## Phase 07 – HITL + Provider Marketplace (Weeks 14–15)

- Pending action queue and Approval Card UI
- LangGraph interrupt nodes per hard‑approval action
- Graph resume on approval
- Provider vault with encrypted key storage
- Integration marketplace UI
- Budget configuration + per‑provider limits
- Morning digest generation + delivery

## Phase 08 – Voice, Polish, Production (Weeks 16–18)

- Whisper voice input integration
- TTS output for Tomas (optional)
- Autonomous Run mode
- Trust learning system (auto‑approve suggestions)
- Performance optimization and load testing
- AWS production deployment
- Monitoring: Sentry, Prometheus, Grafana
- Onboarding flow polish — Company Brief UI