---
title: Pull Request Template
artifact_type: template
status: public
visibility: public
classification: public
owner: GOVERNANCE
review_cadence: quarterly
applies_to: reusable_governance
source_basis: GitHub Docs
source_manifests: governance__github_docs.md
alignment_mode: direct-adaptation
updated: 2026-03-30
---

<!-- Pull Request Template — instantiate per repository; fill all {{PLACEHOLDER}} values before publishing -->

## Change Type

<!-- Select all that apply -->

- [ ] `feat` — new artifact or capability
- [ ] `fix` — correction to existing artifact (frontmatter, validator, broken link)
- [ ] `docs` — documentation update (README, decision log, governance docs)
- [ ] `chore` — maintenance (dependency update, file rename, reformatting)
- [ ] `refactor` — restructure without functional change
- [ ] `ci` — workflow or automation change

## Summary

<!-- 2–5 bullet points describing WHAT changed and WHY -->

- `{{CHANGE_DESCRIPTION_1}}`
- `{{CHANGE_DESCRIPTION_2}}`

**Scope**: <!-- select one: instance | artifact library | both -->

**Affected dimension(s)**: `{{ARTIFACT_DIMENSION}}` (e.g., operations, platform, risk)

**Related issue / ADR**: closes #`{{ISSUE_NUMBER}}`

## Validation Evidence

<!-- Paste the exact output of running the validator locally -->

```
python3 scripts/validate_governance_artifacts.py
```

Output:
```
{{VALIDATOR_OUTPUT}}
```

Exit code: `{{EXIT_CODE}}`

## Testing Evidence

| Test Type | Method | Result |
|---|---|---|
| Governance validation | `python3 scripts/validate_governance_artifacts.py` | `{{VALIDATOR_RESULT}}` |
| Manual review | Verified sections match canonical framework | `{{MANUAL_REVIEW_RESULT}}` |
| CI workflow | `{{WORKFLOW_NAME}}` | `{{CI_RESULT}}` |

## Breaking Changes

<!-- Does this change affect frontmatter keys, validator rules, or downstream instantiation? -->

- [ ] No breaking changes
- [ ] **Breaking** — describe impact: `{{BREAKING_CHANGE_DESCRIPTION}}`

Downstream repos affected: `{{DOWNSTREAM_REPOS_AFFECTED}}`

## Automation and AI Notes

<!-- List any GitHub Actions, issue forms, or AI automation hooks that rely on this change -->

- `{{AUTOMATION_NOTE_1}}`
- `{{AUTOMATION_NOTE_2}}`

Placeholders downstream repos must configure: `{{PLACEHOLDER_LIST}}`

## Self-Review Checklist

<!-- Complete ALL items before requesting review -->

- [ ] Change is scoped correctly (`instance` / `artifact library` / `both`)
- [ ] All `{{PLACEHOLDER}}` values use `{{UPPER_SNAKE_CASE}}` convention
- [ ] `## Source Attribution` added or updated with correct reviewed-on date
- [ ] Frontmatter includes all 11 required keys
- [ ] Validator passes locally — output pasted above
- [ ] No private/sensitive content in public artifact body
- [ ] PR title follows Conventional Commits: `<type>(scope): <description>`
- [ ] Appropriate labels applied (`area:{{DIMENSION}}`, classification label)

<!-- Source Attribution: governance__github_docs.md; GitHub Docs + Open Source Guides; direct-adaptation; Reviewed on 2026-03-27 -->
