---
title: Release and Versioning Policy
artifact_type: policy
status: public-draft
visibility: public
classification: public
owner: "{{OWNER_NAME}}"
review_cadence: quarterly
applies_to: release and version management
source_basis: Semantic Versioning 2.0.0 (semver.org) and Conventional Commits 1.0.0
source_manifests:
  - governance__github_docs.md
  - operations__google_sre.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
---

## Policy Statement

All versioned artifacts follow Semantic Versioning 2.0.0. All commits that produce a release follow the Conventional Commits 1.0.0 specification. Releases are tagged, changelogs are generated from commit history, and rollback readiness is proven before publication.

## Version Format

All version strings conform to: `MAJOR.MINOR.PATCH[-PRERELEASE][+BUILD]`

- `MAJOR`, `MINOR`, and `PATCH` are non-negative integers with no leading zeros.
- Pre-release and build metadata are optional suffixes separated by `-` and `+` respectively.
- Example: `1.4.2`, `2.0.0-rc.1`, `1.0.0-beta.3+build.42`

Versions below `1.0.0` indicate unstable public API; anything may change at any minor version.

## MAJOR Increment Triggers

Increment `MAJOR` when a change is incompatible with the previous public API. A change is breaking when it:

- Removes or renames a public interface, endpoint, field, or behavior that consumers depend on.
- Changes the semantics of an existing interface in a way that requires consumers to adapt.
- Drops support for a previously supported runtime, platform, or dependency version declared in the public contract.

`MAJOR` increments reset `MINOR` and `PATCH` to `0`.

## MINOR Increment Triggers

Increment `MINOR` when new functionality is added in a backward-compatible manner:

- New public endpoints, fields, or commands are introduced without removing or changing existing ones.
- Existing behavior is extended in a way that does not require consumers to change.
- A feature previously behind a flag is promoted to stable without behavioral change for existing users.

`MINOR` increments reset `PATCH` to `0`. `MAJOR` stays unchanged.

## PATCH Increment Triggers

Increment `PATCH` when backward-compatible bug fixes are made:

- A defect in existing behavior is corrected without changing the public interface.
- Internal refactoring with no observable change to consumers.
- Dependency updates that fix security vulnerabilities without changing the public API surface.

## Pre-release Identifiers

Pre-release versions use the identifier `{{PRERELEASE_IDENTIFIER}}` appended after a hyphen. Standard identifiers in ascending stability order:

| Identifier | Meaning |
|---|---|
| `alpha` | Early prototype; breaking changes expected |
| `beta` | Feature-complete; breaking changes unlikely but possible |
| `rc` (release candidate) | Production-ready candidate; no new features |

Pre-release versions have lower precedence than the associated normal version. Example: `1.0.0-rc.1 < 1.0.0`.

## Commit Message Format

All commits that may contribute to a release must follow: `type(scope): description`

- `type` is mandatory and must be one of the types in the table below.
- `scope` is optional; when present, it names the component or module affected (e.g., `auth`, `api`).
- `description` is a short imperative summary in lowercase, no trailing period.
- Body and footers are optional but required when a breaking change is introduced.

## Commit Types

| Type | Version bump | Description |
|---|---|---|
| `feat` | MINOR | A new feature |
| `fix` | PATCH | A bug fix |
| `docs` | none | Documentation changes only |
| `style` | none | Formatting, whitespace; no logic change |
| `refactor` | none | Code restructuring; no feature or fix |
| `perf` | PATCH | Performance improvement |
| `test` | none | Adding or updating tests |
| `chore` | none | Maintenance tasks (dependency bumps, config) |
| `ci` | none | CI/CD configuration changes |
| `revert` | varies | Reverts a previous commit |

## Breaking Change Notation

A breaking change is indicated by either:

- A `BREAKING CHANGE:` footer in the commit body, followed by a description of what breaks and how to migrate.
- An exclamation mark suffix on the type: `feat!: remove deprecated endpoint`.

Both notations trigger a MAJOR version increment. The `BREAKING CHANGE` footer is preferred because it carries migration guidance.

## Tag Format

All release tags follow the pattern: `v{{MAJOR}}.{{MINOR}}.{{PATCH}}`

- The `v` prefix is mandatory.
- Pre-release tags append the identifier: `v1.0.0-rc.1`.
- Tags are immutable; once pushed, a tag must not be deleted or moved to a different commit.

## Changelog Generation Guidance

Changelogs are generated from the commit history between consecutive release tags. The generated changelog must be reviewed and approved before the release is published. Tooling reads commit types to group entries under `Features`, `Bug Fixes`, `Performance Improvements`, and `Breaking Changes`. Commits with types that carry no version bump (docs, style, test, chore, ci) may be omitted or grouped under `Other Changes` at maintainer discretion.

## Release Approval and Publication

A release requires approval from `{{RELEASE_APPROVER}}` before the tag is pushed. The release approval confirms that:
- All quality gates in `definition_of_done_quality_gates.md` are satisfied.
- The changelog is accurate and complete.
- Rollback readiness has been verified (rollback procedure documented, tested, and owner identified).

## Rollback Readiness

Before every release, the release owner must confirm that a rollback procedure exists, is documented at `{{ROLLBACK_RUNBOOK_PATH}}`, and has been tested against the previous stable version.

## Source Attribution

- Source manifests: governance__github_docs.md, operations__google_sre.md
- Primary source basis: Semantic Versioning 2.0.0 (semver.org) and Conventional Commits 1.0.0
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27
