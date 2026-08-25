# AGENTS.md — Working with the public BuildSolid tree

This file is agent-neutral guidance for the standalone public BuildSolid package. It is navigation and working policy, not a replacement for the Framework constitution.

## Read first

Before substantive work, read only the material relevant to the task, in this order:

1. `README.md`
2. this `AGENTS.md`
3. `framework/README.md`
4. `framework/docs/constitution.md`
5. `framework/docs/context-package.md`
6. `framework/docs/brand/BUILD_SOLID_CANONICAL.md`
7. the relevant skill, template, or reference-example files under `project-system/`
8. `CONTRIBUTING.md` or `SECURITY.md` when the task touches feedback, contribution, or vulnerability reporting

## Authority and boundaries

- Framework owns normative BuildSolid meaning.
- Project System packages, instantiates, and demonstrates Framework without redefining it.
- Root wrappers route the public package and do not override Framework.
- Git-tracked human-readable Markdown is the accepted knowledge surface.
- An untagged commit is a candidate. Released authority belongs only to the exact commit selected by the matching annotated `v0.5.0` tag.
- A proposal, issue, review, validation result, or prior action does not grant a later effect by implication.

## Working rules

- Preserve the fourteen stages, three profiles, four modes, fourteen skills, twenty templates, artifact vocabulary, quality standards, compact-lifecycle semantics, and reference-example behavior unless an authorized change explicitly says otherwise.
- Prefer editing accepted artifacts in place. Do not create parallel versions or silently promote proposed knowledge.
- Keep capabilities Markdown-first, skill-first, portable, and usable by one competent agent from a normal checkout.
- Do not introduce a product CLI, API, package, service, database, hosted platform, deployment automation, project generator, or required provider-specific runtime by implication.
- Ask only when a missing choice materially changes scope, authority, or outcome. Preserve human control for high-impact or irreversible actions.
- Validate the narrowest relevant invariants and the complete changed surface before presenting work as complete.

## Feedback, contributions, and security

GitHub Issues are available for feedback. External code and content contributions are not accepted initially, and unsolicited pull requests will be closed; follow `CONTRIBUTING.md`.

Do not report a vulnerability in an Issue or pull request. Use the repository's private GitHub Security reporting interface described in `SECURITY.md`.
