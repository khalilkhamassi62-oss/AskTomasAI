# UI / UX Design

The AskTomas UI is modeled after Lovable's aesthetic — clean, focused, split‑pane — but purpose‑built for an AI‑orchestrated company. The user's primary interface is always the conversation with Tomas. Everything else is secondary.

## Shell Layout

```text
┌──────────────────────────────────────────────────────────────────┐
│  [⌘K  Search or ask anything...]    [Acme Corp ▾]   [K] ⚙       │  ← Header
├───────────────────┬──────────────────────────────────────────────┤
│                   │  [Preview] [Code] [Providers] [Integrations]  │
│                   │  [Agents ●] [Agile]                           │  ← Tab Bar
│   T O M A S       │                                              │
│   C H A T         │                                              │
│                   │                                              │
│   20%             │            CANVAS  80%                       │
│                   │                                              │
│   text / voice    │   live, reactive, context‑aware               │
│   streaming       │   renders based on active tab                │
│                   │                                              │
│  ┌─────────────┐  │                                              │
│  │ type or 🎙  │  │                                              │
│  └─────────────┘  │                                              │
└───────────────────┴──────────────────────────────────────────────┘
```

## Header Components

- **⌘K Command Menu** — Searches across all conversations, projects, agile items, agents, and providers. Also accepts natural language commands: 'Show me what\'s blocking Sprint 2', 'Switch to Acme Corp', 'Approve all pending items'.
- **Company Dropdown** — Switch between companies instantly. Shows active project count and live agent indicators per company.
- **Avatar / Settings** — Account, provider vault, notification preferences, subscription, budget overview.

## Canvas Tabs

- **Preview** – Renders the actual project in an embedded iframe. Connected to the staging environment. Updates automatically on each agent deployment.
- **Code** – A VS Code‑like file tree + diff viewer. Shows exactly what agents are writing in real time. Read‑only by default; edits surface as a suggestion to Tomas.
- **Providers** – Live status of all connected API providers. Shows current usage, spend vs. budget, rate‑limit status, recent actions taken per provider.
- **Integrations** – The provider marketplace. Connected integrations and available ones. Adding a new integration expands agent capabilities immediately.
- **Agents ●** – A live force‑directed graph (React Flow / D3) of the agent hierarchy. Active agents pulse. Task labels on edges show what each agent is currently doing. A real‑time activity feed runs below the graph. This is the 'engine room' view.
- **Agile** – The Azure DevOps‑inspired board. Left: tree view (Initiative → Epic → Feature → Story → Task). Right: Kanban board columns (Backlog, Todo, In Progress, Review, Done). Top: iteration/sprint selector. Each item shows acceptance criteria, assigned agent, status, and creation trail.

## Tomas Chat — Key UX Rules

1. Tomas speaks in business language, never tech jargon. The user never sees 'RabbitMQ task dispatched to specialist.nextjs' — they see 'I've asked the frontend team to start on the dashboard layout.'
2. Every agent action is traceable. Click any message or Agile item to see which agent produced it, the instructions it was given, and its acceptance criteria.
3. Approval Cards surface inline in chat — not in a separate notification center. They are part of the conversation.
4. Tomas owns the narrative. Even when 20 agents run in parallel, Tomas synthesizes everything into one coherent update.
5. Voice input supported via Whisper. TTS output available for Tomas responses (optional, configurable).
6. Morning Digest appears at the top of chat when the user returns to a session — a structured summary of async activity since the last visit.