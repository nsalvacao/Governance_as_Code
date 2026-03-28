---
title: Governance Overview
artifact_type: policy
status: public
visibility: public
classification: public
owner: repository-maintainer
review_cadence: quarterly
applies_to: this repository
source_basis: GitHub Docs + Open Source Guides
source_manifests:
  - governance__github_docs.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
---

# Governance Overview

This file governs **this repository as an instance** of the central governance system. It does not act as a downstream template. Reusable equivalents live under [`artifacts/01_Governance_Method/templates/`](./artifacts/01_Governance_Method/templates/).

## Scope

- Root Markdown files describe the public instance of this repository.
- `/.github/` contains the GitHub-native intake and validation surfaces used by this repository.
- `artifacts/` contains reusable assets that other repositories may instantiate selectively.

## Governance rules

1. Accepted structural and policy decisions are recorded in [`decision_log.md`](./decision_log.md).
2. The public target corpus is defined in the [`Public Document Map`](./README.md#public-document-map) section of the README.
3. Reusable assets must be edited in `artifacts/`, not in the root instance files, unless the change is specific to this repository itself.
4. This repository stays publishable by default; non-public rationale and working material remain under `/.private/`.
5. Public AI and coding-agent contribution behavior is governed by [`AI_AGENT_POLICY.md`](./AI_AGENT_POLICY.md).

## Lifecycle

1. Discovery and structural changes are proposed through issues or pull requests.
2. Deterministic validation runs before merge.
3. Public documentation and reusable assets are kept aligned with the decision log.
4. Larger structural or methodological changes must update the public and private decision logs together when applicable.

## Responsibilities

- The repository maintainer owns review cadence, publication safety, and structural coherence.
- Contributors proposing reusable assets must preserve the instance-versus-template boundary.
- Contributors changing root or `/.github/` files must treat them as concrete repository behavior, not placeholder content.

## Source Attribution

- Source manifests: [`governance__github_docs.md`](./sources/manifests/governance__github_docs.md)
- Primary source basis: GitHub Docs + Open Source Guides
- Alignment mode: `hybrid-synthesis`
- Reviewed on: 2026-03-27
