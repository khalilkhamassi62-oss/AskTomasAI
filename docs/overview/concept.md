# Core Concept

AskTomas mimics a real company org chart. Every role that exists in a funded startup has an AI equivalent. The hierarchy determines both **decision authority** and **task routing**.

## Chain of Command

```text
User
   └── Tomas (CEO Agent)  ←── single point of user contact
         ├── CTO Agent
         │     ├── Frontend Director
         │     │     ├── Next.js Specialist        domain: frontend.nextjs
         │     │     ├── React Specialist          domain: frontend.react
         │     │     └── Tailwind/CSS Specialist   domain: frontend.styling
         │     ├── Backend Director
         │     │     ├── FastAPI Specialist         domain: backend.fastapi
         │     │     ├── PostgreSQL Specialist      domain: backend.postgres
         │     │     ├── Redis Specialist           domain: backend.redis
         │     │     └── RabbitMQ Specialist        domain: backend.rabbitmq
         │     └── DevOps Director
         │           ├── Docker Specialist          domain: devops.docker
         │           ├── Traefik Specialist         domain: devops.traefik
         │           └── AWS Specialist             domain: devops.aws
         ├── CPO Agent
         │     ├── Product Director
         │     │     ├── PRD Specialist             domain: product.prd
         │     │     └── User Story Specialist      domain: product.stories
         │     └── Design Director
         │           ├── UX Specialist              domain: design.ux
         │           └── UI Specialist              domain: design.ui
         ├── CMO Agent
         │     ├── Content Director
         │     │     ├── Copywriter Specialist      domain: marketing.copy
         │     │     └── SEO Specialist             domain: marketing.seo
         │     └── Growth Director
         │           └── Email/Outreach Specialist  domain: marketing.outreach
         └── CFO Agent
               └── Finance Director
                     ├── Pricing Specialist         domain: finance.pricing
                     └── Metrics Specialist         domain: finance.metrics
```

## What Makes It Different

Every specialist agent is *micro‑specialized*. The Next.js agent doesn’t know anything about Stripe. The Stripe agent doesn’t write JSX. This narrowness enforces separation of concerns at the agent level, produces more accurate output, and makes agents replaceable and upgradeable independently.

Each agent’s configuration (system prompt, tools, MCP servers, doc sources, permissions, model) lives in PostgreSQL as a row in the **agent registry**. This means the system is data‑driven — you can change an agent’s behavior, swap its model, or add a new specialist without touching code.