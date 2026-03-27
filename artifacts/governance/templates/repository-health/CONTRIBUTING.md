---
title: Contribution Guidelines
artifact_type: policy
status: public
visibility: public
classification: public
owner: "{{GOVERNANCE_OWNER}}"
review_cadence: quarterly
applies_to: reusable_governance
source_basis: GitHub Docs + Open Source Guides
source_manifests: governance__github_docs.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
---

# Contribution Guidelines

We are the canonical governance repository, so contributions must respect the automation-first architecture, placeholder conventions, and traceability rules described in `GOVERNANCE.md` and `README.md`.

## Before you start

1. Claim the artifact you want to edit in an issue or a comment on an existing conversation so we avoid overlap.
2. Confirm applicability: is the downstream repo actually going to instantiate this item? Use the repository's public document map or equivalent classification reference to classify the document (`public`, `public-redacted`, `private`).
3. Pull the latest `main` locally and run `python scripts/validate_governance_artifacts.py`; the matching GitHub Actions workflow enforces the same checks in CI.

## Authoring rules

- Use `{{UPPER_SNAKE_CASE}}` placeholders for values that will change per repository.
- Keep Markdown content focused, reuse existing sections, and avoid introducing private rationale.
- When you add a new artifact, append a `## Source Attribution` section referencing the manifest and source family.
- If you update an automation artifact (issue form, workflow, etc.), ensure the automation notes section explains how to reuse the file with GitHub Actions inputs, environments, or secrets.

## Review workflow

1. Open a pull request using `.github/PULL_REQUEST_TEMPLATE.md`.
2. Label the PR with `area:governance` and the relevant classification label (`public`, `public-redacted`, `private`).
3. Await a review from `{{GOVERNANCE_TEAM}}`.
4. Merge only after the validation workflow passes and the `## Source Attribution` block is intact.

## Source Attribution

- Source manifests: `governance__github_docs.md`
- Primary source basis: GitHub Docs + Open Source Guides
- Alignment mode: `hybrid-synthesis`
- Reviewed on: 2026-03-27
