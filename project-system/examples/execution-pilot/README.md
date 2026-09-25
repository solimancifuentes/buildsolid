# Execution and verification pilot

This local pilot shows how a project-specific verifier checks an [accepted compact contract](contract.md) and records coverage in a [feature map](verification/feature-map.md). Its [CLI checker](cli/validate_fixture.py) reads a tiny disposable Git fixture. It does not inspect a BuildSolid installation or replace a project's own checks.

Start with the [verification instructions](verification/SKILL.md). They create a fresh repository in a task-owned temporary directory, then run clean, planted-violation and invalid-root cases. The recipe needs Python 3.10 or newer, Git and a shell. From the checkout root, run the [checker tests](cli/test_validate_fixture.py), which use disposable repositories too:

```sh
python3 -B -m unittest discover -s project-system/examples/execution-pilot/cli -p 'test_*.py' -v
```

The [browser fixture](browser/README.md) covers rendered and interactive states separately. Its healthy route is `browser/`; `?variant=visual` and `?variant=interaction` are deliberate failure controls. The [performance fixture](performance/README.md) compares a synthetic lookup workload with correctness and same-code null controls plus separate profiling. Neither supplies evidence for the CLI criteria, and CLI success does not establish their behavior.

These are synthetic local demonstrations. Record each run's command, exit, Git state and limits in the current task or QA result. The example's feature map starts unverified; it does not claim a customer, production, browser or performance result.
