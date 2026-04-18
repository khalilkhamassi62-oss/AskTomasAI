# Agent Registry

Every agent — from Tomas down to the most specialized assistant — is a row in PostgreSQL. The registry is the single source of truth for agent behavior. Changing an agent requires no code deployment, only a DB update.

## agents Table Schema

```text
agents
├── id                UUID          primary key
├── slug              TEXT          unique  e.g. 'nextjs-specialist'
├── display_name      TEXT          e.g. 'Next.js Engineer'
├── tier              ENUM          ceo | c_suite | director | specialist
├── parent_id         UUID          FK → agents (dispatching parent)
├── domain            TEXT          e.g. 'frontend.nextjs'
├── system_prompt     TEXT          full persona + constraints + examples
├── tools             JSONB         ['file_write','terminal','web_search']
├── mcp_servers       JSONB         ['filesystem','github','vercel']
├── doc_sources       JSONB         ['https://nextjs.org/docs', ...]
├── permissions       JSONB         { 'write_code': true, 'deploy': false,
│                                     'send_email': false, 'spend_money': false }
├── model             TEXT          'nvidia/llama-3.1-nemotron-70b-instruct'
├── max_tokens        INTEGER       4096
├── temperature       FLOAT         0.2
├── langgraph_graph   TEXT          'specialist_graph_v1' (graph class name)
├── is_active         BOOLEAN       true
└── created_at        TIMESTAMPTZ
```

### Why Data‑Driven Agent Config Matters

- Swap the model for any agent without redeploying — just update the row.
- Add a new specialist (e.g. 'Supabase Specialist') by inserting one row and writing a system prompt.
- Restrict an agent's permissions at runtime — revoke deploy rights without touching code.
- A/B test different system prompts for the same agent domain.
- Audit trail — every agent behavior change is a traceable DB mutation.