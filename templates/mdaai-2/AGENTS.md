# MDAAI 2.0 operating contract

For any agent system, point its entry instructions to the nearest AGENTS.md. Applicable parent and scoped governance files are cumulative.

This package governs only this folder until another repository explicitly adopts it. The nearest applicable `AGENTS.md` and higher-level operator instructions still apply. Read this file, the assigned task in [the task registry](PROJECT-INTERNAL/MANAGEMENT/TASKS.json), and only the named relevant references. Do not scan parent or unrelated projects unless asked.

| Rule | Contract |
| --- | --- |
| Authority | An explicit request authorizes its bounded implementation without repeated approval. Analysis alone authorizes no external write. No Git state changes, public release, spending, messaging, account creation, secret exposure, destructive cleanup, or unrelated deferred work without the applicable operator authority. See [authority](PROJECT-INTERNAL/GOVERNANCE/AUTHORITY.md). |
| Ownership | [Project Elaboration](PROJECT-INTERNAL/MANAGEMENT/PROJECT-ELABORATION.md) owns scope and sequence; [TASKS.json](PROJECT-INTERNAL/MANAGEMENT/TASKS.json) alone owns task state, disposition, acceptance evidence, and next action. Never maintain a second status list. |
| Records | The registry entry and evidence are normally enough. No routine per-edit WO, CWO, checkpoint, or approval ritual. Add a compact durable record only when a decision, defect, handoff, external effect, or audit need cannot be understood from the task and its evidence. Active records are owner-editable; terminal records are preserved and corrected by a linked superseding record. See [records](PROJECT-INTERNAL/GOVERNANCE/RECORDS.md). |
| Engineering | Put invariants with their domain owner; make state, effects, lifetimes, cancellation, recovery, resource limits, and durable formats explicit. Prefer the smallest coherent implementation over speculative layers. A defect follows investigation, faithful regression, related-test audit, red, root fix, affected green. See [engineering](PROJECT-INTERNAL/GOVERNANCE/ENGINEERING.md). |
| Evidence | Claim only the behavior actually proved. Choose checks by changed surface and risk; distinguish build, test, ordinary startup, browser/device, integration, and release evidence. Generated files may be runtime dependencies. Relevant blocking defects cannot be deferred into a false acceptance claim. See [evidence](PROJECT-INTERNAL/GOVERNANCE/EVIDENCE.md). |
| Coordination | Delegate only bounded, independent work when requested or useful and permitted. Give each file one owner, including tests/docs. The coordinator owns shared contracts, integration, and status. Preserve others' edits. See [reasoning](PROJECT-INTERNAL/GOVERNANCE/REASONING.md). |
| Continuation | On resumption, read the current registry entry and linked evidence, verify live state, then continue only currently authorized work. Deferred items remain visible but are not automatically authorized. See [recovery](PROJECT-INTERNAL/GOVERNANCE/RECORDS.md#recovery-and-supersession). |

Use the adopting project's actual shell, dependency manager, and verification commands. Do not add AI attribution. A passing structural checker is not product acceptance or adoption by another repository.
