---
title: Change Log / Release Notes Template
artifact_type: template
status: public
visibility: public
classification: public
owner: "{{DELIVERY_OWNER}}"
review_cadence: quarterly
applies_to: release communication and public change history
source_basis: Keep a Changelog format and Conventional Commits specification
source_manifests:
  - governance__github_docs.md
  - operations__google_sre.md
alignment_mode: guided-synthesis
updated: 2026-03-30
---

## Change Log / Release Notes

This template follows the [Keep a Changelog](https://keepachangelog.com/) format and aligns with the [Conventional Commits](https://www.conventionalcommits.org/) specification. Maintain an `[Unreleased]` section at the top and move entries to a versioned release section on each release. Entries within each section should be ordered newest-first.

---

## [Unreleased]

Changes merged to the main branch but not yet released. Move all entries to the next versioned section when cutting a release.

### Added
- `{{UNRELEASED_ADDED_1}}`

### Changed
- `{{UNRELEASED_CHANGED_1}}`

### Fixed
- `{{UNRELEASED_FIXED_1}}`

---

## [`{{VERSION}}`] - `{{RELEASE_DATE}}`

### Release Header

| Field | Value |
|---|---|
| Version | `{{VERSION}}` |
| Release date | `{{RELEASE_DATE}}` |
| Release manager | `{{RELEASE_MANAGER}}` |
| Release notes author | `{{RELEASE_NOTES_AUTHOR}}` |
| Related release plan | `{{RELEASE_PLAN_LINK}}` |

---

### Breaking Changes

> List all changes that break backward compatibility. Users must act on these before upgrading.

- `{{BREAKING_CHANGE_DESCRIPTION}}` (`{{COMMIT_OR_PR_REFERENCE}}`)

**Migration guide:**
`{{MIGRATION_STEPS}}`

Provide a numbered migration guide for every breaking change. If no breaking changes exist, write "None in this release."

---

### Added

> New features and capabilities introduced in this release. Maps to Conventional Commits `feat:` type.

- `{{ADDED_CHANGE_DESCRIPTION}}` (`{{COMMIT_OR_PR_REFERENCE}}`)

---

### Changed

> Changes to existing functionality that do not break the public API or user-facing contract. Maps to `refactor:`, `perf:`, `style:` types.

- `{{CHANGED_CHANGE_DESCRIPTION}}` (`{{COMMIT_OR_PR_REFERENCE}}`)

---

### Deprecated

> Features that are still available but will be removed in a future release. Give users clear advance notice and an alternative.

- `{{CHANGE_DESCRIPTION}}` — will be removed in `{{REMOVAL_VERSION}}`; use `{{ALTERNATIVE}}` instead (`{{COMMIT_OR_PR_REFERENCE}}`)

---

### Removed

> Features removed in this release. Should correspond to previously Deprecated entries. Maps to `feat!:` or `BREAKING CHANGE` footer.

- `{{CHANGE_DESCRIPTION}}` (`{{COMMIT_OR_PR_REFERENCE}}`)

---

### Fixed

> Bug fixes that restore intended behaviour. Maps to Conventional Commits `fix:` type.

- `{{FIXED_CHANGE_DESCRIPTION}}` (`{{COMMIT_OR_PR_REFERENCE}}`)

---

### Security

> Fixes for security vulnerabilities. Always include a CVE or advisory reference where available. Maps to `fix:` type with `security` scope.

- `{{CHANGE_DESCRIPTION}}` — `{{CVE_OR_ADVISORY_REFERENCE}}` (`{{COMMIT_OR_PR_REFERENCE}}`)

Security entries must be included even if the fix is trivial. Users need to know to upgrade for security reasons independently of other changes.

---

### Known Issues

> Issues present in this release that are known but not yet fixed. Include a workaround where available.

- `{{KNOWN_ISSUE_DESCRIPTION}}` — workaround: `{{WORKAROUND}}`

---

## [`{{PREVIOUS_VERSION}}`] - `{{PREVIOUS_RELEASE_DATE}}`

Add previous release entries following the same structure above. Keep the full history in this file — do not delete older versions.

---

## Source Attribution

- Source manifests: `governance__github_docs.md`, `operations__google_sre.md`
- Primary source basis: Keep a Changelog format and Conventional Commits specification
- Alignment mode: guided-synthesis
- Reviewed on: 2026-03-30
