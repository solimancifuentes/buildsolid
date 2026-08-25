# Changelog — Project template

> **Purpose.** The project's running record of **what shipped and when**. The changelog is the durable answer to "what changed?" — readable by humans and agents alike. It complements [`decisions.md`](decisions.md): decisions explain *why* things changed; the changelog reports *that* they did.
>
> **Workflow phase.** Cross-cutting (Phase 13 — Iteration is where this gets the most use).
>
> **How to use this template.**
> - Replace `<…>` placeholders.
> - Keep blockquoted guidance (`>` lines) only at the top of the file as a how-to-read header; remove or replace before considering the artifact filled.
> - Stable headings — downstream skills rely on the section shape.
> - **Append-only by version.** New work lands in the **Unreleased** section until a version ships, at which point those entries are moved into a dated version section and the **Unreleased** header is preserved with an empty body for the next cycle.
> - **Profile applicability.** This artifact is **Need-triggered** for New Product Build and Existing Project Change when the project uses a durable change log or a release/update is recorded, and **Optional** for Lightweight/Internal Build.
> - **Section depth.** Numbered sections are required when this artifact is Required, Profile-triggered, or Need-triggered for the selected profile; optional sections stay optional unless project facts make them need-triggered.
> - **Semantic readiness.** This artifact is ready only when it records released or unreleased changes in stable categories, preserves historical accuracy, and points to decisions or migration notes when changes matter. Placeholder cleanup alone is not enough.
> - **Reference example fill:** `project-system/examples/photographer-saas/changelog.md`.
>
> **This file is the project-level changelog.** It is **not** BuildSolid's own changelog. BuildSolid's own changelog lives at `CHANGELOG.md` in the BuildSolid repository and records what shipped in each version of BuildSolid itself. Do not record BuildSolid-level releases here.

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

> Drop any subsection that has no entries for a given version. Most versions will not need every category. Keep entries to one line each; reference [`tasks.md`](tasks.md) IDs and [`decisions.md`](decisions.md) `DEC-N` IDs for context.

**Versioning.** This template is neutral on versioning scheme. Use whatever the project committed to in [`plan.md`](plan.md) (semver, calver, or otherwise). State the scheme in §A below if unobvious.

---

## Unreleased

> New work lands here until a version is cut. When a version ships, move these entries into a new dated version section above and reset this section to empty.

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

---

## <version> — <YYYY-MM-DD>

> Replace this template version section with the project's first real release. Then add new versions above this one as they ship.

### Added

- <…>

### Changed

- <…>

### Notes

- <…>

---

## Optional sections

### A. Versioning convention *(optional)*

> One short paragraph naming the project's versioning scheme (semver, calver, build numbers) and where the canonical version string lives. Skip if [`plan.md`](plan.md) §D already covers this.

### B. Migration notes *(optional)*

> If a version requires manual migration (data, configuration, environment), point at the migration steps. Keep the steps short; long migrations belong in their own document linked from here.
