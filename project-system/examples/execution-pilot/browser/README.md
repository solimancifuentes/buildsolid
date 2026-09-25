# Verification card browser fixture

This tiny local page is an illustrative BuildSolid verification fixture, not a product or released visual baseline. It has no external assets, account, network calls, animation, random values or time-based state. Use an 800 × 600 viewport, 100% browser zoom, light color scheme and the same browser/OS font environment for every comparison. The CSS uses local monospace fonts; record the resolved font if comparing images across machines.

## Frozen expected behavior

| State | URL and action | Expected observation |
|---|---|---|
| Default | `/browser/` after load | Centered white bordered card; heading “Verification card”; green-tinted summary “Ready to review. Three checks are waiting for your inspection.”; Details button has `aria-expanded="false"`; detail panel hidden; labeled Run label input and Submit run button visible. |
| Expanded | Default page, activate Details by click or keyboard Enter/Space | Detail panel becomes visible with “Inspect the expected layout, keyboard behavior, and form feedback.”; button has `aria-expanded="true"`. A second activation closes it. |
| Empty/error | Default page, leave Run label empty and submit by click or keyboard Enter | Visible `role="alert"` reads “Enter a run label.” in red; the page does not navigate. |
| Filled/success | Enter `pilot-1` and submit | Feedback reads “Run queued: pilot-1” in green; the page does not navigate. |

These expectations are fixed before measurement. The two query variants are **intentional negative controls**, not alternate acceptable baselines:

- `/browser/?variant=visual` clips the entire green summary, removing meaningful readiness content. The default summary above remains expected; a screenshot comparison should flag this visual regression.
- `/browser/?variant=interaction` disables the native Details button. Mouse and keyboard users cannot expand the panel; keyboard focus skips the disabled control. This fails the default interaction and accessibility expectation even if a static screenshot looks similar.

Use the default page for the reference capture. Capture default, expanded and error states at the frozen viewport, then load each negative-control URL from a fresh page and repeat the relevant check. Record actual screenshots, keyboard focus/activation observations and `aria-expanded` state. Do not replace the default expectation with a defect variant to make it pass.

## Loopback-only serving

From the repository root, in a shell you control:

```sh
python3 -m http.server 8765 --bind 127.0.0.1 --directory project-system/examples/execution-pilot >/dev/null 2>&1 &
browser_fixture_pid=$!
```

Open `http://127.0.0.1:8765/browser/` and its `?variant=visual` and `?variant=interaction` forms. If port 8765 is occupied, choose an unused loopback port and record it with the evidence. When finished, stop only the process whose PID this shell captured:

```sh
kill "$browser_fixture_pid"
wait "$browser_fixture_pid" 2>/dev/null
```

The browser and server are optional tools for exercising this example. The accepted behavior is stated here in Markdown and can be inspected without a BuildSolid service or generator.
