# Budget & Permissions

Budget configuration is per‑company, not per‑project. The user defines two zones: autonomous (agents act freely within limits) and approval‑required (agents pause regardless of budget).

## Budget Configuration Schema

```text
budget_config (per company)
├── monthly_ceiling_usd         500.00    total spend cap
├── per_action_soft_limit       50.00     soft approval trigger
├── autonomous_ceiling          20.00     no approval below this per action
│
├── auto_approve
│     ├── domain_registration           true  (if < $20/yr)
│     ├── npm_pip_packages              true
│     ├── staging_deployments           true
│     └── api_test_calls               true
│
└── always_require_approval
      ├── production_deployments        true
      ├── user_email_sends              true
      ├── llc_registration              true
      ├── paid_subscriptions            true
      ├── data_deletion                 true
      └── spend_above_ceiling           true
```

## Per‑Provider Budget

In addition to the global ceiling, each connected provider has its own monthly budget limit. If the Vercel spend hits its limit, the DevOps agents are blocked from deploying and Tomas surfaces a budget alert rather than silently failing.
