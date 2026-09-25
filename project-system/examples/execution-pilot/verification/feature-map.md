# Pilot feature map

This map links the [pilot contract](../contract.md#acceptance-and-verification) to observable checks. Every row starts **unverified**. Change a status only after recording the actual command, exit or state, tested revision or dirty snapshot, environment, output and verifier in the current task or QA result. Use `inconclusive` when a run cannot distinguish the condition.

| Criterion | Observable check | Current status | Missing evidence |
|---|---|---|---|
| CLI-1 clean index | [Verification §4](SKILL.md#4-outputs) commits the tiny fixture; checker exits 0 and Git status is empty | Unverified | Fresh run and index readback. |
| CLI-2 planted violations | Stage README and skill only; checker exits 1 with three diagnostics; independently read staged blobs and untracked target | Unverified | Fresh run and staged/untracked readback. |
| CLI-3 invalid root | Checker exits 2 for an existing non-repository sibling; nested root also exits 2 | Unverified | Fresh invocation and stderr. |
| BROWSER-1 rendered states | Follow [browser instructions](../browser/README.md) for healthy, expanded and error states plus the visual control | Unverified | Controlled render and screenshots. |
| BROWSER-2 interaction/accessibility | Follow [browser instructions](../browser/README.md) for keyboard, interaction and state changes | Unverified | Actual interaction observations. |

A planted negative that yields the expected diagnostic demonstrates checker sensitivity. It does not establish that the planted repository is valid. Recheck affected rows when the checker, fixture, Git state or rendering environment changes.
