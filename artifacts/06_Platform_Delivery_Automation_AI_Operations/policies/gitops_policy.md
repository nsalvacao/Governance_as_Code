---
title: GitOps Policy
artifact_type: policy
status: public
visibility: public
classification: public
owner: platform-governance
review_cadence: quarterly
applies_to: repositories and platforms that use declarative delivery
source_basis: OpenGitOps v1.0 (gitops.tech)
source_manifests:
  - platform__gitops.md
  - governance__github_docs.md
alignment_mode: direct-adaptation
updated: 2026-03-30
---

# GitOps Policy

## Policy Scope

This policy applies to all workloads and platforms that use declarative configuration managed in Git. It is grounded in the four OpenGitOps v1.0 principles published at gitops.tech. Teams adopting GitOps delivery must conform to all four principles and the implementation requirements below.

## OpenGitOps v1.0 Principles

The four principles are mandatory. Each entry below states the principle, its policy interpretation, and the relevant configuration placeholder.

### Principle 1 — Declarative

The entire desired state of the system must be expressed declaratively. Imperative scripts that mutate state outside of a reconciliation loop are not permitted in the delivery path.

- Declarative tooling in use: `{{DECLARATIVE_TOOLING}}` (e.g., Helm charts, Kustomize overlays, Kubernetes manifests, Bicep, Terraform HCL).
- All configuration must be expressible as code storable in a Git repository.

### Principle 2 — Versioned and Immutable

The desired state must be stored in a version control system that enforces immutability and preserves history.

- Authoritative Git repository: `{{GIT_REPO}}`.
- History must be immutable: force-pushes and history rewrites on protected branches are prohibited.
- Every change to desired state requires a traceable commit and, where applicable, a reviewed pull request.

### Principle 3 — Pulled Automatically

Software agents must automatically pull the desired state from the Git repository and apply it to the managed system. Push-based delivery into managed environments is not permitted except during bootstrapping.

- GitOps agent responsible for pull and apply: `{{GITOPS_AGENT}}` (e.g., Flux, Argo CD, a custom controller).
- Agents must authenticate to the Git repository using least-privilege credentials.

### Principle 4 — Continuously Reconciled

Software agents must continuously and automatically compare the actual state of the system with the desired state and correct any divergence.

- Reconciliation interval: `{{RECONCILIATION_INTERVAL}}` (e.g., `1m`, `5m`; shorter intervals reduce drift window).
- Reconciliation failures must generate an alert within `{{DRIFT_NOTIFICATION_SLA}}`.

## Implementation Requirements

### GitOps Operator

- Operator in use: `{{GITOPS_OPERATOR}}` (Flux / Argo CD / other — specify version).
- The operator must be deployed and maintained in-cluster; its own configuration must itself be managed via GitOps.

### Environment Repository Structure

- Repository layout: `{{ENV_REPO_STRUCTURE}}` (e.g., `clusters/<name>/`, `envs/<name>/`, monorepo with path-based separation).
- Application manifests and environment-specific overrides must be stored at declared paths and must not be generated at runtime outside of the reconciliation loop.

### Secrets Management

- Secrets must never be stored as plaintext in the Git repository.
- Secrets management solution: `{{SECRETS_MANAGER}}` (e.g., Sealed Secrets, SOPS, External Secrets Operator, Vault).
- Encrypted or reference-based secrets may be committed; plaintext values are prohibited.

## Drift Detection Policy

Drift is any difference between actual runtime state and the desired state recorded in Git.

- The GitOps agent must detect and report drift continuously per Principle 4.
- Unresolved drift must trigger a notification within `{{DRIFT_NOTIFICATION_SLA}}` (e.g., `5m`, `15m`).
- Drift reports must be observable in `{{PIPELINE_ALERT_CHANNEL}}`.

## Manual Intervention Procedure

Manual changes to managed environments are permitted only in declared emergencies.

- Emergency changes must be documented with justification before or immediately after the change.
- A follow-up pull request that brings the Git repository in sync with the emergency change must be created and merged within `{{MANUAL_CHANGE_FOLLOWUP}}` (e.g., `4h`, `next business day`).
- Failure to create the follow-up PR is treated as a policy violation and triggers an incident review.

## Source Attribution

- Source manifests: `platform__gitops.md`, `governance__github_docs.md`
- Primary source basis: OpenGitOps v1.0 (gitops.tech)
- Alignment mode: direct-adaptation
- Reviewed on: 2026-03-30
