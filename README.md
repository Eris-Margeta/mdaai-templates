# mdaai-templates

![Catalog checks](https://github.com/Eris-Margeta/mdaai-templates/actions/workflows/catalog.yml/badge.svg)

Literal, versioned governance-file bundles by **Eris Margeta Kurdali**: **MDAAI 1.0 first-generation family** and **MDAAI 2.0 portable core**. Private source projects and their Git histories are not published here.

## Protocol ≠ template

The **protocol** is the method and rules governing work, evidence, decisions and improvement. A **template** is a particular set of files implementing those rules in a repository. Templates can evolve through reviewed changes, manually or with an assistant, under the applicable protocol. Catalog updates do not authorize rewriting downstream repositories.

```text
Protocol → Template files → Repository → Review → Template revision
                               ↑                       │
                               └── explicit adoption ──┘
```

## Bundles and file ownership

| Bundle | Files and responsibilities |
| --- | --- |
| [MDAAI 1.0 family](templates/mdaai-1/AGENTS.md) | `AGENTS.md` routes reading; `GOVERNANCE/AI-INSTRUCTIONS.md` supplies the rules. Lifecycle/Beta protocols select requirements. Project Elaboration authorizes scope; Work Order protocols, WO/CWO templates, function schemas and the blank registry define the audit trail. ADRs preserve decisions, knowledge files preserve lessons, checkpoints preserve milestones. |
| [MDAAI 2.0](templates/mdaai-2/AGENTS.md) | Root operating contract plus five governance owners: `AUTHORITY.md` authorization; `ENGINEERING.md` engineering; `EVIDENCE.md` acceptance claims; `REASONING.md` investigation/coordination; `RECORDS.md` task and record lifecycle. Project Elaboration owns scope/sequence; `TASKS.json` alone owns task state, disposition, evidence and next action. |

```text
templates/
├── mdaai-1/
│   ├── AGENTS.md, CLAUDE.md, project-meta.yaml, LICENSE
│   ├── PROJECT-INTERNAL/
│   │   ├── GOVERNANCE/         instructions and protocols
│   │   ├── MANAGEMENT/         project scope and metadata
│   │   ├── WORK-ORDERS/        blank registry and WO/CWO templates
│   │   ├── AI/functions/       registry/work-order/reporting schemas
│   │   ├── CHECKPOINTS/        milestone template
│   │   └── ARCHITECTURE/, GUIDES/, KNOWLEDGE/, SCRATCH/
│   └── .template/, docs/       inherited tooling and doc scaffolds
└── mdaai-2/
    ├── AGENTS.md, CLAUDE.md
    └── PROJECT-INTERNAL/
        ├── GOVERNANCE/        AUTHORITY, ENGINEERING, EVIDENCE, REASONING, RECORDS
        └── MANAGEMENT/        PROJECT-ELABORATION.md and TASKS.json
```

In the first generation, a task follows authorized scope → applicable lifecycle rules → Work Order and registry → verification → completion and any triggered checkpoint. In v2 it follows bounded scope → stable task row → relevant checks/evidence → truthful result. Durable v2 records are conditional, not a per-edit ritual. Language doctrines, multi-agent coordination, diagnostics and milestones apply when relevant; optional compatibility pointers and tooling do not create new authority.

## Adopt manually

1. Read the selected entry point, applicable rules and [license scopes](LICENSE-NOTICES.md). Preserve stronger existing project constraints.
2. Back up the target. Choose **one** active profile; reconcile contradictory v1/v2 instructions before activation.
3. Copy selected bundle contents to the target, preserving relative paths and notices. Do not copy this catalog root or another project's history.
4. Fill project identity, authorized scope, actual environment and real commands. For v2 choose a unique uppercase task prefix and add real task rows to the initially empty registry.
5. Reconcile historical limitations below and exercise actual project checks, one ordinary task and resumption. Structural catalog validation is not downstream acceptance.

Blank registries, bracketed text and example links are **uninitialized scaffolds**, not a ready-to-run project. No installer or automatic activation is provided. Inherited first-generation scripts are optional artifacts, not executed by catalog validation or verified here as downstream installation tools.

## Provenance and honest limitations

- First-generation source: `Eris-Margeta/monorepo-template`, commit `ec57688e48f8ad12e60785173956d50386fee6b8`. `VERSION` says **1.0.0**, `AI-INSTRUCTIONS.md` says **1.7**, and supporting protocols have separate labels. “MDAAI 1.0” names the family, **not** a pristine original v1.0 release. The initial `d118cd1` authored blank registry and Elaboration replace later source-instance history, explicitly recorded in [export-manifest.json](export-manifest.json).
- MDAAI 2.0 source: `Eris-Margeta/MDAAI-2-0`, commit `5395006954bf298db652679b934ea5755ec17b1c`. The six authored core files are supplied; only the root's laboratory-specific workspace/tool/check paragraph is made portable. Project Elaboration and TASKS are deliberately fresh project-owned scaffolds per the source adoption procedure. Laboratory validators, dashboards, research, rollout ADRs and execution history are excluded; no automatic rollout implementation is claimed.
- Literal first-generation inconsistencies remain visible: `AI-INSTRUCTIONS.md` refers to `PROJECT-DEVELOPMENT-ELABORATION.md` and `GUIDES/CHECKPOINT-PROTOCOL.md`, while supplied owners are `MANAGEMENT/PROJECT-ELABORATION.md` and `GOVERNANCE/CHECKPOINT-PROTOCOL.md`. Work Order immutability versus active lifecycle wording also requires reconciliation. No fake duplicate authority files were invented to hide this.
- Inherited documentation examples reference future project pages. The exact [checked link-gap inventory](tests/known-source-link-gaps.json) records them. New unresolved links fail validation; existing examples are not presented as configured documentation.
- Every payload's source path/revision/hash, destination hash/size and adaptation reason is recorded. Exclusions are explicit. Source hashes remain useful when source access is restricted; downloading this public catalog requires no source access.

Manifest entries deliberately use `complete: false` and `status: review-before-adoption`: export integrity is verified, completed downstream configuration is not.

## Optional website build-time feed

[`templates.json`](templates.json) is deterministic **schemaVersion 1**. Catalog **0.1.0** is separate from template/protocol identity. Entries contain `id`, `title`, `description`, `templateVersion`, `protocol`, `source`, `status`, `complete`, `entrypoint`, and `files`. File entries contain repository-relative `path`, SHA-256, byte `size`, and `role` (`required`, `optional`, or `conditional`). Role describes selection, not permission to disregard governing conditions.

Pin a reviewed **40-character commit SHA** from `Eris-Margeta/mdaai-templates`, never an unreviewed moving branch/latest reference. Fetch that commit's archive and manifest; enforce repository identity, schema, count/byte limits and exact `templates/mdaai-1/` or `templates/mdaai-2/` allowlists. Reject absolute paths, traversal, symlinks and duplicates **before extraction**; verify every listed file's size and SHA-256. Render only listed payloads and never execute their scripts/instructions. Updating the pin is a separate review action. Ingestion is optional and does not change governance authority.

Archive pattern: `https://github.com/Eris-Margeta/mdaai-templates/archive/<FULL_COMMIT_SHA>.tar.gz`.
Manifest pattern: `https://raw.githubusercontent.com/Eris-Margeta/mdaai-templates/<FULL_COMMIT_SHA>/templates.json`.

## Verify and contribute

Development/CI Python 3.13.14 (from `.python-version`); minimum validator compatibility Python 3.11+, standard library only:

```sh
python3 scripts/validate_catalog.py
python3 -m unittest discover -s tests -v
```

See [CONTRIBUTING.md](CONTRIBUTING.md). Changes are proposals until reviewed and adopted; publication alone does not supersede existing repository authority.

## Canonical repositories and aggregate admission

The canonical templates are https://github.com/Eris-Margeta/mdaai-template-1 and https://github.com/Eris-Margeta/mdaai-template-2 . This repository remains the unified catalog and compatibility mirror, not a competing source owner. Each `source` pins a public canonical repository commit; `originalSource` preserves historical provenance. Existing schemaVersion 1 paths remain stable. Both distributed templates and original catalog packaging use Apache-2.0, with inherited MIT notices preserved.

Registry additions go through a reviewed pull request before the website updates its catalog pin. No website hardcoded parallel feed is necessary.
