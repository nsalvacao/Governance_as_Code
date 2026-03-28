---
title: Support Guidelines
artifact_type: policy
status: public
visibility: public
classification: public
owner: "{{SUPPORT_OWNER}}"
review_cadence: quarterly
applies_to: contributor_support
source_basis: GitHub Docs
source_manifests: governance__github_docs.md
alignment_mode: direct-adaptation
updated: 2026-03-27
---

# Support

This document describes how to get help with `{{REPOSITORY_NAME}}`.

---

## Request Routing

Use this table to route your request to the right channel:

| Request Type | Description | Channel | Response SLA |
|---|---|---|---|
| Pre-flight question | "Should I use this artifact for X?" or "How do I instantiate Y?" | `{{DISCUSSION_CHANNEL}}` | `{{DISCUSSION_SLA}}` |
| Governance question | "Which classification applies to my repo?" | `{{GOVERNANCE_CHANNEL}}` | `{{GOVERNANCE_SLA}}` |
| Downstream automation error | "The workflow fails when consuming artifact Z" | `{{SUPPORT_CHANNEL}}` | `{{SUPPORT_SLA}}` |
| Placeholder clarification | "What value should `{{PLACEHOLDER_NAME}}` take?" | `{{DISCUSSION_CHANNEL}}` | `{{DISCUSSION_SLA}}` |
| Bug report | Broken validator, invalid frontmatter, broken link | GitHub issue (bug form) | `{{BUG_SLA}}` |
| Change request | Artifact improvement or new artifact proposal | GitHub issue (change form) | `{{CHANGE_REQUEST_SLA}}` |
| Security concern | Potential vulnerability | `{{SECURITY_CONTACT}}` | See `SECURITY.md` |
| Commercial enquiry | Licensing or partnership question | `{{COMMERCIAL_CONTACT}}` | `{{COMMERCIAL_SLA}}` |

---

## When to Use Each Channel

### Use `{{DISCUSSION_CHANNEL}}` for

- Questions not ready to become a formal issue or PR
- Feedback on existing conventions or standards
- Asking whether a proposed approach is appropriate

### Use GitHub Issues for

- Confirmed bugs (use the bug report form)
- Formal change requests (use the change request form)
- Incident reports for already-disclosed issues
- Investigation requests where structured intake adds value

### Use `{{SUPPORT_CHANNEL}}` for

- Downstream automation errors where the consuming repo has followed all instructions correctly
- Time-sensitive operational questions affecting a running repository

### Do NOT use issues for

- Security vulnerabilities — use `{{SECURITY_CONTACT}}` or GitHub private vulnerability reporting (see `SECURITY.md`)
- Pre-flight questions where a discussion thread is more appropriate

---

## Escalation Path

| Level | Condition | Contact |
|---|---|---|
| Level 1 | Initial question or standard request | `{{DISCUSSION_CHANNEL}}` or GitHub issue |
| Level 2 | No response within `{{ESCALATION_TIMEOUT_L1}}` or issue requires maintainer decision | Tag `{{GOVERNANCE_TEAM}}` in the issue or discussion |
| Level 3 | Policy dispute or governance conflict | `{{GOVERNANCE_CONTACT}}` |
| Level 4 | Security or compliance escalation | `{{SECURITY_CONTACT}}` — see `SECURITY.md` |

---

## Out of Scope

The following are out of scope for support in this repository:

- Support for downstream repositories that have diverged from the conventions defined here
- Consulting on how to adapt artifacts beyond their documented instantiation guidance
- Issues originating from `{{OUT_OF_SCOPE_DEPENDENCY}}` — report those upstream

---

## Response Expectations

- Maintainers (`{{GOVERNANCE_TEAM}}`) respond to GitHub issues and discussions within `{{STANDARD_RESPONSE_SLA}}`.
- Community members may respond to discussions at any time.
- SLAs apply to `{{SUPPORT_HOURS}}` hours; critical security reports are handled outside these hours.

## Source Attribution

- Source manifests: `governance__github_docs.md`
- Primary source basis: GitHub Docs support guidance + GitHub Open Source Guides
- Alignment mode: `direct-adaptation`
- Reviewed on: 2026-03-27
