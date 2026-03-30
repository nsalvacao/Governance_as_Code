---
title: Pull Request Template
artifact_type: template
status: public
visibility: public
classification: public
owner: quality-platform
review_cadence: quarterly
applies_to: pull request submission and review preparation
source_basis: GitHub Docs pull request template guidance
source_manifests:
  - governance__github_docs.md
alignment_mode: direct-adaptation
updated: 2026-03-30
---

## Purpose

Standardize the information a contributor provides when proposing a change, following GitHub Docs PR template best practices.

## Template Body

```markdown
## Summary

<!-- What does this PR do? Why is it needed? -->
{{PR_SUMMARY}}

## Change Type

<!-- Check all that apply -->
- [ ] Bug fix (non-breaking change that resolves an issue)
- [ ] New feature (non-breaking change that adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to change)
- [ ] Documentation update
- [ ] Refactor / internal improvement
- [ ] Configuration / infrastructure change

## Related Issues

<!-- Link any related issues or tickets -->
Closes #{{ISSUE_NUMBER}}
Related: {{RELATED_LINKS}}

## Testing Evidence

<!-- Describe the tests you ran. Include commands, screenshots, or links to CI results. -->

| Test Type | Command / Link | Result |
|---|---|---|
| Unit tests | `{{UNIT_TEST_COMMAND}}` | {{UNIT_TEST_RESULT}} |
| Integration tests | `{{INTEGRATION_TEST_COMMAND}}` | {{INTEGRATION_TEST_RESULT}} |
| Manual verification | `{{MANUAL_TEST_STEPS}}` | {{MANUAL_TEST_RESULT}} |
| Validator | `python3 scripts/validate_governance_artifacts.py` | {{VALIDATOR_RESULT}} |

## Breaking Changes

<!-- If this is a breaking change, describe the impact and migration path. -->
{{BREAKING_CHANGE_DESCRIPTION}}

## Checklist

- [ ] I have read `CONTRIBUTING.md`
- [ ] My changes follow the coding standards in `artifacts/01_Governance_Method/standards/coding_standards.md`
- [ ] I have added/updated tests where applicable
- [ ] All status checks pass
- [ ] I have updated documentation if necessary
- [ ] I have reviewed the security implications of my change
- [ ] For Automation/AI-generated content: I have reviewed and take responsibility for the output

## Notes for Reviewers

{{REVIEWER_NOTES}}
```

## Field Guidance

| Field | Purpose | Required? |
|---|---|---|
| `{{PR_SUMMARY}}` | Concise description of change and motivation | Yes |
| `{{ISSUE_NUMBER}}` | Traceability to backlog/issue tracker | Yes when applicable |
| Testing evidence table | Reproducible validation proof | Yes |
| `{{BREAKING_CHANGE_DESCRIPTION}}` | Migration path for consumers | Yes if breaking |
| Checklist | Self-review gate before review request | Yes |

## Guidance

- Keep the summary concise: what changed and why, not how.
- Point to validation evidence (commands, CI links), not just intent.
- For AI-assisted changes, explicitly confirm human review of all generated content.

## Source Attribution

- Source manifests: `governance__github_docs.md`
- Primary source basis: GitHub Docs pull request template guidance
- Alignment mode: direct-adaptation
- Reviewed on: 2026-03-30
