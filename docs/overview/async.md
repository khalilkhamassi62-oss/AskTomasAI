# Autonomous Run Mode

After a user has established trust with the system through HITL interactions, they unlock Power Mode — goal‑oriented autonomous execution with minimal interruption.

## Two Session Modes

| Mode | Description |
|------|-------------|
| INTERACTIVE | Live Session – User is present and engaged. Agents stream results in real time to the canvas. Approvals surface immediately. User provides feedback inline. Best for ideation, first sprints, and high‑touch reviews. |
| AUTONOMOUS | Fire & Forget – User sets goal + budget + deadline, then closes the app. Agents execute in the background. Hard‑approval items queue without blocking others. User returns to a consolidated review and single approval batch. |

## Autonomous Run Flow

```text
User: 'Build and launch a waitlist landing page by Friday. Budget: $100.'

Tomas:
  1. Generates Agile breakdown (initiative → epics → features → tasks) autonomously
  2. Surfaces ONE confirmation card: 'Ready to begin. Here’s the full plan. [Start]'
  3. User confirms → execution begins

Background execution:
  - All auto‑approvable actions execute immediately
  - Hard‑approval items queue silently (no interruption)
  - Cross‑agent work continues in parallel
  - Real‑time progress visible in Agents tab if user returns

On goal completion (or Friday deadline):
  Tomas: 'Landing page is ready. 3 items need your approval before launch:
    1. Deploy to production (vercel)
    2. Send announcement to 247 waitlist subscribers
    3. DNS propagation (domain: invoicepro.io)
    [Review & Approve All]'
```