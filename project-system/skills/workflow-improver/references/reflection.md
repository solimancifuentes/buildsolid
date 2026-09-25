# Evidence-based workflow reflection

Start with one observed request and its actual outcome. Preserve the instruction version and invocation context that existed **at the time**, the relevant accepted contract, and a checkable output or action. State what changed for the user or project. Missing traces are unknown, not evidence that an agent ignored an instruction.

Classify the most specific supported cause:

| Classification | Discriminating evidence | Proportionate route |
|---|---|---|
| Missing guidance | The applicable accepted instructions did not describe a material decision the actor had to make. | Propose a narrow instruction or example at the owning source. |
| Trigger miss | Adequate guidance existed, but the invocation or routing path did not select it. | Repair discovery or routing; keep the sound procedure intact. |
| Noncompliance | The actor had applicable guidance and sufficient inputs but demonstrably acted against it. | Correct the task and examine whether a clearer, testable instruction would prevent recurrence. |
| One-off error | Guidance and trigger worked, but this execution failed through a local slip or transient condition. | Repair within the task; do not infer a general policy gap. |

Use “inconclusive” when access to the instruction context, output, or causal path is missing. Check alternative causes, such as changed accepted intent, stale context, an unavailable tool, or a misleading test. State recurrence only from independent comparable observations; one case may support a targeted repair but not a claim of frequency. Recommend a reusable change when it would alter a decision at the demonstrated failure point, then identify the owning artifact and a realistic case that should improve. Preserve existing work and report any acceptance change separately.

Example (illustrative, not executed evidence): an agent answers a deployment question without opening the deployment skill. If the skill contains the needed procedure and the router did not select it, classify a **trigger miss**. If a trace instead shows the skill loaded and a required check skipped, revisit as **noncompliance**. If no trace reveals what was loaded, keep the cause **inconclusive**. The same output alone cannot establish all three.
