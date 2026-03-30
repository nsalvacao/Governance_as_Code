---
title: Automation and AI Execution
artifact_type: normative
status: public
visibility: public
classification: public-redacted
owner: governance@org
review_cadence: quarterly
applies_to: repositories using automation hooks or AI agents
source_basis: documentation__diataxis, platform__aws_well_architected, platform__microsoft_learn, ai_ops__openai_docs
source_manifests: documentation__diataxis.md, platform__aws_well_architected.md, platform__microsoft_learn.md, ai_ops__openai_docs.md
alignment_mode: hybrid-synthesis
updated: 2026-03-30
---

# Automation and AI Execution

This document is a reusable library standard. It governs how downstream repositories should describe and operate automation and AI-assisted flows when they instantiate assets from this repository.

## Scope

This standard applies to all automation pipelines and AI agent executions within `{{APPLIES_TO_SCOPE}}`. It defines what automation and AI agents may do autonomously, what requires human approval, and how all changes must be traced.

Automation rules apply only to repositories where the automation feature is enabled via the `{{AUTOMATION_ENABLED}}` flag. Repositories with this flag set to `false` must not use AI-generated changes in production without first enabling the flag and satisfying all gates in this standard.

## Human-in-the-Loop Gates

The following actions require explicit human approval before execution. Approval must be recorded in the audit trail. The approving role is `{{APPROVAL_LEVEL_1}}` for standard changes and `{{APPROVAL_LEVEL_2}}` for changes with production impact.

Actions requiring human approval (`{{GATE_ACTION_LIST}}`):
- Merging a pull request that was authored or co-authored by an AI agent.
- Deploying any artifact to a production or staging environment.
- Updating governance artifact frontmatter outside of an approved automation workflow.
- Modifying access control configurations (repository permissions, team memberships, secrets).
- Publishing a release or creating a release tag.
- Any action that cannot be fully rolled back within `{{ROLLBACK_TIME_SLA}}`.

Automation must halt and await human approval when it encounters any action in this list. It must not proceed autonomously even if the action appears low-risk based on context.

## Deterministic vs Non-deterministic Boundary

The risk profile of an automated action depends on whether it is deterministic or non-deterministic. This boundary determines where human oversight is required.

**Deterministic** (automation may execute autonomously):
- Linting and static analysis (e.g., running `{{LINT_CONFIG_PATH}}` checks).
- Code formatting (e.g., applying formatter configuration at `{{FORMATTER_CONFIG_PATH}}`).
- Schema validation (e.g., running `python scripts/validate_governance_artifacts.py`).
- Dependency version pinning from a pre-approved lockfile.
- Generating structured outputs from structured inputs using a fixed algorithm.

**Non-deterministic** (human approval required before committing or publishing):
- Content generation: writing, summarizing, or classifying text using a language model.
- Classification or labeling of issues, PRs, or artifacts using AI inference.
- Suggesting or applying code changes based on natural language instructions.
- Any action where the output cannot be fully predicted from the inputs by inspection.

When an action is ambiguous, classify it as non-deterministic and require human approval.

## Audit Trail Requirements for AI-generated Changes

Every AI-generated or AI-assisted change must be traceable. The following requirements apply to all non-deterministic outputs that are committed or published:

- The commit message or PR description must identify the AI model or tool that contributed to the change (e.g., `Co-Authored-By: {{AI_AGENT_NAME}}`).
- The frontmatter `updated` field of any modified artifact must reflect the date of the AI-assisted change.
- A review comment or PR annotation must confirm that a human reviewer verified the AI output before approval.
- Audit log entries at `{{AUDIT_LOG_PATH}}` must record: timestamp, actor (human approver), AI tool used, artifact modified, and approval rationale.

## Rollback Capability Requirement

Every automated change must be designed for rollback. Before an automated workflow runs, it must confirm that:

- The change can be reversed within `{{ROLLBACK_TIME_SLA}}` without data loss or service interruption.
- A rollback procedure is documented at `{{ROLLBACK_RUNBOOK_PATH}}`.
- The rollback procedure has been tested against the previous stable state.

Automated workflows that cannot guarantee rollback capability must be classified as human-gated actions and require explicit approval before execution.

## Approval Authority Levels

| Level | Role | Scope |
|---|---|---|
| `{{APPROVAL_LEVEL_1}}` | Standard reviewer | Non-production, non-breaking changes |
| `{{APPROVAL_LEVEL_2}}` | Senior reviewer or tech lead | Production changes, breaking changes |
| `{{APPROVAL_LEVEL_3}}` | Designated authority | Security-sensitive changes, credential access, destructive operations |

Approval authority must be declared in the repository's `CODEOWNERS` file and enforced via branch protection rules.

## Prohibited Autonomous Actions

The following actions are never permitted without explicit human approval from `{{APPROVAL_LEVEL_3}}`, regardless of automation flags or inferred context:

- Destructive filesystem operations (recursive deletion, directory removal, overwriting without backup).
- Reading, writing, or transmitting credentials, secrets, API keys, or certificates.
- Making external API calls to third-party services not pre-approved in `{{APPROVED_EXTERNAL_SERVICES_LIST}}`.
- Modifying branch protection rules, repository settings, or organization-level configurations.
- Creating, updating, or deleting GitHub Actions secrets or environment variables.
- Any action on behalf of a user identity that is not the automation service account.

Automation that encounters a situation requiring a prohibited action must halt immediately, emit a structured error with context, and notify `{{ESCALATION_CONTACT}}`.

## Automation Descriptions

Every automation pipeline or AI-assisted workflow must document:
- Triggering event (e.g., `workflow_dispatch`, `issue_comment`, `pull_request`).
- Input parameters (`{{UPPER_SNAKE_CASE}}`) and defaults.
- Expected outputs (e.g., validation comment, checklist update).
- Downstream actions (e.g., `{{GOVERNANCE_VALIDATION_WORKFLOW}}`).
- Whether each step is deterministic or non-deterministic (see section above).

Link automation descriptions to `artifacts/01_Governance_Method/templates/partials/source_attribution.md` so attribution travels with results. Preface deterministic steps with "Deterministic step:" to make the boundary explicit.

## AI Agent Guidelines

- Document the surface that agents may read or write, such as frontmatter schema hooking (`artifacts/01_Governance_Method/schemas/frontmatter.schema.json`) and `source_manifests` and `alignment_mode` fields for verification.
- Provide guidance for how agents should interpret placeholders: "Replace `{{PROJECT_NAME}}` before instantiating the template."
- State the fallback behavior when AI detects missing data: "If `{{SERVICE_AREA}}` is unknown, tag as `requires human` and stop before committing changes."
- Outline the verification obligation: agents must run `python scripts/validate_governance_artifacts.py` locally before merging; `.github/workflows/validate-governance-artifacts.yml` enforces the same checks in CI.
- AI-generated content must be attributed in commit messages and PR descriptions (see `## Audit Trail Requirements for AI-generated Changes`).

## Source Attribution

- Source manifests: documentation__diataxis.md, platform__aws_well_architected.md, platform__microsoft_learn.md, ai_ops__openai_docs.md
- Primary source basis: AI safety and human-in-the-loop principles; AWS/Microsoft automation guidance; OpenAI AI ops guidance
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-30
