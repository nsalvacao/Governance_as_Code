---
title: Issue Forms and Issue Templates
artifact_type: template
status: public
visibility: public
classification: public
owner: quality-platform
review_cadence: quarterly
applies_to: issue intake for bugs, requests, incidents, and investigations
source_basis: GitHub Docs issue forms guidance
source_manifests:
  - governance__github_docs.md
alignment_mode: direct-adaptation
updated: 2026-03-30
---

## Purpose

Provide reusable GitHub issue form definitions (YAML-based structured intake) so each request type arrives with the minimum fields needed to route, triage, and act.

## Issue Form: Bug Report

```yaml
# .github/ISSUE_TEMPLATE/bug_report.yml
name: Bug Report
description: Report a reproducible defect
title: "[BUG] {{BUG_TITLE}}"
labels: ["bug", "{{BUG_LABEL}}"]
assignees:
  - "{{DEFAULT_ASSIGNEE}}"
body:
  - type: markdown
    attributes:
      value: "Please complete all fields to help us reproduce and fix the issue."
  - type: input
    id: version
    attributes:
      label: Version
      placeholder: "{{VERSION_PLACEHOLDER}}"
    validations:
      required: true
  - type: textarea
    id: description
    attributes:
      label: Bug Description
      description: "{{BUG_DESCRIPTION_GUIDANCE}}"
    validations:
      required: true
  - type: textarea
    id: reproduction
    attributes:
      label: Steps to Reproduce
      value: |
        1. {{STEP_1}}
        2. {{STEP_2}}
        3. See error: {{EXPECTED_VS_ACTUAL}}
    validations:
      required: true
  - type: textarea
    id: environment
    attributes:
      label: Environment
      placeholder: "OS: {{OS}}, Runtime: {{RUNTIME_VERSION}}, Config: {{CONFIG_SUMMARY}}"
```

## Issue Form: Change Request

```yaml
# .github/ISSUE_TEMPLATE/change_request.yml
name: Change Request
description: Request a new feature or enhancement
title: "[CHANGE] {{CHANGE_TITLE}}"
labels: ["enhancement", "{{CHANGE_LABEL}}"]
body:
  - type: textarea
    id: motivation
    attributes:
      label: Motivation
      description: Why is this change needed? What problem does it solve?
      placeholder: "{{MOTIVATION_PLACEHOLDER}}"
    validations:
      required: true
  - type: textarea
    id: proposal
    attributes:
      label: Proposed Solution
      placeholder: "{{SOLUTION_PLACEHOLDER}}"
    validations:
      required: true
  - type: dropdown
    id: priority
    attributes:
      label: Priority
      options:
        - "{{PRIORITY_HIGH}}"
        - "{{PRIORITY_MEDIUM}}"
        - "{{PRIORITY_LOW}}"
    validations:
      required: true
```

## Issue Form: Incident Report

```yaml
# .github/ISSUE_TEMPLATE/incident_report.yml
name: Incident Report
description: Report a production incident or service degradation
title: "[INCIDENT] {{INCIDENT_TITLE}}"
labels: ["incident", "{{SEVERITY_LABEL}}"]
body:
  - type: dropdown
    id: severity
    attributes:
      label: Severity
      options:
        - "SEV1 — Complete outage"
        - "SEV2 — Major degradation"
        - "SEV3 — Partial degradation"
        - "SEV4 — Minor issue"
    validations:
      required: true
  - type: input
    id: start_time
    attributes:
      label: Incident Start Time (UTC)
      placeholder: "{{START_TIME_PLACEHOLDER}}"
    validations:
      required: true
  - type: textarea
    id: impact
    attributes:
      label: Customer Impact
      placeholder: "{{IMPACT_PLACEHOLDER}}"
    validations:
      required: true
  - type: textarea
    id: status
    attributes:
      label: Current Status
      placeholder: "{{STATUS_PLACEHOLDER}}"
```

## Template Configuration

```yaml
# .github/ISSUE_TEMPLATE/config.yml
blank_issues_enabled: {{BLANK_ISSUES_ENABLED}}
contact_links:
  - name: "{{SUPPORT_LINK_NAME}}"
    url: "{{SUPPORT_URL}}"
    about: "{{SUPPORT_LINK_ABOUT}}"
  - name: "{{SECURITY_LINK_NAME}}"
    url: "{{SECURITY_URL}}"
    about: "Report security vulnerabilities privately"
```

## Guidance

- Keep each form's fields to the minimum needed to route and triage.
- Use `validations: required: true` for fields without which the issue cannot be acted on.
- Align label values with your project's label taxonomy in `{{LABEL_TAXONOMY_DOC}}`.

## Source Attribution

- Source manifests: `governance__github_docs.md`
- Primary source basis: GitHub Docs issue forms guidance
- Alignment mode: direct-adaptation
- Reviewed on: 2026-03-30
