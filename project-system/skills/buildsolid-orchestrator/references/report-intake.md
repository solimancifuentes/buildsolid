# Manual, channel-neutral report intake

Use this when feedback arrives through a user, issue, review, support channel, document, or other source and the owner or next step is unclear. Intake is an observation and routing step, not acceptance of a fix. Read the actual source when accessible within the task; note its location, date/revision if material, reporter's stated behavior, and any reproduction or artifact. If the source is unreadable or permission-bound, record **unverified source** and route to obtain access or a faithful excerpt. Do not invent its contents or treat a summary as the original.

Compare the report with accepted behavior and current project state. Check whether the behavior is already documented, an existing task/known issue covers it, a prior fix is pending or merged, and whether the reporter's evidence is current. Preserve links to existing work and its status. Distinguish:

| Route | Evidence needed | Next owner |
|---|---|---|
| New bug | Reproducible or credible deviation from accepted behavior, with affected surface and current status. | Existing Project Change impact/accepted task; QA or investigator may establish mechanism. |
| Duplicate | Same underlying issue and scope as an existing current item. | Existing owner; add new evidence there if useful. |
| Possible duplicate | Similar symptoms but identity or scope is unproved. | Bounded investigation before merging records or closing a report. |
| Feature request | Requested behavior is new or changes accepted intent. | Spec/scope owner and applicable acceptance gate before implementation. |
| Question | Clarification or usage request without established defect/change. | Answer from current accepted guidance; record a gap only if persistent. |
| Wrong owner | Evidence points to a different project, component, or external provider. | Name likely owner and uncertainty; do not silently assign or send externally. |
| Uncertain | Source, expected behavior, reproduction, or ownership is insufficient. | State the cheapest discriminating check and who can perform it. |

Return a compact intake note in the current task or review: source and readability, observed claim versus inference, relevant accepted behavior, evidence and freshness, existing work checked, route/owner, uncertainty, and next step. Create or update `known-issues.md` only for a persistent bug, gap, or accepted debt; ordinary same-task reports remain in task/review provenance. A material change to accepted intent follows the normal Stage 13 or Existing Project Change route and its human gate. Intake does not create a ticket, message a reporter, edit product code, accept a feature, or close existing work automatically. An authorized human or owning workflow may later choose those actions under its own scope.

Illustrative distinctions: “The login error now omits its retry link” plus a current reproduction against an accepted retry-link criterion is a **new bug** unless an existing task already owns that same cause. “Login is broken too” near an open login issue is only a **possible duplicate** until mechanism or reproduction matches. A link that the agent cannot open stays **uncertain/unverified source**, even if its title sounds like a bug.
