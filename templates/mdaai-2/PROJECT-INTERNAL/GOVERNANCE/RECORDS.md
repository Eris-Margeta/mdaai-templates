# Tasks, records, recovery, and supersession

## One state source

[TASKS.json](../MANAGEMENT/TASKS.json) is the only machine-readable task/status source. Project Elaboration owns planned scope and order; it must not duplicate checkboxes or task states. Each task has a stable `M20-NNN`-style ID (minimum three digits, no maximum), owner, scope reference, acceptance criteria, lifecycle state, scheduling disposition, evidence, blocker, next action, and transition history. An adopting project may choose its own prefix, but must retain a single stable ID grammar and registry.

Lifecycle states: `proposed`, `active`, `blocked`, `complete`, `void`. Scheduling disposition: `current` or `deferred`; it is independent of lifecycle state. `blocked` requires an actual blocker. `complete` requires evidence for every acceptance criterion or a precise explanation of a partial claim; a partial task should normally remain nonterminal. `void` requires a reason. Nonterminal tasks require a useful next action. A deferred entry stays visible and nonterminal until authorized, resolved, or voided; deferral never grants execution authority.

Use local evidence references when possible; an external reference is a locator, not proof that its content remains available or correct. A completion claim must distinguish the level of evidence (structural, unit, integrated, ordinary runtime, real browser/device, deployed) in its result text. The validator checks shape and links, not truth.

Update an active task and any linked active record as evidence evolves. Append a concise transition entry on lifecycle/disposition changes. Once a record has a coherent terminal result, preserve its content; correct material errors with a linked new record. This freeze is about audit meaning, **not** a required Git commit. The canonical registry may add a link to a subsequent correction without erasing the original transition. A later discovered defect gets its own task and must be reflected in current acceptance reporting; historical “complete” is not proof of perpetual product correctness.

## Optional durable records

Do not create a WO, CWO, checkpoint, or repeated status document for routine edits, red tests, or tool feedback. Use the task entry and linked test/log/artifact first. Create a short record only when a material decision, defect cause, review round, external effect, or handoff needs durable context. Record: ID/date, owner, bounded scope, decision or mechanism, evidence/result/limits, next action, and supersession link as applicable. Omit inapplicable fields. ADRs record architecture tradeoffs; review ledgers preserve individual client annotations and human supersession. No record template can override current authorization.

## Recovery and supersession

Resume from nonterminal registry entries relevant to the current request, their linked evidence, and the current working tree/runtime—not from an unbounded history replay. Reconcile stale or contradictory records before declaring recovery complete. Do not automatically execute all deferred work. Preserve withdrawn/superseded knowledge with a pointer to the replacement; supersession is about guidance, not scheduling. Use the smallest affected unit and prevent replacement cycles. A handoff, record creation, or green build alone is not completion.
