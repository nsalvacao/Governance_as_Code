---
title: Security Policy
artifact_type: policy
status: public
visibility: public
classification: public
owner: "{{SECURITY_OWNER}}"
review_cadence: semi-annual
applies_to: public_security
source_basis: GitHub Docs
source_manifests: governance__github_docs.md
alignment_mode: direct-adaptation
updated: 2026-03-27
---

# Security Policy

Security reports go to `{{SECURITY_CONTACT}}`. Do not open a public issue for an unpatched or sensitive vulnerability. Use `.github/ISSUE_TEMPLATE/incident_report.yml` only for already-public security incidents, non-sensitive automation failures, or follow-up tracking once disclosure is safe.

## Reporting

1. Contact `{{SECURITY_CONTACT}}` directly if you discover a sensitive vulnerability or abuse pattern that should not be disclosed publicly.
2. File an incident report only when the report is safe to keep in the public corpus.
3. Include the severity, affected automation (if any), and remediation status.
4. Mark the issue with `type: incident` and `label: security`.

## Response

`{{SECURITY_TEAM}}` triages incoming reports within 24 hours. If the issue is actionable for downstream repositories, a `{{SECURITY_TRIAGE_LABEL}}` is applied and the corresponding automation is redlined.

## Source Attribution

- Source manifests: `governance__github_docs.md`
- Primary source basis: GitHub Docs
- Alignment mode: `direct-adaptation`
- Reviewed on: 2026-03-27
