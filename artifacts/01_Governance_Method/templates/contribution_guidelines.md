---
title: Contribution Guidelines
artifact_type: template
status: public
visibility: public
classification: public
owner: "{{OWNER_NAME}}"
review_cadence: quarterly
applies_to: contributor-facing repository entry points
source_basis: GitHub Docs and Open Source Guides contribution guidance
source_manifests:
  - governance__github_docs.md
alignment_mode: hybrid-synthesis
updated: 2026-03-30
---

## Purpose

Provide the reusable public guidance for how contributors should propose, review, and submit changes to a governance artifact repository. This template is instantiated per repository; replace all `{{PLACEHOLDER}}` values before publishing.

---

## Types of Contributions

| Contribution Type | Description | Entry Point |
|---|---|---|
| New artifact | Adding a template, standard, policy, or schema | Issue → PR |
| Artifact update | Improving an existing artifact body or frontmatter | PR with scope note |
| Bug / validator fix | Correcting frontmatter, broken links, or validator failures | Issue → PR |
| Automation update | Modifying workflows, issue forms, or scripts | Issue → PR |
| Documentation | Updating README, decision log, or governance docs | PR |
| Question / discussion | Pre-flight or clarification questions | `{{DISCUSSION_CHANNEL}}` |

---

## Before You Start

1. Check the issue tracker and open PRs to avoid duplicate work on `{{ARTIFACT_IN_SCOPE}}`.
2. Confirm the artifact classification: `public` / `public-redacted` / `private` — consult the repository map.
3. Pull the latest `{{DEFAULT_BRANCH}}` and run local validation:
   ```
   python3 scripts/validate_governance_artifacts.py
   ```
4. Identify the correct artifact path: `artifacts/<dimension>/<artifact-type>/` — see `artifacts/README.md`.
5. If your change affects downstream repositories, document the impact in the PR description.

---

## Environment Setup

| Prerequisite | Version / Notes | Verification |
|---|---|---|
| Python | ≥ `{{MIN_PYTHON_VERSION}}` (3.x) | `python3 --version` |
| Git | ≥ `{{MIN_GIT_VERSION}}` | `git --version` |
| GitHub CLI | Optional — for PR creation | `gh --version` |
| `{{ADDITIONAL_TOOL_1}}` | `{{TOOL_1_VERSION}}` | `{{TOOL_1_VERIFY_CMD}}` |

No external packages required for validation — standard library only.

---

## Contribution Workflow

1. **Fork or branch**: create a feature branch from `{{DEFAULT_BRANCH}}`:
   ```
   git checkout -b {{BRANCH_PREFIX}}/{{FEATURE_SLUG}}
   ```
2. **Apply changes**: follow the authoring rules below.
3. **Validate locally**: `python3 scripts/validate_governance_artifacts.py` must exit `0`.
4. **Commit**: use Conventional Commits — `feat`, `fix`, `docs`, `chore`, `refactor`.
5. **Open PR**: use `.github/PULL_REQUEST_TEMPLATE.md`; fill all sections.
6. **Respond to review**: address all comments; do NOT merge until CI passes and `{{MIN_REVIEWERS}}` approvals are received.

---

## Authoring Rules

- Use `{{UPPER_SNAKE_CASE}}` placeholders for all instance-specific values.
- Never leave unresolved placeholders in root instance documents.
- Every Markdown artifact MUST include a `## Source Attribution` section citing the canonical framework.
- Frontmatter MUST include all 11 required keys: `title`, `artifact_type`, `status`, `visibility`, `classification`, `owner`, `review_cadence`, `applies_to`, `source_basis`, `source_manifests`, `alignment_mode`, `updated`.
- Keep artifact body structurally faithful to its stated canonical framework.
- Prefer editing existing files over creating new ones.
- Automation artifacts (workflows, issue forms) must document all required inputs and secrets.

---

## Pull Request Standards

| Field | Expectation |
|---|---|
| Title | Conventional Commit format: `<type>(scope): <description>` |
| Summary | What changed, why, and which artifact dimension is affected |
| Scope | Clearly state: `instance` / `artifact library` / `both` |
| Validation evidence | Paste `python3 scripts/validate_governance_artifacts.py` output |
| Breaking changes | Explicitly flag any frontmatter key changes or validator rule changes |
| Labels | Apply `area:{{DIMENSION_LABEL}}` and classification label |

---

## Code Review Expectations

Following GitHub Engineering Practices:

| Reviewer responsibility | Description |
|---|---|
| Design | Does the change fit the existing artifact topology and governance model? |
| Functionality | Do placeholders, sections, and Source Attribution conform to standards? |
| Completeness | Are all required frontmatter keys present and correct? |
| Consistency | Does the style match neighboring artifacts in the same dimension? |
| Automation impact | Does the change affect CI, validator, or downstream workflows? |

- Reviewers: provide actionable feedback or approval within `{{REVIEW_SLA}}`.
- Authors: respond to all review comments before requesting re-review.
- Resolve all threads before merging.

---

## Escalation

| Situation | Route |
|---|---|
| Validation failure you cannot resolve | Comment on the PR and tag `{{GOVERNANCE_TEAM}}` |
| Unclear artifact scope or classification | Open a discussion in `{{DISCUSSION_CHANNEL}}` |
| Security concern in a contribution | Email `{{SECURITY_CONTACT}}` — do NOT open a public issue |
| Disputed review decision | Escalate to `{{ESCALATION_CONTACT}}` |

## Source Attribution

- Source manifests: governance__github_docs.md
- Primary source basis: GitHub Docs contribution guidance and Open Source Guides
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-30

