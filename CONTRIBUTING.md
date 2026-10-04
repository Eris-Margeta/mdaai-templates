# Catalog admission via pull request

Change template content in its individual canonical repository first. Submit a catalog PR naming its public repository and full immutable 40-character commit, Apache-2.0 scope and retained notices, original-source provenance/adaptations, and mirror file sizes/SHA-256. Preserve schemaVersion 1, unique IDs and safe existing prefixes. Review hashes and original provenance before admission; update the website catalog commit pin only after merge. Catalog mirrors are explicitly synchronized snapshots, never an independent authority.

Run `python scripts/validate_catalog.py`, `python scripts/verify_sources.py` and `python -m unittest discover -s tests -v` on Python 3.13.14. CI reads `.python-version`. Source verification downloads only listed immutable bytes, never executes source code. PR CI uses read-only permissions, no secrets, and no pull_request_target. Owner review/adoption is required; branch protection must never be bypassed.
