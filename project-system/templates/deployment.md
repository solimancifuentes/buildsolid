# Deployment — Project template

> **Purpose.** When the project ships to an environment, changes operations, or affects rollout or recovery, describe **how it ships and runs**: environments, secrets, rollout, rollback, and on-call basics. Deployment is a designed concern, not an afterthought. This artifact is agent-neutral; it does not assume a specific cloud, framework, or CI/CD platform unless the project has explicitly chosen one in [`decisions.md`](decisions.md).
>
> **Workflow phase.** Phase 11 — Deployment.
>
> **Driving skill.** `deployment-manager` (planning artifact only — BuildSolid does not automate deployment in v0.1).
>
> **How to use this template.**
> - Replace `<…>` placeholders.
> - Keep blockquoted guidance (`>` lines) while drafting; remove or replace before considering the artifact filled.
> - Stable headings — downstream skills rely on them.
> - **Agent-neutral.** State concrete platform / tool choices as decisions in [`decisions.md`](decisions.md), not as templates assumptions.
> - **Profile applicability.** This artifact is **Required** for New Product Build, **Conditional** for Existing Project Change, and **Need-triggered** for Lightweight/Internal Build. Create or update it only when the applicable lifecycle slice includes deployment because the project ships to an environment, changes operations, or affects rollout/recovery.
> - **No N/A-only artifact.** If deployment does not apply, record a material exclusion in the owning compact applicability record when needed; do not create this file solely to say N/A. An existing `N/A - reason: <reason>` deployment artifact remains valid. In an otherwise applicable artifact, a numbered section that is materially inapplicable may use that same specific token; unresolved deployment work is not N/A.
> - **Section depth.** When this artifact applies, keep every numbered stable heading and complete each applicable section. Use a specific `N/A - reason` only for a materially inapplicable section; optional sections stay optional unless project facts make them need-triggered.
> - **Semantic readiness.** Where deployment applies, this artifact is ready only when it covers environments, secrets, rollout, rollback, observability, incident response, recovery, cost/capacity, and compliance, with any material in-file omission explained by a specific `N/A - reason`. Placeholder cleanup alone is not enough, and readiness does not authorize a deployment; human confirmation remains required for irreversible or high-impact deployment actions.
> - **Reference example fill:** `project-system/examples/photographer-saas/deployment.md`.

Related artifacts: [`architecture.md`](architecture.md), [`intelligence-layer.md`](intelligence-layer.md), [`spec.md`](spec.md), [`launch-checklist.md`](launch-checklist.md), [`decisions.md`](decisions.md).

---

## 1. Environments

> The environments the project ships through. Typical: `dev` (local), `staging` (shared, pre-prod), `production`. For each: purpose, who has access, where data comes from. If the project ships a single environment, say so explicitly.

- **<environment>** — purpose: <…>; access: <…>; data source: <…>.
- **<environment>** — purpose: <…>; access: <…>; data source: <…>.

## 2. Secrets and credentials

> One short paragraph plus a bullet list. Where secrets live, how they are rotated, and what each is used for. **Never store secrets in this file or anywhere in the repository.** This section names the secrets and points at where they actually live (a secret manager, environment variables, a hosted vault).

<…>

- **<secret name>** — used by: <…>; storage: <…>; rotation: <…>.
- **<secret name>** — used by: <…>; storage: <…>; rotation: <…>.

## 3. Rollout strategy

> One short paragraph. How a new version reaches production: direct deploy, blue/green, canary, feature-flagged. Include the typical lead time and who triggers the rollout.

<…>

## 4. Rollback strategy

> One short paragraph. How to revert a bad rollout. State the maximum acceptable rollback time and what data, if any, would be lost. **If rollback has data implications, name them explicitly.** A rollback strategy that pretends data is reversible when it is not is worse than no plan.

<…>

## 5. Observability

> Bullet list. The signals the project watches in production: logs, metrics, traces, AI-layer evals, error reports. For each: what it covers and where it is read.

- **<signal>** — covers: <…>; read at: <…>.
- **<signal>** — covers: <…>; read at: <…>.
- **<signal>** — covers: <…>; read at: <…>.

## 6. On-call and incident response

> One short paragraph plus a bullet list. Who is on-call, what counts as an incident, and the basic response loop. For a solo founder MVP, "the founder gets paged for severity-1, otherwise watches dashboards once a day" is a valid answer — but it must be stated explicitly.

<…>

- **Pager:** <…>.
- **Severity definitions:** <…>.
- **Response loop:** <…>.

## 7. Backups and recovery

> One short paragraph. What is backed up, how often, and how recovery is tested. If the project has no persistent data, write `N/A - reason: stateless project with no persistent data`.

<…>

## 8. Cost and capacity

> One short paragraph. The expected operating cost at MVP scale, the cost ceiling, and the capacity envelope (concurrent users, request rate). Cross-references [`architecture.md`](architecture.md) §7 and [`intelligence-layer.md`](intelligence-layer.md) §6 for AI-layer cost.

<…>

## 9. Compliance and data handling

> One short paragraph plus a bullet list. Any regulatory regime in scope (GDPR, HIPAA, SOC 2, etc.) and how deployment respects it. State concrete commitments — not aspirations.

<…>

- **<commitment>** — checked by <…>.
- **<commitment>** — checked by <…>.

---

## Optional sections

### A. Infrastructure-as-code references *(optional)*

> If the project's infrastructure is defined as code (Terraform, Pulumi, etc.), point at the directory or repo. Otherwise skip this optional section; use `N/A - reason: <reason>` only when that in-file omission needs a durable explanation.

### B. Deploy procedure *(optional)*

> A short, stable description of the deploy procedure that a new operator can follow. Skip if the rollout strategy in §3 is already self-contained.

### C. Multi-region strategy *(optional)*

> If the project deploys to multiple regions, describe failover and consistency. Skip for single-region MVPs.

### D. Disaster recovery drills *(optional)*

> The cadence and shape of DR drills. Cross-references [`launch-checklist.md`](launch-checklist.md).
