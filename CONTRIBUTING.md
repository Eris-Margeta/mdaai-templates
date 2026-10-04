# Contributing to the template catalog

1. Fork this catalog and create a bounded change. Select the family and explain whether the proposal changes implementation, protocol interpretation, or project-specific scaffolding.
2. Preserve authored notices and source snapshots. Propose new revisions rather than pretending historic text always said something different. Do not import source project task history, credentials, private paths or runtime/account configuration.
3. Update the payload and both manifests: list every payload, source repository/revision/path/hash, resulting SHA-256/size and explicit transformation reason. Source revisions must be full commit IDs. Do not claim an unchanged export when bytes differ.
4. Recompute digests using standard SHA-256 tooling. Keep file arrays sorted by repository-relative path. No traversal, symlinks, remote executable installers or unbounded ingestion.
5. Run `python3 scripts/validate_catalog.py` and `python3 -m unittest discover -s tests -v`. Review any new link gap; do not blindly add it to the baseline. Explain genuine historical/example limitations and adoption work.
6. Submit a pull request with the scope, provenance, notice/reuse scope, adaptation rationale and real verification results. Changes need owner review before publication; downstream adoption is a separate explicit decision.

Catalog validation proves integrity and structural consistency, not legal completeness, semantic correctness, downstream runtime acceptance or authority to automatically apply upstream changes. Keep protocol identity, template revision and catalog version distinct. See [license scopes](LICENSE-NOTICES.md); contributions do not silently grant a new blanket license.
