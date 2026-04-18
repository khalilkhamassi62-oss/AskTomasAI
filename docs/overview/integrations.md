# Integrations & Provider Marketplace

Providers are the hands of the agents. Every provider connection is stored per‑company in an encrypted vault. The capability manifest determines which agents can use which provider and what actions they can take.

## Integration Categories

- **Code & Deployment** – GitHub, Vercel, Netlify, Railway, Render
- **Payments** – Stripe, Paddle, LemonSqueezy
- **Email** – Resend, Postmark, SendGrid, Mailchimp
- **DNS & Domains** – Cloudflare, Namecheap, Route53
- **Communication** – Twilio, Slack, Discord
- **Legal & Entity** – Stripe Atlas, Clerky, Registered Agent
- **Storage** – AWS S3, Supabase Storage, Cloudflare R2
- **Analytics** – PostHog, Mixpanel, Plausible
- **AI / LLMs** – OpenAI, Anthropic, NVIDIA, Groq

## Capability Manifest Structure

```text
{\n  'provider': 'stripe',\n  'agent_tiers': ['specialist'],\n  'allowed_agents': ['stripe-specialist'],\n  'actions': [\n    { 'id': 'create_customer',    'approval': 'auto' },\n    { 'id': 'create_price',       'approval': 'soft' },\n    { 'id': 'create_product',     'approval': 'soft' },\n    { 'id': 'issue_refund',       'approval': 'hard' },\n    { 'id': 'create_subscription','approval': 'hard' }\n  ],\n  'budget_tracked': true,\n  'spend_category': 'payments_infrastructure'\n}\n```