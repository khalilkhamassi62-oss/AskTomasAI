# Agile System

Modeled directly after Azure DevOps. The Agile board is not something the user manages manually — it is generated and maintained by the agents, with the user as the strategic reviewer.

## Item Hierarchy

```text
Initiative  (Tomas generates — top‑level company goal)
   └── Epic  (C‑Suite generates — domain‑specific strategic theme)
         └── Feature  (Director generates — deliverable capability)
               └── Story  (Director generates — user‑facing behavior)
                     └── Task  (Specialist generates — atomic work unit)
                           └── Bug  (any agent can file — deviation from acceptance criteria)
```

## agile_items Table Schema

```text
agile_items
├── id                    UUID
├── project_id            UUID          FK → projects
├── type                  ENUM          initiative|epic|feature|story|task|bug
├── parent_id             UUID          FK → agile_items (self‑referential)
├── title                 TEXT
├── description           TEXT          markdown
├── acceptance_criteria   JSONB         [{ "criterion": "User can create invoice", "met": false, "tested_by": "agent_id or null" }, ...]
├── assigned_agent_id     UUID          FK → agents
├── status                ENUM          backlog|todo|in_progress|review|done
├── priority              ENUM          critical|high|medium|low
├── story_points          INTEGER
├── iteration_id          UUID          FK → iterations
├── created_by_agent_id   UUID          FK → agents
├── tags                  JSONB         ['auth','billing','frontend']
└── created_at, updated_at
```

## Acceptance Criteria Enforcement

This is the key mechanism that prevents agents from shipping incomplete work. Every Task and Story has a structured `acceptance_criteria` array. A specialist agent **cannot mark a task done** until all criteria are marked as met. Each criterion can specify a testing agent (e.g., a QA Specialist that runs assertions).

## Iteration / Sprint Model

```text
iterations
├── id, project_id
├── name              TEXT    "Sprint 1"
├── goal              TEXT    plain‑language sprint goal
├── start_date        DATE
├── end_date          DATE
├── status            ENUM    planning | active | review | closed
└── velocity          INTEGER  actual story points completed
```

## Generation Flow

```
Tomas → Initiative
C‑Suite (CTO/CPO/CMO/CFO) → Epic
Directors → Feature
Directors → Story
Specialists → Task
```

Each tier is represented as a card in the UI, showing which agents are responsible for generating the next level of work.
