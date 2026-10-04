# Evidence and acceptance

Evidence is chosen by changed surface and risk, not by a universal checklist. Preserve a concise baseline of known failures before editing; distinguish pre-existing failures from regressions. Cite exact commands, selected cases, exit status, environment/input identity, artifact/build identity, and observed result where material. A log or hash identifies an artifact; it does not prove its semantics.

| Surface | Minimum relevant proof |
| --- | --- |
| Documentation/governance | Links, registry consistency, examples, and human review of contradictions and claims. |
| Library/CLI | Targeted tests plus affected contract/integration paths; actual invocation when usability is claimed. |
| Application | Build/tests plus ordinary startup and the requested user path. A process existing or a smoke mode running is not normal-launch acceptance. |
| Visual/client review | Settled real-browser or device observation on the exact integrated build, role, route, viewport, and state. Privacy-safe capture if needed. Source-only rendering or a stale screenshot is insufficient. |
| External integration | Permission scope, read/write boundary, target account/environment, reversible test, live response where authorized, and limits. A mock proves only the local contract. |
| Release/distribution | Explicit channel and unique artifact/build identity, tested installed/runtime artifact, migration/rollback, and separately verified production state. Main-branch code or a green CI run is not deployed proof. |

Before cleanup, classify generated files as disposable cache, build input, runtime dependency, evidence artifact, or rollback artifact. Trace ordinary launch dependencies; removing `dist` or another generated tree may break a packaged application. Destructive cleanup needs exact targets and post-cleanup verification. Keep private data out of screenshots and logs.

Acceptance must name the user-visible behavior and evidence level: local, browser/device, integrated branch, installed artifact, or production. Do not merge these into a single “done” percentage. For finite client-review ledgers, keep the original denominator and show each annotation's disposition; new or superseded requests get explicit lineage rather than silently shrinking the set.
