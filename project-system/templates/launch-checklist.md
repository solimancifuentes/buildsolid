# Launch Checklist — Project template

> **Purpose.** When the project has an actual launch or readiness event, list the things that must all be **true** before that event occurs. Launch is the moment the project becomes accountable to people outside the team — this checklist is what prevents the easy mistakes from happening on launch day.
>
> **Workflow phase.** Phase 12 — Launch Prep.
>
> **Driving skill.** `launch-prep`.
>
> **How to use this template.**
> - Replace `<…>` placeholders.
> - Keep blockquoted guidance (`>` lines) while drafting; remove or replace before considering the artifact filled.
> - Stable headings — downstream skills rely on them.
> - **Every included item is binary.** If you cannot say "yes, this is true," it is not done. Include only checks that apply to the actual launch or readiness event; an unresolved required check is a blocker, not N/A.
> - **Profile applicability.** This artifact is **Required** for New Product Build, **Conditional** for Existing Project Change, and **Need-triggered** for Lightweight/Internal Build. Create or update it only for an actual user-facing launch, communication, metrics, or readiness event.
> - **No N/A-only artifact.** If launch prep does not apply, record a material exclusion in the owning compact applicability record when needed; do not create this checklist solely to say N/A. An existing `N/A - reason: <reason>` launch checklist remains valid. In an otherwise applicable checklist, a numbered section that is materially inapplicable may use that same specific token after its checks are removed.
> - **Section depth.** When this artifact applies, keep every numbered stable heading and include the checks relevant to the actual event. Use a specific `N/A - reason` only for a materially inapplicable section; optional sections stay optional unless project facts make them need-triggered.
> - **Semantic readiness.** Where launch applies, this artifact is ready only when every applicable product, intelligence-layer, infrastructure, security, privacy, communication, metrics, operations, and unresolved-decision check is complete, with any material in-file omission explained by a specific `N/A - reason`. Placeholder cleanup alone is not enough. Checklist completion is evidence of readiness, not authority to launch; the human must authorize any irreversible or high-impact launch action.
> - **Reference example fill:** `project-system/examples/photographer-saas/launch-checklist.md`.

Related artifacts: [`spec.md`](spec.md), [`mvp-scope.md`](mvp-scope.md), [`architecture.md`](architecture.md), [`intelligence-layer.md`](intelligence-layer.md), [`deployment.md`](deployment.md), [`decisions.md`](decisions.md).

---

## 1. Product

> The product itself works for the journeys named in [`user-journeys.md`](user-journeys.md).

- [ ] All MVP journeys ([`user-journeys.md`](user-journeys.md)) complete end-to-end without manual intervention.
- [ ] All [`spec.md`](spec.md) §10 acceptance criteria are checked.
- [ ] Empty / loading / error states are handled for each key screen ([`design.md`](design.md)).
- [ ] <project-specific item>.

## 2. Intelligence layer

> If the project has an intelligence layer ([`intelligence-layer.md`](intelligence-layer.md)), it must be evaluated and bounded before launch. If the project has no load-bearing AI layer, this section is a material in-file omission: write `N/A - reason: no load-bearing AI layer` and remove the items.

- [ ] Eval pass on the golden set is at or above the project's commitment ([`intelligence-layer.md`](intelligence-layer.md) §5).
- [ ] Fallbacks for every capability are tested and observable.
- [ ] Cost ceiling is configured and alerted on ([`intelligence-layer.md`](intelligence-layer.md) §6).
- [ ] Safety boundaries are checked ([`intelligence-layer.md`](intelligence-layer.md) §7).

## 3. Infrastructure and deployment

> The deployment is rehearsed, not improvised on the day.

- [ ] Production deploy procedure ([`deployment.md`](deployment.md) §3) has been exercised end-to-end.
- [ ] Rollback procedure ([`deployment.md`](deployment.md) §4) has been exercised end-to-end.
- [ ] Secrets are in their canonical store ([`deployment.md`](deployment.md) §2) — none committed to the repository.
- [ ] Backups configured and a recovery test passed ([`deployment.md`](deployment.md) §7).
- [ ] Observability dashboards are populated and read by the on-call ([`deployment.md`](deployment.md) §5).

## 4. Security

> A security pass has been done — not aspirationally, actually.

- [ ] Security review against the project's threat model has been completed.
- [ ] Authentication / authorization works for the supported user roles.
- [ ] No high or critical issues open at launch.
- [ ] Logs do not contain secrets, credentials, or sensitive user data.
- [ ] Third-party dependencies are at supported versions.

## 5. Privacy and compliance

> If the project handles user data of any kind, state the commitments and verify them.

- [ ] Privacy policy is written, current, and linked from the product.
- [ ] Data retention rules ([`deployment.md`](deployment.md) §9, [`intelligence-layer.md`](intelligence-layer.md) §4) are implemented and tested.
- [ ] Compliance commitments (regulatory regimes named in [`spec.md`](spec.md) / [`architecture.md`](architecture.md) / [`intelligence-layer.md`](intelligence-layer.md)) are met.
- [ ] Users can request data export and deletion (if committed).

## 6. Communications

> The launch reaches the right people in a way that lets them succeed.

- [ ] Landing page or first-impression surface is live.
- [ ] First-user list (or first-user channel) is identified and notified.
- [ ] Support channel is staffed and named in the product.
- [ ] First 24-hour response plan is agreed.

## 7. Metrics

> The project will know, on the day, whether the launch worked.

- [ ] Activation metric is defined ([`mvp-scope.md`](mvp-scope.md) §4) and instrumented.
- [ ] Failure metric is defined ([`mvp-scope.md`](mvp-scope.md) §5) and instrumented.
- [ ] Success and failure thresholds are stated in advance.
- [ ] Dashboard exists where the founder can read both within minutes.

## 8. Operations and on-call

> The first hours after launch are owned, not improvised.

- [ ] On-call is staffed for the launch window ([`deployment.md`](deployment.md) §6).
- [ ] Severity definitions and response loop are documented.
- [ ] At least one practiced incident drill has happened.
- [ ] Status page or status communication channel is identified.

## 9. Decisions and open questions

> Every launch-affecting decision is logged, and every blocker is named.

- [ ] All launch-blocking items in [`decisions.md`](decisions.md) are resolved.
- [ ] All launch-blocking items in [`known-issues.md`](known-issues.md) are either fixed or accepted with a documented mitigation.
- [ ] Post-launch iteration plan exists (where the project goes in the first week after launch).

---

## Optional sections

### A. Marketing assets *(optional)*

> Page copy, screenshots, and posts the launch needs. Skip if launch is private or invite-only.

### B. Legal and contracts *(optional)*

> Terms of service, payment processor agreements, partner contracts. Skip if none apply at MVP.

### C. Post-launch monitoring rota *(optional)*

> Who watches what for the first 1–7 days after launch. Useful for solo founders to plan recovery time around the watch window.

### D. Rollback decision tree *(optional)*

> A short decision tree for "when is rolling back the right call?" Helps prevent decision paralysis under pressure.
