# Changelog — Photographer SaaS

The project's running record of **what shipped and when**. Readable by humans and agents alike. It complements [`decisions.md`](decisions.md): decisions explain *why* things changed; the changelog reports *that* they did.

This is the **project-level** changelog for the example. It is **not** BuildSolid's own changelog (`CHANGELOG.md` at the BuildSolid repository root records what shipped in each version of BuildSolid itself).

> **Stop-point notice (per [`README.md`](README.md) §1).** No version of this product has actually been released. The entries below describe what the *would-launch* changelog would look like at the moment v1 ships, plus a brief stage-13 iteration touch under "Unreleased" that demonstrates the constitution's iteration rule (artifacts updated in place; no parallel copies). The scenario, versions, dates, people, research, permissions, checks, and results are synthetic and illustrative.

Related artifacts: [`spec.md`](spec.md), [`tasks.md`](tasks.md), [`decisions.md`](decisions.md), [`known-issues.md`](known-issues.md).

---

## How to read this file

Entries are in **reverse chronological order**: most recent at the top, oldest at the bottom. Each version section follows this shape:

```
## <version> — <YYYY-MM-DD>

### Added
- <…>

### Changed
- <…>

### Fixed
- <…>

### Removed
- <…>

### Security
- <…>

### Notes
- <…>
```

Drop any subsection that has no entries for a given version. Most versions will not need every category. Keep entries to one line each; reference [`tasks.md`](tasks.md) IDs and [`decisions.md`](decisions.md) `DEC-N` IDs for context.

**Versioning.** This project uses CalVer in the form `YYYY.MM.PATCH` per [`plan.md`](plan.md) Optional D.

---

## Unreleased

> Stage-13 iteration touch (per [`decisions.md`](decisions.md) DEC-8). The entries below illustrate how a revisit lands in the changelog **without creating a v2 file**. They are markers for the iteration trigger, not yet shipped.

### Notes

- Iteration trigger: **override rate > 50% sustained across at least three photographers in a calendar week** ([`intelligence-layer.md`](intelligence-layer.md) §5). When fired, [`intelligence-layer.md`](intelligence-layer.md) §2 is updated in place with per-style scoring; [`decisions.md`](decisions.md) DEC-1 is superseded by a forward-link entry; [`mvp-scope.md`](mvp-scope.md) Optional C is updated. No parallel `intelligence-layer-v2.md`. (DEC-8.)
- The shipped reference corpus is wholly synthetic; it is not evidence of interviews, consent, permissions, live checks, or product results.
- DEC-11 clarifies DEC-1 as one neutral scorer across the selected event-and-portrait types and keeps the provider unresolved.
- DEC-12 supplements DEC-5 with out-of-lineage tombstones and mandatory purge-before-restore promotion.

---

## 2026.06.0 — *(planned)*

> Illustrative; the example does not actually ship. Shown so the file's shape is unambiguous.

### Added

- Photographer signup, login, password reset ([`tasks.md`](tasks.md) A2).
- Photographer dashboard with seven-status row view ([`tasks.md`](tasks.md) A3, B7).
- Folder-of-JPEGs gallery upload with resumable transfer ([`tasks.md`](tasks.md) B1).
- Per-frame AI image-suggestion pass at upload time, closed output vocabulary `sharp | eyes-open | composition | duplicate-of-<id>` ([`tasks.md`](tasks.md) C1, C2).
- Photographer review-and-mark UI with per-frame override and reason label visible ([`tasks.md`](tasks.md) B2).
- Token-scoped delivery link, unauthenticated client surface, default-keepers + show-all view ([`tasks.md`](tasks.md) B3, B4).
- Client selection capture and explicit "Finalize" action ([`tasks.md`](tasks.md) B5).
- Transactional email notification to the photographer on client finalize ([`tasks.md`](tasks.md) B6).
- Finalized-selections grid view and CSV export of picked filenames only ([`tasks.md`](tasks.md) B8; DEC-7).
- 90-day client-photo retention with photographer-side per-gallery extension, storage lifecycle deletion, an idempotent scheduled datastore purge, and restore-time tombstone/expiry enforcement before promotion ([`tasks.md`](tasks.md) D1; DEC-5, DEC-12).
- Privacy, notice, consent, terms, and related surfaces required by qualified jurisdiction-specific review ([`tasks.md`](tasks.md) D2).
- Cost-ceiling enforcement at the model-call boundary: $0.20 per gallery, $5.00 per active photographer per month ([`tasks.md`](tasks.md) C4).
- Eval harness against the 300-frame golden set; precision ≥ 0.80, recall ≥ 0.70 required to ship a model or policy change (DEC-6).

### Security

- AI model-call boundary uses an input allow-list (downscaled image bytes + opaque per-frame ID only); a unit test fails if any other field reaches the provider ([`tasks.md`](tasks.md) C1).
- AI output schema validation enforces the closed vocabulary; non-conforming responses fall through to the manual path.
- Logs scrubbed of image bytes and identifying metadata; a future implementation must verify this with a regression test before launch.

### Notes

- The specific v1 AI provider remains unresolved; integration and launch stay blocked until a later accepted entry names it and records the dated written no-retention/no-training commitment (DEC-4, DEC-11).
- v1 runs single-region; multi-region is deferred work, not an alternate first-iteration trigger under DEC-8.
- v1 uses one neutral scorer across the selected event-and-portrait shoot types. Per-style weighting is the in-place model/policy assessment named by DEC-8 only after its sole accepted first trigger fires; it is not activated automatically (DEC-1, DEC-8, DEC-11).

---

## Optional sections

### A. Versioning convention

CalVer (`YYYY.MM.PATCH`) per [`plan.md`](plan.md) Optional D. The `MM` segment increments when a new release is cut in a calendar month; `PATCH` increments for in-month follow-ups. The canonical version string lives in this file's heading.

### B. Migration notes

No migrations have shipped. When a future release requires data or configuration migration, the steps will land here as a short subsection per release.
