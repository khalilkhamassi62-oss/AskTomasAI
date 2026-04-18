# AskTomas AI‑Native Platform – Implementation Plan

**Purpose**: Build the end‑to‑end “company‑in‑a‑box” platform covering data model, FastAPI core, LangGraph agents, RabbitMQ dispatcher, specialist tooling, UI, human‑in‑the‑loop (HITL) approval flow, voice integration, CI/CD, monitoring, testing and production deployment.

---

## Phase 01 – Foundations & CI/CD
- [ ] **01‑01** Add GitHub Actions workflow for lint, type‑check, unit tests, and Docker build.
- [ ] **01‑02** Configure `npm` scripts in `client/package.json` for `dev`, `build`, `start`, `lint`.
- [ ] **01‑03** Set up a dedicated git worktree for the feature branch using `using‑git‑worktrees`.
- [ ] **01‑04** Verify CI runs locally (`npm run lint && npm run test && npm run build`).

## Phase 02 – Database Schema & Migrations
- [ ] **02‑01** Create `backend/db/migrations/001_create_base_tables.sql` with core tables (companies, users, agents, sessions, messages, approvals).
- [ ] **02‑02** Add seed data in `backend/seed/agents_seed.sql` for initial agents (Tomas, CTO, CPO, CMO, CFO, etc.).
- [ ] **02‑03** Write Alembic‑style migration runner in `backend/db/migration_runner.py`.
- [ ] **02‑04** Add integration test `backend/tests/db/test_migrations.py` (fail‑first).

## Phase 03 – FastAPI Core & Auth
- [ ] **03‑01** Scaffold FastAPI app in `backend/app/main.py` (app factory, CORS, middlewares).
- [ ] **03‑02** Implement JWT auth utilities in `backend/app/dependencies.py` and route `backend/app/router/auth.py`.
- [ ] **03‑03** Create generic CRUD routers (`router/companies.py`, `router/users.py`, `router/agents.py`).
- [ ] **03‑04** Add unit tests for auth (`backend/tests/auth/test_jwt.py`).

## Phase 04 – LangGraph Agent Engine
- [ ] **04‑01** Define base `AgentState` model in `backend/agents/base/state.py`.
- [ ] **04‑02** Implement Tomas agent state‑graph in `backend/agents/tomas/stategraph.py`.
- [ ] **04‑03** Repeat for CTO, CPO, CMO, CFO, Director, Specialist agents.
- [ ] **04‑04** Add agent registry `backend/agents/registry.py`.
- [ ] **04‑05** Write tests for state‑graph transitions (`backend/tests/agents/test_tomas.py`).

## Phase 05 – RabbitMQ Dispatcher & Workers
- [ ] **05‑01** Add `backend/queue/producer.py` (publish agent tasks).
- [ ] **05‑02** Add `backend/queue/consumer.py` (consume, invoke LangGraph, publish results).
- [ ] **05‑03** Create Docker Compose service `rabbitmq` with default config.
- [ ] **05‑04** Write integration test `backend/tests/queue/test_rabbitmq.py`.

## Phase 06 – Specialist Tools (MCP, RAG, Agile, Criteria)
- [ ] **06‑01** Implement file‑system MCP stub in `backend/mcp/filesystem.py`.
- [ ] **06‑02** Add GitHub & Vercel stubs (`backend/mcp/github.py`, `backend/mcp/vercel.py`).
- [ ] **06‑03** Build vector‑search service `backend/rag/vector_search.py` using `sentence‑transformers`.
- [ ] **06‑04** Create Agile sprint model (`backend/agile/models.py`) and service (`backend/agile/service.py`).
- [ ] **06‑05** Add criteria‑check middleware `backend/app/middleware/criteria_check.py`.
- [ ] **06‑06** Write unit tests for each specialist tool.

## Phase 07 – UI (React + Next.js) – Multi‑Tab Experience
- [ ] **07‑01** Add a new page `client/pages/preview.tsx` with tabs for **UI, Code, Agents, Actions, Ops**.
- [ ] **07‑02** Implement `CodeTab` component (`client/components/CodeTab.tsx`) showing generated code with syntax highlighting.
- [ ] **07‑03** Implement `AgentsGraph` component (`client/components/AgentsGraph.tsx`) using `react‑flow`.
- [ ] **07‑04** Add `ActionsTab` for executing actions via the backend API.
- [ ] **07‑05** Add `OpsTab` showing job status, logs, and monitoring charts.
- [ ] **07‑06** Write component tests with React Testing Library (`client/__tests__/AgentsGraph.test.tsx`).

## Phase 08 – Human‑In‑The‑Loop (HITL) Approval Flow
- [ ] **08‑01** Create `backend/app/router/approval.py` with endpoint `POST /approval/{task_id}`.
- [ ] **08‑02** Add UI modal `ApprovalModal` in `client/components/ApprovalModal.tsx`.
- [ ] **08‑03** Store approval decisions in DB table `approvals`.
- [ ] **08‑04** Write end‑to‑end test simulating a task needing approval (`backend/tests/hitl/test_approval_flow.py`).

## Phase 09 – Voice Integration (STT/TTS)
- [ ] **09‑01** Add Whisper wrapper in `backend/app/router/voice.py` for speech‑to‑text.
- [ ] **09‑02** Add ElevenLabs TTS wrapper in same router.
- [ ] **09‑03** Extend UI with microphone button and audio playback component.
- [ ] **09‑04** Add integration tests mocking external services.

## Phase 10 – Monitoring, Logging & Observability
- [ ] **10‑01** Configure `prometheus_client` in FastAPI (`backend/app/metrics.py`).
- [ ] **10‑02** Add Grafana dashboards (docker compose) in `monitoring/`.
- [ ] **10‑03** Wire log‑formatters and JSON logging.
- [ ] **10‑04** Write smoke tests that hit `/metrics`.

## Phase 11 – Docker, Traefik & Terraform Deployment
- [ ] **11‑01** Create `Dockerfile` for backend (multi‑stage, Alpine).
- [ ] **11‑02** Create `docker-compose.yml` including backend, client, rabbitmq, prometheus, grafana, traefik.
- [ ] **11‑03** Add `traefik/traefik.yml` with router rules for each service.
- [ ] **11‑04** Write Terraform `infra/aws/main.tf` to provision ECS cluster, RDS, S3, IAM.
- [ ] **11‑05** Add CI step to push Docker images to ECR.
- [ ] **11‑06** Verify deployment with `terraform apply` (dry‑run for now).

## Phase 12 – Documentation, Release & Finalization
- [ ] **12‑01** Populate `README.md` with architecture diagram, quick‑start, and contribution guide.
- [ ] **12‑02** Generate API docs with FastAPI OpenAPI schema (`/docs`).
- [ ] **12‑03** Run full test suite (`npm run test && pytest`).
- [ ] **12‑04** Use `finishing-a-development-branch` skill to decide on PR, merge, or cleanup.

---

### Execution Guidelines
1. **Test‑first**: For each file creation add a failing test, then implement code, re‑run tests until they pass.
2. **Commit after each logical step** using conventional‑commit messages (e.g., `feat(db): add base tables`).
3. **Run CI locally** before pushing.
4. **Report status** after every task (success or error) so the next sub‑agent can continue.

*All paths are relative to the repository root.*

---

**Next step:** I will create this file at `IMPLEMENTATION_PLAN.md` and then start Phase 01.
