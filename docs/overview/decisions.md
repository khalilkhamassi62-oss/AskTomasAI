# Key Architectural Decisions

These are the decisions that have the most downstream impact. Each was chosen deliberately.

## Decision 1 – LangGraph for all agent tiers

**Why:** StateGraph gives each agent resumable, inspectable execution. The interrupt node is the technical foundation of the entire HITL system — agents can pause mid‑execution, wait for human approval, and resume exactly where they stopped. No other framework provides this cleanly.

**Trade‑off:** Higher complexity than simple LLM chains. Each StateGraph requires explicit node definitions and routing logic.

## Decision 2 – RabbitMQ for inter‑agent dispatch (not direct calls)

**Why:** Agents publishing to routing‑key queues rather than calling each other means every agent tier is independently scalable, deployable, and observable. Dead‑letter queues catch failures. Work isn’t lost if a worker crashes.

**Trade‑off:** Added operational complexity vs. a simpler request/response model. Requires careful queue design.

## Decision 3 – Agent config in PostgreSQL (data‑driven, not code‑driven)

**Why:** Changing an agent’s system prompt, model, or permissions requires a DB update, not a code deployment. This enables runtime agent management, A/B testing of prompts, and adding new specialists without engineering involvement.

**Trade‑off:** System prompt quality depends on whoever edits the DB. Versioning of agent configs must be handled explicitly.

## Decision 4 – pgvector for RAG (embedded in existing Postgres)

**Why:** Keeps the data layer unified. Semantic search over agent docs, conversation history, and codebase lives in the same Postgres instance as structured data. Simplifies ops on AWS Free Tier significantly.

**Trade‑off:** Not as performant as dedicated vector DBs (Qdrant, Pinecone) at very large scale. Acceptable for MVP and early growth.

## Decision 5 – Tomas as the sole user‑facing interface

**Why:** The user should never need to think about agent routing, queue depths, or graph states. Tomas translates all technical activity into business language. This is the UX contract that makes the product accessible to non‑technical Idea Holders.

**Trade‑off:** Tomas becomes a critical path. If Tomas’s synthesis is poor, the whole product experience degrades.

## Decision 6 – Acceptance criteria as a structured enforcement layer

**Why:** Without structured criteria, agents self‑report completion incorrectly. Each Task has an array of testable criteria that must be validated before status can advance to ‘done’. This mirrors how real engineering teams work and prevents the classic “it works on my machine” agent failure mode.

**Trade‑off:** Requires agents to generate good acceptance criteria in the first place. Quality of criteria = quality of enforcement.