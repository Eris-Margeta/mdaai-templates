# Engineering and defect workflow

## Design at the owning boundary

Place rules where the affected domain owns them. Prefer pure decisions with explicit effects, typed failure outcomes, stable interfaces, and versioned durable contracts. Make ownership, transfer, lifetimes, cancellation, drain, rollback, retries, idempotency, and resource ceilings explicit when applicable. Treat untrusted data as data, not authority. Avoid duplicate state, speculative abstraction, and generic infrastructure without a concrete second use; do not compress away safeguards or observability.

For architecture changes, record the decision, rejected material alternatives, migration/rollback, and limits in a compact ADR. Update relevant user/developer documentation and examples with the implementation. A fact about an older build or environment is not proof of the current one.

## Defects: investigate → regression → audit → red → root fix → green

1. State expected versus actual behavior, the owning invariant, and a causal hypothesis; label uncertainty until checked.
2. Add the smallest faithful regression at the broken boundary before behavior edits. For non-code issues, use a reproducible structural/runtime inspection rather than a ceremonial test.
3. Audit adjacent tests and expectations. Preserve independent oracles; justify fixture/expectation changes from the contract, not from a desire for green output.
4. Capture the selected test and intended pre-fix failure. A harness crash, skipped test, or zero selected tests is not a red regression.
5. Fix the root owner. Do not turn an invalid state into success by hiding errors, weakening assertions, or adding unjustified retries.
6. Run the regression and affected composition, failure, and ordinary runtime paths. Record residual limits.

If a safe pre-fix red run is unavailable, record the reason and use an independent contract or observation; never invent a red result.

## Resource hygiene belongs to the work

Declare ownership and lifetime for caches, scratch space, build output, subprocesses and container resources. Inventory before deletion; preserve source, credentials, evidence, active work, runtime dependencies and rollback artifacts. Recheck exact path/identity/liveness at the effect boundary. Prefer a bounded recovery window for disposable output, then report actual deletion honestly; moving data into quarantine does not reclaim disk space. Only unused project-labeled Docker objects may be cleaned automatically—never global prune or volumes. RAM hygiene means releasing owned idle processes and buffers, not purging the operating system or killing unrelated applications. Measure disk headroom and local memory with units and sampling limits. A cleanup milestone requires ordinary startup verification afterward.

An unrelated defect is registered in the canonical task source and may be deferred with a reason; it does not stop the current authorized task unless it invalidates that task's evidence or acceptance. A defect relevant to a release or checkpoint still blocks that claim. Expected red tests and transient compiler feedback during a repair are not separate defects. No mandatory CWO is created for every error.
