# User Journeys

## JRN 01 – First Contact — Onboarding

**Description:** The most critical journey. The moment after signup isn’t a dashboard — it’s Tomas, asking one question: 'Tell me what you’re building.'

**Steps**
1. **Intake Conversation** – User describes their idea in free‑form text or voice. Tomas asks clarifying questions: problem, target customer, budget runway, prior validation, preferred name.
2. **Company Brief** – **HITL CHECKPOINT** — Tomas produces a structured Company Brief: name, entity type, jurisdiction, core product description, recommended tech stack, estimated monthly operating cost, and first sprint scope. User reviews, edits, and approves each section before anything spins up.
3. **Provider Setup** – Tomas presents a prioritized list of required integrations specific to this product idea — not a generic dump. User pastes API keys into an encrypted vault. Budget limits set per provider.
4. **Budget Configuration** – **HITL CHECKPOINT** — User defines autonomous zones (agents act freely) and approval‑required zones (agents must pause and surface a request before proceeding).

---

## JRN 02 – Idea to Live Product

**Description:** The flagship journey. The story told on the landing page.

**Steps**
1. **Day 0** – Idea described → Company Brief approved → Tomas scaffolds company structure + first initiative in the Agile board.
2. **Day 1** – Agents begin executing Sprint 1. Code appears in the canvas Code tab. Preview tab begins rendering.
3. **Day 2–3** – User reviews first working build on staging. Approves deployment. Provides feedback in chat — Tomas re‑routes to relevant agents.
4. **Day 5** – Landing page live, Stripe wired, waitlist running. Domain registered (approved by user), email connected.
5. **Day 7** – MVP feature‑complete. Final HITL review. Production launch.

---

## JRN 03 – Daily Execution Loop

**Description:** After onboarding, this is the normal operating cadence for every session.

**Steps**
1. **User Opens Session** – Tomas presents a Morning Digest: what was completed, what’s in progress, what needs review, what’s blocked.
2. **User Reviews & Approves** – Approval Cards surfaced in chat for any pending HITL actions. User approves, modifies, or rejects.
3. **User Provides Direction** – User adds new goals or feedback in plain language. Tomas updates the Agile board and dispatches to relevant agents.
4. **Agents Execute Async** – Specialists work in the background — coding, writing, configuring, deploying. User can close the app.
5. **Morning Digest on Return** – User returns to a digest of everything that happened. Cycle repeats.

---

## JRN 04 – HITL Approval Flow

**Description:** The trust layer. Every high‑stakes action pauses the agent and surfaces an Approval Card before execution.

**Steps**
1. **Agent Triggers Action** – An agent determines it needs to perform a high‑stakes action (deploy to prod, register domain, send emails to users, subscribe to a paid service, register LLC).
2. **Action Queued** – Instead of executing, the agent publishes to the approval queue. Tomas surfaces an Approval Card in the chat with full context: action, cost, requester, reason.
3. **User Decides** – User taps Approve, Modify, Reject, or Ask Tomas. If modified, the new parameters are passed back to the agent.
4. **Execution or Cancellation** – If approved, the action executes immediately. If rejected, Tomas records the reason and instructs the agent to find an alternative path.
5. **Trust Building** – If the user approves the same type of action 10+ times, Tomas suggests elevating it to auto‑approve. The system learns.

---

## JRN 05 – Provider Connection

**Description:** The Integrations tab acts as a capability marketplace. Adding a new provider unlocks new agent capabilities.

**Steps**
1. **Browse Marketplace** – User opens Integrations tab. Sees connected providers and available ones, organized by category (hosting, payments, email, communication, DNS, storage).
2. **Connect Provider** – User selects a provider, sees exactly which agents will use it and what actions they’ll be able to take. Pastes API key into encrypted vault.
3. **Capability Expansion** – Tomas proactively surfaces: 'Now that Resend is connected, I can automate your transactional emails. Want me to set up email templates for your onboarding flow?'
4. **Budget Scoping** – User sets per‑provider spend limits. Some provider actions require explicit per‑action approval regardless of budget.

---

## JRN 06 – Multi‑Project Management

**Description:** Power users eventually build multiple products under multiple companies.

**Steps**
1. **Company Switching** – Header company dropdown lets user switch between companies instantly. Each company has its own vault, budget, agent config, and billing.
2. **Project Selection** – Within a company, multiple projects exist. Each project has its own session history, Agile board, preview URL, and codebase.
3. **Context Isolation** – Starting a session in Project A means Tomas knows that company’s stack, prior decisions, brand voice, and current sprint. Zero bleed between projects.
4. **Cross‑Company Agents** – Global agents (shared) can serve multiple companies. Dedicated agents (per‑company) are trained on that company’s context specifically.

---

## JRN 07 – Autonomous Run (Power Mode)

**Description:** For founders who have established trust. Fire, forget, review.

**Steps**
1. **Set the Goal** – User gives Tomas a time‑boxed goal with a budget ceiling: 'Build and launch a waitlist landing page by Friday. Budget: $100.'
2. **Tomas Plans** – Tomas auto‑generates the full Agile breakdown — initiative, epics, features, stories, tasks — all with acceptance criteria. User gets one confirmation card before execution begins.
3. **Agents Execute** – All auto‑approvable actions proceed. Hard‑approval items are queued without blocking other work.
4. **Consolidated Review** – At the end (or at a configured time), user gets one card: 'Ready for launch. 3 items need your sign‑off.' All queued approvals in one batch.
5. **Launch** – User approves the batch. Tomas executes the final actions in sequence and confirms launch.