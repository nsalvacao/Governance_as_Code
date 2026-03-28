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

# Contributing to `{{REPOSITORY_NAME}}`

Thank you for contributing! This guide explains how to contribute to `{{REPOSITORY_NAME}}`.

*Based on GitHub Open Source Guides contribution guidance.*

---

## Types of Contributions

We welcome the following contributions:

| Type | Description | How to start |
|---|---|---|
| Bug fix | Correct a broken artifact, validator issue, or broken link | Open an issue, then PR |
| New artifact | Add a template, standard, policy, or schema | Discuss in an issue first |
| Artifact improvement | Enrich an existing artifact body to better match its canonical framework | PR with scope note |
| Documentation | Update README, decision log, or governance docs | PR |
| Automation | Improve workflows, issue forms, or validation scripts | Issue → PR |
| Question | Pre-flight questions or clarifications | `{{DISCUSSION_CHANNEL}}` |

For large or structural changes, **open an issue first** to discuss your approach before investing time in a PR.

---

## Getting Started

### Prerequisites

- Python `≥ {{MIN_PYTHON_VERSION}}` (standard library only — no extra packages)
- Git

### Setup

```bash
git clone https://github.com/{{ORG_NAME}}/{{REPOSITORY_SLUG}}.git
cd {{REPOSITORY_SLUG}}
# Run validation to confirm baseline
python3 scripts/validate_governance_artifacts.py
```

Expected output: `Validator: OK (no issues found).`

---

## Your First Contribution

1. **Find something to work on**: look for issues labelled `good first issue` or `help wanted`.
2. **Comment on the issue** to claim it — this prevents duplicate work.
3. **Create a branch**:
   ```bash
   git checkout -b {{BRANCH_PREFIX}}/short-description
   ```
4. **Make your changes** — see Authoring Rules below.
5. **Validate** — must pass before opening a PR:
   ```bash
   python3 scripts/validate_governance_artifacts.py
   ```
6. **Commit** using Conventional Commits: `feat`, `fix`, `docs`, `chore`, `refactor`, `ci`.
7. **Open a PR** using `.github/PULL_REQUEST_TEMPLATE.md`.

---

## Authoring Rules

Following the placeholder and traceability conventions of this repository:

| Rule | Detail |
|---|---|
| Placeholder convention | Use `{{UPPER_SNAKE_CASE}}` for all instance-specific values |
| Source Attribution | Every Markdown artifact MUST end with `## Source Attribution` |
| Frontmatter | All 11 required keys must be present (see `artifacts/01_Governance_Method/schemas/frontmatter.schema.json`) |
| Canonical faithfulness | Artifact body must structurally follow its stated canonical framework |
| Path placement | `artifacts/<dimension>/<artifact-type>/` — no other locations |
| No private content | Never include private rationale, operational secrets, or personal details |
| Minimal changes | Prefer editing existing files over creating new ones |

---

## Pull Request Process

1. Open PR using `.github/PULL_REQUEST_TEMPLATE.md` — fill all sections.
2. Apply labels:
   - `area:{{DIMENSION_LABEL}}` (e.g., `area:operations`, `area:risk`)
   - Classification: `public`, `public-redacted`, or `private`
3. CI must pass: the `{{CI_WORKFLOW_NAME}}` workflow runs `validate_governance_artifacts.py`.
4. A review from `{{GOVERNANCE_TEAM}}` is required — `{{MIN_REVIEWERS}}` approvals needed.
5. **Do not merge your own PR** unless you are a maintainer and `{{SELF_MERGE_POLICY}}`.
6. Address all review comments before requesting re-review.

---

## Code Review Expectations

**Reviewers** (following Google Engineering Practices):

| Review dimension | What to check |
|---|---|
| Design | Does the artifact fit the existing topology? |
| Correctness | Are placeholders, sections, and Source Attribution conforming to standards? |
| Completeness | Are all frontmatter keys present and correct? |
| Style | Does it match neighboring artifacts? |
| Automation impact | Does it affect CI, validator, or downstream consumers? |

- Provide actionable feedback or approval within `{{REVIEW_SLA}}`.
- Be specific — link to the relevant standard or convention rather than citing vague style preferences.

**Authors**:
- Respond to every comment — even if just confirming it was addressed.
- Commit fixes as separate commits during review; do not force-push to avoid losing diff context.

---

## Reporting Issues

Use the structured intake forms in `.github/ISSUE_TEMPLATE/`:

| Issue type | Template |
|---|---|
| Bug / validation failure | Bug report form |
| Change request | Change request form |
| Security concern | Email `{{SECURITY_CONTACT}}` — do NOT open a public issue |
| Question | `{{DISCUSSION_CHANNEL}}` or Support |

---

## Community

This project follows the [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you agree to uphold it.

Questions? `{{SUPPORT_CHANNEL}}` — see `SUPPORT.md`.

## Source Attribution

- Source manifests: `governance__github_docs.md`
- Primary source basis: GitHub Open Source Guides (opensource.guide/how-to-contribute) + GitHub Docs contribution guidance
- Alignment mode: `hybrid-synthesis`
- Reviewed on: 2026-03-27
