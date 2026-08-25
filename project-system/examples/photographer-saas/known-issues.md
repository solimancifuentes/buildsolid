# Known Issues — Photographer SaaS

Running list of **current bugs, gaps, and intentional debt** in the example. Read by anyone landing on the project, anyone preparing to ship, and anyone planning the next iteration.

> **Stop-point notice (per [`README.md`](README.md) §1).** This is a BuildSolid reference example. The product itself has not been built; the entries below capture the gaps and intentional debt **the example walkthrough surfaced** about the *would-build*. They are concrete enough to belong in this artifact, while remaining honest that no live bugs exist because no live system exists.

> **Synthetic-scenario notice.** The people, research, dates, measurements, galleries, tests, and operating outcomes in this worked example are synthetic and illustrative. The entries below are planned gaps and debt, not observed production defects or completed legal, privacy, or security conclusions.

Related artifacts: [`spec.md`](spec.md), [`tasks.md`](tasks.md), [`decisions.md`](decisions.md), [`changelog.md`](changelog.md), [`launch-checklist.md`](launch-checklist.md).

---

## How to read this file

Entries are grouped by **category**: bugs, gaps, intentional debt. Within each category, entries are sorted by **severity** (highest first). Each entry uses this shape:

```
### <ID> — <Title>
**Category:** Bug / Gap / Intentional debt
**Severity:** Critical / High / Medium / Low
**Status:** Open / In progress / Accepted / Resolved
**Discovered:** <YYYY-MM-DD>
**Description:** <one short paragraph>
**Workaround:** <one line, or "none">
**References:** <links to tasks, decisions, prior changelog entries>
```

ID format: `KI-N`. Severity: **Critical** blocks shipping or causes data loss; **High** blocks a key journey or violates a stated commitment; **Medium** affects a non-key journey or has a viable workaround; **Low** cosmetic.

---

## Bugs

> No live bugs — no live system. This section will populate during Phase B onward when the implementation begins. The shape below is held empty as a forward-reference for downstream readers; if you are reading this on a real project, replace this paragraph with real bug entries.

---

## Gaps

### KI-1 — Per-style AI weighting not present in v1

**Category:** Gap
**Severity:** Medium
**Status:** Accepted
**Discovered:** 2026-04-27
**Description:** The planned v1 uses one neutral scorer across the selected event-and-portrait shoot types under DEC-1 as clarified by DEC-11. Per-style weighting remains deferred and is reconsidered only if DEC-8's accepted override-rate trigger fires.
**Workaround:** Photographer overrides every suggestion they disagree with on Screen 2; production override-rate dashboard ([`intelligence-layer.md`](intelligence-layer.md) §5) tracks the signal.
**References:** [`decisions.md`](decisions.md) DEC-1, DEC-8, DEC-11; [`intelligence-layer.md`](intelligence-layer.md) §2.

### KI-2 — Photographer-deletion-on-request is manual

**Category:** Gap
**Severity:** Medium
**Status:** Accepted
**Discovered:** 2026-04-27
**Description:** A future downstream implementation may initially handle photographer-requested deletion through a founder-run runbook. The example makes no categorical deletion-deadline or legal-sufficiency claim; qualified, jurisdiction-specific review must determine the applicable request process and timing.
**Workaround:** Before real use, document and rehearse the required runbook with synthetic data, then implement any treatment required by qualified review.
**References:** [`deployment.md`](deployment.md) §9; [`launch-checklist.md`](launch-checklist.md) §5.

### KI-3 — Specific AI provider remains unresolved

**Category:** Gap
**Severity:** High
**Status:** Open
**Discovered:** 2026-04-27
**Description:** DEC-4 requires a later append-only accepted entry that names the provider and dates its written no-retention/no-training commitment. No provider has been selected; [`tasks.md`](tasks.md) C1 is therefore `Blocked` and no provider integration may begin.
**Workaround:** The manual loop may be developed and exercised with synthetic fixtures only; no provider call is permitted.
**References:** [`decisions.md`](decisions.md) DEC-4, DEC-11; [`tasks.md`](tasks.md) C1; [`intelligence-layer.md`](intelligence-layer.md) §2, §4.

### KI-4 — Single-region deployment

**Category:** Gap
**Severity:** Low
**Status:** Accepted
**Discovered:** 2026-04-27
**Description:** v1 deploys to a single region. Photographers and clients outside that region may see additional latency on the client surface. Cross-region failover remains deferred and is not an alternate Stage-13 trigger under DEC-8.
**Workaround:** Region chosen to cover the founder's pre-committed photographer audience (North America).
**References:** [`architecture.md`](architecture.md) §7; [`deployment.md`](deployment.md) §1.

### KI-5 — Recovery test is quarterly, not monthly

**Category:** Gap
**Severity:** Low
**Status:** Accepted
**Discovered:** 2026-04-27
**Description:** [`deployment.md`](deployment.md) §7 calls for a quarterly recovery test. A solo founder can absorb that cadence; a team would test more frequently. If the photographer pool grows past ten, the cadence should be reconsidered.
**Workaround:** Calendar reminder; quarterly test gate in [`launch-checklist.md`](launch-checklist.md) §3.
**References:** [`deployment.md`](deployment.md) §7.

---

## Intentional debt

### KI-6 — No general-purpose worker farm; scoring and purge remain application-owned

**Category:** Intentional debt
**Severity:** Medium
**Status:** Accepted
**Discovered:** 2026-04-27
**Description:** Upload-time scoring remains dispatched by the API service. One provider-neutral daily trigger may invoke the idempotent application-owned 90-day purge; that narrow trigger is not a general-purpose worker tier.
**Workaround:** Keep both operations bounded and observable; any broader recurring-work platform requires a later accepted architecture decision.
**References:** [`decisions.md`](decisions.md) DEC-3, DEC-11, DEC-12; [`tasks.md`](tasks.md) D1; [`architecture.md`](architecture.md) §3.

### KI-7 — Web-only client; no native mobile

**Category:** Intentional debt
**Severity:** Medium
**Status:** Accepted
**Discovered:** 2026-04-27
**Description:** The worked scenario uses the responsive web client for mobile access. Mobile-web may be worse than a native app on certain interactions. A native app remains deferred; DEC-8's accepted first-iteration trigger concerns sustained scorer override rate, not mobile delivery.
**Workaround:** Responsive design tuned for tablet first; mobile-web second ([`design.md`](design.md) §3 / Optional D).
**References:** [`decisions.md`](decisions.md) DEC-2; [`non-goals.md`](non-goals.md) §1.

### KI-8 — CSV export contains filenames only, not AI labels

**Category:** Intentional debt
**Severity:** Low
**Status:** Accepted
**Discovered:** 2026-04-27
**Description:** The CSV export deliberately omits AI labels (DEC-7). Photographers who want labels for their own bookkeeping have to copy them from Screen 2 manually. Keeping the export shape stable was preferred over baking AI internals into the photographer's downstream tools.
**Workaround:** Photographers can manually note labels during Screen 2 review.
**References:** [`decisions.md`](decisions.md) DEC-7; [`design.md`](design.md) §4.

---

## Resolved (archive)

### KI-9 — Task backlog omitted status fields

**Category:** Gap
**Severity:** Low
**Status:** Resolved
**Discovered:** 2026-07-03
**Resolved:** 2026-07-03
**Description:** A compatibility review found that this accepted reference backlog omitted the `Status` field required by the Stage 9 implementation-support procedure. The omission made fresh-agent implementation state less reconstructable from tracked artifacts.
**Workaround:** None needed after the local correction; every task now carries an allowed status. C1 is `Blocked` by the unresolved provider entry and the other 26 tasks are `Not started`; no implementation task is `In progress` or `Done`.
**References:** [`decisions.md`](decisions.md) DEC-10; [`plan.md`](plan.md) §5; [`tasks.md`](tasks.md).

---

## Optional sections

### A. Triaging cadence

In a future real implementation, the founder reviews this file **once a week on Friday** during the launch month, then **once every two weeks** afterward. New entries from production are added as the founder finds them; the override-rate dashboard ([`intelligence-layer.md`](intelligence-layer.md) §5) is one possible source of persistent gap entries.

### B. Severity-1 response policy

Covered in [`deployment.md`](deployment.md) §6. Incidents first use the operational incident record. Open a `KI-N` only when triage establishes a persistent or material bug, gap, or debt item; severity alone does not force a duplicate entry here.

### C. Issue intake from outside the project

In a future real implementation, reports are triaged through the named support channel. Create a `KI-N` only for a persistent or material bug, gap, or debt item; routine questions, duplicates, and transient incidents remain in their owning support or incident record.
