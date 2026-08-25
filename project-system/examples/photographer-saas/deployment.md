# Deployment — Photographer SaaS

How the photographer SaaS would ship and run: environments, secrets, rollout, rollback, on-call. This artifact is **agent-neutral** and **artifact-level only** — it describes the planned shape; it does not stand up real infrastructure.

> **Stop-point notice (per [`README.md`](README.md) §1).** The BuildSolid v0.1 reference example fills this artifact as a planning document. It does **not** include source code, infrastructure-as-code, a live deployment, secret values, or production credentials. Stages 9–12 of the BuildSolid workflow remain artifact-level for this example. Treat the contents below as the *would-deploy* design that a future implementation phase would execute against, not as a record of running infrastructure.

Workflow phase: **Phase 11 — Deployment.** Driving skill: `deployment-manager` (planning artifact only — BuildSolid v0.1 does not automate deployment).

Related artifacts: [`architecture.md`](architecture.md), [`intelligence-layer.md`](intelligence-layer.md), [`spec.md`](spec.md), [`launch-checklist.md`](launch-checklist.md), [`decisions.md`](decisions.md).

---

## 1. Environments

The MVP would ship through two environments. A third (`dev`) is the photographer-builder's local working tree; it is named here so the layout is obvious, but only `staging` and `production` are deployed targets.

- **`dev` (local)** — purpose: photographer-builder's working tree; access: founder only; data source: generated or otherwise rights-cleared synthetic fixtures. The shipped example includes no real gallery or consent record.
- **`staging`** — purpose: rehearsal of every change before production; access: authorized test users only; data source: representative synthetic galleries until every real-photo gate passes.
- **`production`** — prospective purpose: real deliveries to real clients; access: signed-up photographers; real photos are admitted only after provider, retention/restore, security, privacy, and qualified legal-review gates pass.

The MVP does not define separate *region* environments. `production` is single-region (per [`architecture.md`](architecture.md) §7); a multi-region strategy is deferred work, not an alternate first-iteration trigger under DEC-8.

## 2. Secrets and credentials

Secrets live in the deployment platform's managed secret store, never in this repository. The list below names the secrets the MVP requires; values are not recorded here, anywhere in this directory, or anywhere in the BuildSolid repository.

- **AI provider API key** — used by: API service's model-call boundary; storage: deployment platform secret store; rotation: every 90 days, on a calendar reminder.
- **Object-storage access key** — used by: API service for signed URL minting; storage: deployment platform secret store; rotation: every 90 days.
- **Application data store credentials** — used by: API service; storage: deployment platform secret store; rotation: on incident, otherwise stable.
- **Transactional email provider API key** — used by: API service for the photographer "client finalized" notification; storage: deployment platform secret store; rotation: every 180 days.
- **Delivery-link signing secret** — used by: API service for token integrity; storage: deployment platform secret store; rotation: every 180 days; rotation invalidates outstanding delivery links and is therefore coordinated.
- **Session-cookie signing secret** — used by: API service / web client; storage: deployment platform secret store; rotation: every 180 days; rotation logs photographers out.

No secret is committed in any form (raw, base64-encoded, or otherwise) to this repository or any downstream copy. The pre-commit hook of any actual implementation must include a secret scanner; that is a launch-checklist item ([`launch-checklist.md`](launch-checklist.md) §4).

## 3. Rollout strategy

A new version reaches `production` via a tagged release deployed by the founder. Lead time from `main` merge → `staging` deploy is automated (single-digit minutes). `staging` → `production` is a manual promote action triggered by the founder, typically on a Tuesday or Wednesday morning to avoid weekend incident response. There is no canary infrastructure in v1; the "canary" is launching one photographer at a time during Phase E (per [`plan.md`](plan.md) §5 / [`tasks.md`](tasks.md) E1). Major model or policy changes ([`intelligence-layer.md`](intelligence-layer.md) §8) follow the same path; the eval pass on the golden set is the gate that prevents a model change from reaching `production`.

## 4. Rollback strategy

A bad rollout is reverted by re-promoting the previous tagged release; **maximum acceptable rollback time is 30 minutes** from incident start. Application data store schema changes are forward-compatible by convention (new columns only, never type-changes-in-place); a migration that breaks rollback must be split across two releases. Rollback never suspends or reverses the accepted 90-day storage lifecycle, database purge, or deletion-tombstone controls. **Data implications:** if a release accepted client selections under a new schema column, rolling back can hide those selections from the old application version; the rollback playbook therefore prefers a forward-fix when client selections are at stake and still applies tombstones and current-time expiry before any restored state can receive traffic.

## 5. Observability

The signals the project watches in `production`:

- **API per-route latency and error rate** — covers the photographer surface and the client delivery view; read at the per-route dashboard.
- **AI scoring latency and cost per gallery** — covers the upload-time scoring pass; read at the AI-layer dashboard.
- **AI override rate per gallery and per photographer** — covers the production signal in [`intelligence-layer.md`](intelligence-layer.md) §5; read at the AI-layer dashboard.
- **AI fallback rate (scoring failures)** — covers fallback-path triggering; read at the AI-layer dashboard.
- **Per-photographer monthly cost** — covers the per-photographer ceiling; read at the cost dashboard.
- **Total monthly cost** — covers the system-wide ceiling ([`architecture.md`](architecture.md) §7); read at the cost dashboard.
- **Retention enforcement** — separately monitors storage lifecycle completion, the scheduled application-data purge, tombstone availability/expiry, and restore-time purge verification; any failure is alerting and blocks affected promotion.
- **Email delivery success/failure** — covers the photographer notification; read at the notifications dashboard.

Logs are designed to omit image bytes and identifying metadata at the boundary (per [`intelligence-layer.md`](intelligence-layer.md) §4). Before launch, a future implementation must pass a staging regression test demonstrating that no logging path emits image content.

## 6. On-call and incident response

The founder is solo on-call. Severity-1 (full outage, data leak, retention breach) pages the founder; everything else is dashboard-watched once a day.

- **Pager:** founder's mobile, via the deployment platform's alerting integration.
- **Severity definitions:** **Severity-1** — production unavailable for > 5 minutes; client photo data exposed to an unauthorized party; retention-deletion job failing for > 24 hours. **Severity-2** — a single photographer's gallery is unusable (e.g., scoring stuck) for > 30 minutes; AI provider returning > 50% non-conforming responses. **Severity-3** — degraded performance below targets but loop completes; cosmetic regressions.
- **Response loop:** acknowledge → assess scope → mitigate (rollback if safe, forward-fix if data is at stake) → record the operational incident and run a post-incident review within 48 hours. Add a [`decisions.md`](decisions.md) entry only if that review produces a meaningful accepted choice, exception, deferral, or tradeoff.

This shape is appropriate for a solo founder MVP; if the photographer pool grows past ten, the on-call rotation must be reconsidered as a separate operating decision, not an alternate first-iteration trigger under DEC-8.

## 7. Backups and recovery

The application data store is snapshotted **daily**, with encrypted snapshots retained for 30 days. Storage lifecycle and the scheduled application-data purge jointly enforce the 90-day rule. Each deletion also creates an opaque tombstone in a retention-control namespace outside the database snapshot lineage; the tombstone remains until every snapshot that could contain the deleted record has expired.

Recovery is tested **once per quarter** by restoring a snapshot to a scratch environment, applying all retained tombstones and current-time expiry, purging affected active and derived records, verifying the result, and only then walking the primary journey. A restored environment cannot be promoted or receive traffic until that sequence succeeds; missing tombstones, purge failure, or failed verification blocks promotion. If a quarter passes without a recovery test, the launch checklist's backup item ([`launch-checklist.md`](launch-checklist.md) §3) regresses and must be addressed before the next release.

## 8. Cost and capacity

Total monthly operating cost target for the initial operating cohort: **≤ $200/month at ≤ 10 active photographers** and their expected gallery volume. This is distinct from the technical capacity envelope of ≤50 photographers / ≤50,000 images per month; cost at that larger envelope is not yet validated. Initial-cohort budget decomposition:

- AI scoring: planning target ≤ $20/month at typical volume (≤$2 per active photographer), with a hard boundary of ≤ $50/month at ten active photographers (≤$5 each), subject to provider and pricing validation ([`intelligence-layer.md`](intelligence-layer.md) §6).
- Object storage: ≤ $40/month for the initial cohort, with 90-day retention bounding the long tail.
- API + data store hosting: ≤ $60/month (single small instance + small managed relational store).
- Email + miscellaneous: ≤ $20/month.
- Contingency: ≤ $60/month at the typical AI target, or ≤ $30/month if AI reaches its hard boundary; either composition remains inside the $200 total.

The **$200/month initial-cohort target** is the operating requalification point: a projection or sustained result above it requires scope and pricing requalification plus an explicit budget decision before expansion. The separate capacity envelope is an unvalidated planning target and requires fresh performance, cost, and architecture validation before use; the AI cost ceiling is the first planned constraint to test (per [`architecture.md`](architecture.md) Optional D).

## 9. Compliance and data handling

These planned controls are illustrative design measures, not a compliance conclusion:

- **No client photos used for AI training** — before integration, checked against the later accepted entry that names the provider and records its dated written commitment; re-review cadence is determined before launch.
- **90-day retention** — checked across storage lifecycle, the scheduled datastore purge, tombstone retention, and restore-time purge (`tasks.md` D1).
- **Accepted on-request deletion treatment** — a future implementation documents and checks the procedure and timing required by qualified review and accepted product policy. Any later automation is deferred work, not an alternate first-iteration trigger under DEC-8.
- **Required privacy, notice, consent, and terms surfaces** — implement and check exactly what qualified review requires (`tasks.md` D2 / [`launch-checklist.md`](launch-checklist.md) §5).
- **Required provider or subprocessor disclosures** — keep current when qualified review requires them and on every provider change.

A real launch requires qualified, jurisdiction-specific review to determine applicable privacy, consumer, contractual, terms, consent, retention, deletion, subprocessor, notice, and other obligations. Regimes such as GDPR or CCPA may be considerations; this artifact does not establish applicability, sufficiency, or categorical exclusions.

---

## Optional sections

### A. Infrastructure-as-code references

Not applicable in v1 of this example. The constitution forbids deployment automation for BuildSolid itself (`framework/docs/constitution.md` §15); this artifact describes a *would-deploy* shape for the downstream photographer SaaS and does not commit to a specific IaC tool. When a real implementation begins, the IaC choice is recorded in [`decisions.md`](decisions.md).

### B. Deploy procedure

The rollout strategy in §3 is self-contained for this planning example. A future implementation must create and review any detailed `ops/runbooks/` material before relying on it; no such runbook is shipped here.

### C. Multi-region strategy

Out of scope for v1. Single-region (per [`architecture.md`](architecture.md) §7); cross-region failover is deferred work, not an alternate first-iteration trigger under DEC-8.

### D. Disaster recovery drills

Quarterly recovery test (§7) is the only DR drill in v1. If the photographer pool grows past ten, the cadence and scope are reconsidered.
