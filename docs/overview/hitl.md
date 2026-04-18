# Human‑in‑the‑Loop Approvals

The approval layer is what separates AskTomas from a fully unsupervised automation tool. It's designed to build trust, not create friction. Approval fatigue is the enemy — the system should only interrupt for decisions that genuinely require human judgment.

## Approval Card Anatomy

```text
┌─────────────────────────────────────────────────────┐
│  🔵 Action Required                    2 min ago   │
│                                                     │
│  Register domain: asktomas.io                      │
│  Registrar: Cloudflare · Cost: $8.57/year          │
│  Requested by: DevOps Director                     │
│  Reason: Primary domain for MVP deployment         │
│                                                     │
│  [Approve]   [Modify]   [Reject]   [Ask Tomas]     │
└─────────────────────────────────────────────────────┘
```

## Approval Tiers

| Action | Tier | Default Behavior | Upgradeable? |
|-------|------|------------------|------------|
| Write code | Auto | Executes freely | N/A |
| Create GitHub repo | Auto | Executes freely | N/A |
| Send test email (to self) | Auto | Executes freely | N/A |
| Install npm/pip package | Auto | Executes freely | N/A |
| Register domain (< budget) | Soft | Auto if under ceiling | Yes → full auto |
| Deploy to staging | Soft | Auto if under ceiling | Yes → full auto |
| Deploy to production | Hard | Always requires approval | No |
| Send email to real users | Hard | Always requires approval | No |
| Subscribe to paid service | Hard | Always requires approval | No |
| Register LLC | Hard | Always requires approval | No |
| Delete data / resources | Critical | Approval + confirmation code | No |
| Spend > budget ceiling | Critical | Blocked until ceiling raised | No |

## Trust Learning

The system tracks approval patterns per user per action type. After **10 consecutive approvals** of the same action type without modification, Tomas surfaces a suggestion: *"You've approved every Vercel staging deployment without changes. Want me to auto‑approve those going forward?"* Rejections and modifications are equally important. Each rejection trains the relevant agent: the reason is stored against the `pending_action` record and injected into the agent's context on next invocation.
