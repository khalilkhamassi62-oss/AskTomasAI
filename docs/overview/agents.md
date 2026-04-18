# Agent Hierarchy

| Tier | Role | Responsibility |
|------|------|----------------|
| CEO | Tomas | User interface |
| C‑Suite | CTO/CPO/CMO/CFO | Domain strategy |
| Director | Frontend Dir | Feature decomposition |
| Specialist | Next.js | Task execution |

## Specialist Agent Domains (Sample)

| Slug | Domain | Tools | MCP Servers |
|------|--------|-------|--------------|
| nextjs-specialist | frontend.nextjs | file_write, terminal | filesystem, github, vercel |
| fastapi-specialist | backend.fastapi | file_write, terminal | filesystem, github |
| postgres-specialist | backend.postgres | terminal, db_query | filesystem, pg |
| stripe-specialist | backend.stripe | api_call | stripe-mcp |
| resend-specialist | marketing.email | api_call, template_write | resend-mcp |
| cloudflare-specialist | devops.dns | api_call | cloudflare-mcp |
| aws-specialist | devops.aws | terminal, api_call | aws-cdk-mcp |
| ux-specialist | design.ux | file_write, figma_api | figma-mcp |
| seo-specialist | marketing.seo | web_search, file_write | web-search |
| pricing-specialist | finance.pricing | web_search, spreadsheet | web-search |