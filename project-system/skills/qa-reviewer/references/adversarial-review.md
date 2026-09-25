# Evidence-based adversarial review

Use this procedure for a change whose behavior, security boundary or evidence warrants a focused challenge. It supports `qa-reviewer` and `security-reviewer`; it does not require a panel, fixed finding count or extra approval gate. The applicable accepted contract and current code/evidence remain authoritative.

## Frame the review

Name the reviewed revision or dirty snapshot, affected task and acceptance criteria, direct files and indirect consumers, critical invariants, and the reviewer lens. Freeze expected behavior before probing it. Select a bounded route through realistic inputs and states; reading a diff alone may miss an indirect caller, while an unreachable concern is not a defect in the shipped path.

For each candidate finding, record:

- the exact claim and affected accepted criterion or invariant;
- a concrete entry point, conditions and path to the disputed behavior;
- current file/line or artifact identity plus observed command, test, trace or manual state;
- expected versus actual result, impact and severity, with uncertainty separated from facts;
- a minimal countercheck that could disprove the claim.

The lead tests reachability and the countercheck, then records **valid**, **false positive** or **inconclusive** with a reason. A reviewer may be wrong even when several reviewers agree; a valid singleton finding remains valid when its path and impact are demonstrated. A plausible claim is rejected when a tested guard, unreachable path or contrary current behavior disproves it. Inconclusive claims stay open with the next evidence needed; they are not silently counted as passed or failed. Recheck after a relevant repair and preserve the original observation in ordinary task/review provenance.

Reviewers can work independently on disjoint lenses and then compare evidence. With one agent, run a first pass and a separate countercheck sequentially; do not present that as independent multi-agent agreement. Escalate only an actual missing authority, material acceptance change or consequential effect under the governing contract. No majority threshold or finding quota determines correctness.

## Evidence boundary

An assertion such as “this looks vulnerable” or “tests are green” is a lead, not a verdict. Static reasoning can establish a finding when the path and conditions are concrete; execution is preferable where safe and necessary to settle reachability. Never alter the accepted expected behavior, test baseline or severity solely to make the review pass. Review may inspect incomplete implementation without labeling it complete, and neither a review verdict nor a passed check authorizes merge or deployment.

This reference describes a method only. Seeded findings and actual adjudication belong in the owning task's evidence, not in reusable guidance; no specific finding is claimed here.
