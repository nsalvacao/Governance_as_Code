---
title: GitOps Policy
artifact_type: policy
status: draft
visibility: public
classification: public
owner: platform-governance
review_cadence: quarterly
applies_to: repositories and platforms that use declarative delivery
source_basis: OpenGitOps and GitHub platform automation guidance
source_manifests:
  - platform__gitops.md
  - governance__github_docs.md
alignment_mode: direct-adaptation
updated: 2026-03-27
---

# GitOps Policy

## Rules

- Treat Git as the source of truth for declarative desired state.
- Review changes before reconciliation where the environment requires it.
- Keep reconciliation automated and observable.
- Separate the desired state from generated or runtime-only state.
- Track application and environment definitions as reusable, versioned artifacts.

## Operational expectations

- Every GitOps-managed workload has a clear owner.
- Every promotion is traceable to a commit or pull request.
- Reconciliation failures produce actionable diagnostics.

## Source Attribution

- Source manifests: `platform__gitops.md`, `governance__github_docs.md`
- Primary source basis: OpenGitOps and GitHub automation guidance
- Alignment mode: direct-adaptation
- Reviewed on: 2026-03-27
