## Summary
- Replace bullets with a short summary of what this PR is doing.
- Mention which reusable governance artifact or automation scope is affected.

## Testing
- Describe how to run `python scripts/validate_governance_artifacts.py` locally and how `.github/workflows/validate-governance-artifacts.yml` covers the same checks in CI.
- Note any environment variables or secrets (`{{GITHUB_TOKEN}}`, `{{ENV_NAME}}`) that the validation requires.

## Automation & AI Notes
- List any GitHub Actions, issue forms, or AI automation hooks that rely on this change.
- Specify the placeholders (`{{PLACEHOLDER_NAME}}`) downstream repos must configure before adoption.

## Checklist
- [ ] I have confirmed the selective instantiation rule with the requester.
- [ ] I added or updated `## Source Attribution` as required.
- [ ] I followed the placeholder conventions and kept content parameterised.

<!-- Source Attribution: governance__github_docs.md; GitHub Docs + Open Source Guides; direct-adaptation; Reviewed on 2026-03-27 -->
