# Multi‑Company & Multi‑Project

Power users build multiple products. The company/project hierarchy is a first‑class concept in AskTomas, not an afterthought.

## Company & Project Structure

```text
User Account
   ├── Acme Corp
   │     ├── Project: InvoicePro      (Active sprint, staging live)
   │     ├── Project: Landing Page    (Completed, production)
   │     └── Project: Mobile App      (Backlog)
   │
   └── Nova Labs
         ├── Project: API Gateway     (In Progress)
         └── Project: Admin Dashboard (Planning)
```

## Isolation Guarantees

- Each company has its own encrypted provider vault — API keys never bleed between companies.
- Each company has its own budget configuration and spend tracking.
- Tomas per‑session has the context of that company's decisions, brand voice, tech stack, and current sprint — no cross‑company contamination.
- Agents can be global (shared across companies) or dedicated (trained on one company's codebase and decisions).
- Future billing model: per‑company subscription tier, allowing resale to clients.
