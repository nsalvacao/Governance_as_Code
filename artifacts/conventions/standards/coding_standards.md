---
title: Coding Standards
artifact_type: standard
status: public-draft
visibility: public
classification: public
owner: "{{OWNER_NAME}}"
review_cadence: semiannual
applies_to: code and automation artifacts
source_basis: Google Style Guide principles and GitHub Docs engineering guidance
source_manifests:
  - governance__github_docs.md
  - platform__microsoft_learn.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
---

## Purpose

Define consistent technical expectations for code, scripts, schemas, and automation across downstream repositories. Consistency reduces review friction and enables automated validation.

## Naming Conventions

Names communicate intent. Choose names that make the code readable without requiring a comment.

- **Variables:** Follow `{{NAMING_CONVENTION}}` (e.g., `camelCase` for most languages, `snake_case` for Python). Names must be descriptive; single-letter names are permitted only as loop counters or in well-understood mathematical contexts.
- **Functions and methods:** Follow `{{FUNCTION_NAMING}}` (e.g., `camelCase` verb phrases: `getUserById`, `validateSchema`). Functions that return a boolean should read as a predicate (e.g., `isValid`, `hasPermission`).
- **Constants:** Follow `{{CONSTANT_NAMING}}` (e.g., `UPPER_SNAKE_CASE` for module-level constants). Constants must be defined at the top of the module or in a dedicated constants file.
- **Files and directories:** Use lowercase with hyphen separators for file names (e.g., `user-service.ts`). Do not use spaces or special characters other than hyphens and underscores.

## Type Usage

Types communicate contracts. Explicit types catch errors before runtime.

- Prefer explicit type annotations over inferred types for all public function signatures and module exports.
- Avoid `any` or its language equivalents (e.g., `object`, `interface{}`) in production code; use narrower types or generics.
- Avoid implicit type coercion; use explicit conversion functions.
- When a type is complex or reused, define a named type or interface rather than inlining an anonymous structure.
- Schema definitions (JSON Schema, OpenAPI) are the source of truth for data shapes exchanged across service boundaries; generated types must trace back to the schema.

## Comment Standards

Comments explain why, not what. Code should be self-explanatory; comments fill the gap where it cannot be.

- **When to comment:** Non-obvious logic, performance trade-offs, workarounds for external bugs, or decisions that look wrong but are correct.
- **What not to comment:** Obvious code (avoid `// increment counter` above `i++`), commented-out dead code (delete it; git history preserves it), and TODO comments that have no associated issue or owner.
- Docstrings or JSDoc blocks are required for all public functions, methods, and classes. They must describe parameters, return values, and exceptions.
- Inline comments use the language's line-comment syntax and are placed on the line above the code they explain, not at the end of a long line.

## Error Handling

Errors are first-class values. Silent failures are production incidents waiting to happen.

- Use explicit error types `{{ERROR_TYPE}}` rather than generic exceptions or untyped error objects. Define domain-specific error types for errors that callers must handle differently.
- Do not catch an error only to swallow it silently. If an error cannot be handled at a given layer, re-throw it or wrap it with additional context.
- Provide actionable error messages: include what was attempted, what went wrong, and (where possible) how to fix it.
- Log errors at the appropriate severity level; reserve `ERROR` for conditions that require human attention.
- Functions that can fail should signal failure explicitly via their return type (e.g., `Result<T, E>`, `(T, error)`) rather than relying solely on exceptions for expected failure paths.

## Testing Requirements

Tests are executable specifications. They define what correct behavior looks like.

- **Unit tests:** Required for every public function or method. Tests must be co-located with the source file or placed in the language-conventional test directory.
- **Integration tests:** Required for every module boundary (e.g., service-to-service calls, database interactions, CLI commands). Integration tests may live in a dedicated `integration/` directory.
- **Coverage threshold:** Minimum coverage is `{{COVERAGE_THRESHOLD}}` for lines and branches combined. CI enforces this gate and must fail builds that drop below the threshold. Coverage alone is not a quality signal; tests must assert meaningful behavior.
- Test file names follow the pattern `{{TEST_FILE_NAMING_CONVENTION}}` (e.g., `*.test.ts`, `*_test.py`).
- Tests must be deterministic: no reliance on external network calls, system clocks, or random seeds without explicit mocking or seeding.

## Code Review Checklist

Before marking a PR ready for review, the author confirms:

- [ ] Code follows naming conventions defined in this standard.
- [ ] All public functions have explicit types and docstrings.
- [ ] No `any`, silent error swallows, or commented-out code.
- [ ] Unit tests cover the new or changed logic.
- [ ] Integration tests cover the module boundary if changed.
- [ ] Coverage gate still passes locally.
- [ ] Linting and formatting pass with zero errors.
- [ ] No new linting suppressions added without a comment explaining why.

## Linting Configuration

The linting configuration for this repository is located at `{{LINT_CONFIG_PATH}}`. All contributors must run the linter locally before pushing. CI enforces the same configuration. Suppressions (inline `// eslint-disable` or equivalent) require a comment on the same line explaining the reason.

## Formatter Configuration

The formatter configuration is located at `{{FORMATTER_CONFIG_PATH}}`. Formatting is non-negotiable and fully automated; do not manually format code that the formatter will reformat. Configure your editor to run the formatter on save.

## Source Attribution

- Source manifests: governance__github_docs.md, platform__microsoft_learn.md
- Primary source basis: Google Style Guide principles and GitHub Docs engineering guidance
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27
