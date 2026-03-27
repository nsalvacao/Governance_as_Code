---
title: Governance Overview
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

# Governance Overview

This repository governs the organisational infrastructure for methodology, documentation, and automation. We operate as a central node: we define what artifacts exist, how they should be written, and which downstream repositories may instantiate them. Downstream teams should treat these files as **templates**—apply the placeholders (`{{REPO_NAME}}`, `{{GOVERNANCE_OWNER}}`, `{{REVIEW_CADENCE}}`, `{{GOVERNANCE_TEAM}}`) and adapt only what is necessary for their context, always ensuring that the core conventions remain intact.

## Decision Model

- **Single source of truth:** Every policy, workflow, and schema published here is auditable and versioned.
- **Selective instantiation:** Not every satellite repo needs every artifact; consult the classification grid before copying.
- **Automation-first:** GitHub Actions, issue forms, frontmatter, environments, and secrets are the preferred instruments for enforcement.
- **Dual audience:** Human reviewers and AI agents must both find the conventions explicit, parameterised, and deterministic.

## Governance Lifecycle

1. **Propose changes** via `CONTRIBUTING.md`.
2. **Review** with the PR template and issue forms to capture context.
3. **Automate** updates through reusable workflows under `.github/workflows/`.
4. **Archive** outdated content with the classification system and issue a `public-redacted` or `private` version when required.

## Responsibilities

- `{{GOVERNANCE_TEAM}}` owns the review cadence, ensures attribution stays tied to `governance__github_docs.md`, and coordinates the automation layer.
- `{{REPO_MAINTAINER}}` ensures contributors understand the selective instantiation rule before copying artifacts into their repositories.

## Source Attribution

- Source manifests: `governance__github_docs.md`
- Primary source basis: GitHub Docs + Open Source Guides
- Alignment mode: `hybrid-synthesis`
- Reviewed on: 2026-03-27
