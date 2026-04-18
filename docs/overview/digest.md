# Morning Digest

The re‑engagement loop. When the user returns to a session (or opens the app after time away), Tomas surfaces a structured digest of all async activity. This is the user's daily briefing from their AI company.

## Digest Structure

```text
Good morning. Here's what happened while you were away:

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅  COMPLETED  (8 tasks)
    Auth system is live on staging.
    Email/password + Google OAuth working.
    4 unit tests passing.

⏳  IN PROGRESS  (3 tasks)
    Stripe billing integration — 60% complete (ETA: 2 hours)
    Invoice PDF generator — assigned to backend team

🔵  AWAITING YOUR REVIEW  (2 items)
    1. Database schema change — adds subscription_plans table
       [View Diff]  [Approve]  [Reject]
    2. Email template to 247 waitlist subscribers
       [Preview Email]  [Approve Send]  [Edit First]

⚠️  BLOCKED  (1 item)
    Resend free tier rate limit hit. Options:
    [Upgrade to paid — $20/mo]  [Wait 24 hours]  [Switch provider]

💰  SPEND THIS WEEK  $12.40 of $500.00 budget
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

The digest is also delivered via email and push notification with a configurable schedule. The user can set a "daily briefing time" and receive the digest at 8 am even if they haven't opened the app.
