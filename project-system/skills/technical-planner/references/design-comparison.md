# Usage-first design comparison

Use this only when a material architecture choice has more than one plausible shape. It is a method for filling an applicable `architecture.md` or adequate compact section, not a new artifact or a gate for every implementation task.

## Establish use before design

Write one or two concrete consuming examples from accepted intent or current code: caller/actor, input, expected output or side effect, and meaningful failure. Identify the affected interface, data ownership and invariants that each example requires. Separate an illustrative call used to think from an accepted behavior requirement. The latter must come from the owning contract.

Fix comparison criteria before drawing alternatives: correctness against those uses and invariants, actual non-functional constraints, operational cost, maintainability and any task-specific boundary. Name a small exploration budget. A criterion added after seeing a favored sketch is a changed evaluation, not neutral comparison.

Draft independent alternatives when the decision warrants the cost. Separate workers can sketch against the same inputs and criteria; a single agent can sketch sequentially, preserving the first sketch before opening the second. The sequential fallback remains usable but does not claim the independence of separate reviewers. Do not generate variants merely to meet a count.

Compare each option against the same criteria, identify disqualifying invariant violations, then synthesize the smallest defensible shape. Record the selected interface and boundary, why it serves the consuming examples, the losing tradeoff and the cheapest adequate verification. Put durable accepted rationale in the existing architecture/decision owners; scratch sketches remain working context.

## Illustrative, unexecuted comparison

Suppose an accepted project task needs a local status view for one job ID. A caller asks `status_for(job_id)` and expects `ready`, `pending` or `unknown`; an unreadable source must never become `ready`. This example is hypothetical and does not create a BuildSolid product requirement.

Fix criteria first: preserve unknown on incomplete reads, avoid a new persistent service, keep one-call latency proportionate, and let a fresh maintainer explain the state path. One sketch reads and classifies the source on each call; another holds a short-lived in-process snapshot. The first has simpler freshness but repeats reads. The second may lower repeat cost but needs explicit invalidation and risks returning old readiness. Without measured repeat-load pressure, select direct reads and record the caching option as a later hypothesis, not a present requirement. Verify by exercising complete, incomplete and changed-source cases through the public interface. No performance improvement or executed test is claimed here.
