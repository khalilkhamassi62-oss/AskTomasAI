# Data Models

Full PostgreSQL schema covering all core entities. pgvector columns added to relevant tables for semantic search.

```text
-- Company structure
companies
├── id, name, slug, owner_id
├── settings          JSONB   { brand_voice, timezone, industry }
└── created_at

projects
├── id, company_id, name, slug, description
├── tech_stack        JSONB   ['nextjs','fastapi','postgres']
├── repo_url, preview_url, staging_url
└── status            ENUM    active | paused | archived

sessions
├── id, project_id, user_id
├── title             TEXT    (auto‑generated from first message)
├── mode              ENUM    interactive | autonomous
├── status            ENUM    active | paused | completed
└── created_at

messages
├── id, session_id
├── role              ENUM    user | tomas | agent | system
├── agent_id          UUID    FK → agents (nullable)
├── content           TEXT
├── metadata          JSONB   { agent_tier, task_id, approval_id }
├── embedding         vector(1536)   pgvector
└── created_at

-- Provider vault
provider_connections
├── id, company_id
├── provider          TEXT    'github' | 'stripe' | 'vercel' | ...
├── api_key_enc       TEXT    encrypted at rest
├── scopes            JSONB   ['read','write','deploy']
├── budget_limit_usd  DECIMAL
├── spend_this_month  DECIMAL
└── connected_at

-- HITL Approval queue
pending_actions
├── id, session_id, company_id
├── action_type       TEXT    'register_domain' | 'deploy_prod' | ...
├── requested_by      UUID    FK → agents
├── payload           JSONB   full action parameters
├── cost_estimate     DECIMAL
├── status            ENUM    pending | approved | modified | rejected
├── resolved_by       UUID    FK → users (nullable)
├── resolution_note   TEXT
├── created_at, resolved_at

-- Morning digest cache
digests
├── id, user_id, project_id
├── date              DATE
├── completed         JSONB   array of completed task summaries
├── in_progress       JSONB   array of in‑progress items
├── pending_review    JSONB   array of items needing HITL
├── blocked           JSONB   array of blocked items with context
└── generated_at
```