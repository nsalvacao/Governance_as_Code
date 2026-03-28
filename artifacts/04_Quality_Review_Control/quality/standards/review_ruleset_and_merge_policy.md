---
title: Review Ruleset and Merge Policy
artifact_type: standard
status: public-draft
visibility: public
classification: public
owner: quality-platform
review_cadence: quarterly
applies_to: pull request review, merge rules, and exception handling
source_basis: GitHub Docs branch protection and rulesets guidance
source_manifests:
  - governance__github_docs.md
alignment_mode: direct-adaptation
updated: 2026-03-27
---

## Purpose

Define branch protection rules, required status checks, and merge conditions that gate all changes into protected branches.

## Protected Branches

| Branch | Protection Level | Notes |
|---|---|---|
| `{{DEFAULT_BRANCH}}` (e.g., `main`) | Full — no direct push | All changes via PR |
| `{{RELEASE_BRANCH_PATTERN}}` (e.g., `release/*`) | Full | Cherry-picks only |
| `{{STAGING_BRANCH}}` | Partial — status checks required | Direct push by `{{STAGING_PUSH_TEAM}}` allowed |

## Required Status Checks

All of the following must pass before merge is permitted on `{{DEFAULT_BRANCH}}`:

| Check Name | Tool/Workflow | Failure Action |
|---|---|---|
| `{{GOVERNANCE_VALIDATOR_CHECK}}` | `validate-governance-artifacts.yml` | Block merge |
| `{{UNIT_TEST_CHECK}}` | `{{CI_WORKFLOW_NAME}}` | Block merge |
| `{{LINT_CHECK}}` | `{{LINT_WORKFLOW_NAME}}` | Block merge |
| `{{SECURITY_SCAN_CHECK}}` | `{{SECURITY_WORKFLOW_NAME}}` | Block merge |
| `{{DEPENDENCY_REVIEW_CHECK}}` | `dependency-review` action | Block merge on high/critical |

Status checks are required to be up-to-date (re-run if base branch advances).

## Review Requirements

| Target Branch | Min Approvals | Dismiss Stale Reviews? | Require Code Owner Review? | Allow Force Push? |
|---|---|---|---|---|
| `{{DEFAULT_BRANCH}}` | `{{MIN_REVIEWERS}}` (e.g., 2) | Yes | Yes | No |
| `{{RELEASE_BRANCH_PATTERN}}` | `{{RELEASE_MIN_REVIEWERS}}` | Yes | Yes | No |
| `{{STAGING_BRANCH}}` | `{{STAGING_MIN_REVIEWERS}}` | No | No | No |

## Merge Strategy

- **Merge commit**: `{{ALLOW_MERGE_COMMIT}}` — preserves full commit history
- **Squash merge**: `{{ALLOW_SQUASH}}` — normalizes feature branches
- **Rebase merge**: `{{ALLOW_REBASE}}` — linear history

Default strategy for `{{DEFAULT_BRANCH}}`: `{{DEFAULT_MERGE_STRATEGY}}`.

Enforce linear history: `{{ENFORCE_LINEAR_HISTORY}}` (Yes/No).

## Additional Enforcement

- Require signed commits: `{{REQUIRE_SIGNED_COMMITS}}` (Yes/No)
- Restrict deletions: Yes — no branch deletion for protected branches
- Lock branch (read-only): `{{LOCK_BRANCH}}` (for audit/compliance periods)
- Require conversation resolution before merge: Yes

## Exception Handling

Exceptions to the above must be:

1. Approved by `{{EXCEPTION_AUTHORITY}}` (e.g., repository admin or security officer)
2. Documented in `{{EXCEPTION_LOG_LOCATION}}` with rationale and expiry date
3. Time-limited to `{{MAX_EXCEPTION_DURATION}}` (e.g., 48 hours)
4. Reverted automatically after the exception window closes

## Canonical Relationship

- The GitHub-native enforcement surface is represented by the reusable assets under `artifacts/01_Governance_Method/governance/templates/github-native/`.
- This standard is the quality-layer policy that explains why the rules exist and how they are applied.

## Source Attribution

- Source manifests: `governance__github_docs.md`
- Primary source basis: GitHub Docs branch protection and rulesets guidance
- Alignment mode: direct-adaptation
- Reviewed on: 2026-03-27
