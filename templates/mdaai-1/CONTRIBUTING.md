# Contributing

This project follows the TEJL/MDAAI workflow for structured, auditable development.

## Code of Conduct

All contributors are expected to follow [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

## Ways to Contribute

- Report bugs with clear reproduction steps.
- Suggest improvements with context and expected impact.
- Improve documentation.
- Submit code changes with tests and verification notes.
- Contribute operational lessons back to `PROJECT-INTERNAL/KNOWLEDGE/` when appropriate.

## Development Setup

Use the project command reference in `PROJECT-INTERNAL/KNOWLEDGE/DEVELOPER-GUIDE.md`.

Common template commands:

```bash
# Validate repository structure
just validate

# Install dependencies
just install

# Run tests
just test

# Run lint checks
just lint

# Format code
just fmt
```

Project-specific repositories should replace generic Justfile recipes with real commands.

## Development Workflow

1. Read `AGENTS.md` for repository navigation and AI workflow rules.
2. Check `PROJECT-INTERNAL/MANAGEMENT/PROJECT-ELABORATION.md` for authorized work.
3. Review relevant ADRs in `PROJECT-INTERNAL/ARCHITECTURE/`.
4. Follow the relevant guides in `PROJECT-INTERNAL/GUIDES/`.
5. Make focused changes.
6. Run the verification commands documented in the Work Order or developer guide.
7. Update documentation when behavior, usage, or operations change.

AI-assisted implementation must follow the Work Order lifecycle before file edits begin. Human-only contributions should still preserve the same traceability when the project requires it.

## Pull Request Checklist

Before submitting a pull request:

- `just validate` passes.
- Relevant build, test, lint, and format commands pass.
- Documentation is updated for user-facing or workflow changes.
- ADRs are added or updated for significant architecture decisions.
- No secrets, credentials, private data, generated caches, or local-only files are included.
- Commit messages are clear and do not add AI attribution.

## Commit Messages

Use concise, descriptive commit messages. Conventional Commit style is recommended:

```text
feat: add account export endpoint
fix: handle empty configuration file
docs: document deployment checklist
chore: update template validation
```

## Reporting Bugs

Good bug reports include:

- Project version or commit.
- Operating system and relevant tool versions.
- Steps to reproduce.
- Expected behavior.
- Actual behavior.
- Logs or screenshots when useful.

Security issues must be reported privately according to [SECURITY.md](SECURITY.md).

## License

By contributing, you agree that your contributions are licensed under the repository license unless another written agreement applies.
