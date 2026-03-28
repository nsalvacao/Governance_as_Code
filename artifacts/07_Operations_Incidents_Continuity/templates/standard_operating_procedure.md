---
title: Standard Operating Procedure
artifact_type: template
status: public-draft
visibility: public
classification: public
owner: "{{OWNER_NAME}}"
review_cadence: quarterly
applies_to: stable operational processes
source_basis: ISO 9001 quality management system structure and Google SRE operational practice
source_manifests:
  - operations__nist_cisa.md
  - operations__google_sre.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
---

## Purpose

Capture the stable, repeatable procedure for a routine operational process. An SOP defines the single approved way to execute a process, ensuring consistency regardless of who performs it.

---

## SOP Metadata

| Field | Value |
|---|---|
| SOP ID | `{{SOP_ID}}` |
| Title | `{{SOP_TITLE}}` |
| Version | `{{VERSION}}` |
| Owner | `{{OWNER}}` |
| Effective date | `{{EFFECTIVE_DATE}}` |

Assign a unique SOP ID to enable cross-referencing from runbooks, playbooks, and incident reports. Version the document on every substantive change.

---

## Purpose and Scope

`{{PURPOSE}}`

State what process this SOP governs, why it exists, and what outcome successful execution produces. Keep the purpose to two or three sentences — if it requires more, consider splitting into multiple SOPs.

---

## Applicability

`{{APPLICABILITY}}`

Specify which teams, systems, environments, or conditions this SOP applies to. Also state explicitly what this SOP does not cover to prevent scope creep during execution.

---

## Prerequisites

**Access required:** `{{ACCESS_REQUIREMENT}}`

**Tools needed:**

| # | Tool |
|---|------|
| 1 | `{{TOOL_1}}` |
| 2 | `{{TOOL_2}}` |
| N | `{{TOOL_N}}` |

**Dependencies:**

| # | Dependency |
|---|-----------|
| 1 | `{{DEPENDENCY_1}}` |
| 2 | `{{DEPENDENCY_2}}` |
| N | `{{DEPENDENCY_N}}` |

Confirm all prerequisites before starting. If a dependency is unavailable, do not proceed — escalate to the SOP owner.

---

## Procedure Steps

Execute in strict order. Do not skip steps or reorder unless the SOP explicitly permits it.

| Step | Action | Responsible role | Checkpoint |
|------|--------|-----------------|------------|
| 1 | `{{ACTION_1}}` | `{{ROLE_1}}` | `{{CHECKPOINT_CRITERIA_1}}` |
| 2 | `{{ACTION_2}}` | `{{ROLE_2}}` | `{{CHECKPOINT_CRITERIA_2}}` |
| 3 | `{{ACTION_3}}` | `{{ROLE_3}}` | `{{CHECKPOINT_CRITERIA_3}}` |
| N | `{{ACTION_N}}` | `{{ROLE_N}}` | `{{CHECKPOINT_CRITERIA_N}}` |

Each step with a checkpoint requires positive confirmation before proceeding. If a checkpoint fails, stop and refer to the Exception Handling section.

---

## Verification Checkpoints

| Checkpoint | Criteria | Pass determination | Fail determination |
|-----------|----------|-------------------|-------------------|
| 1 | `{{CHECKPOINT_CRITERIA_1}}` | `{{PASS_1}}` | `{{FAIL_1}}` |
| 2 | `{{CHECKPOINT_CRITERIA_2}}` | `{{PASS_2}}` | `{{FAIL_2}}` |
| N | `{{CHECKPOINT_CRITERIA_N}}` | `{{PASS_N}}` | `{{FAIL_N}}` |

Pass/fail criteria must be objective. If determination requires judgment, document the criteria used to make that judgment — not just the outcome.

---

## Exception Handling

| Exception | Response |
|-----------|----------|
| `{{EXCEPTION_1}}` | `{{EXCEPTION_RESPONSE_1}}` |
| `{{EXCEPTION_2}}` | `{{EXCEPTION_RESPONSE_2}}` |
| `{{EXCEPTION_N}}` | `{{EXCEPTION_RESPONSE_N}}` |

Document known failure modes and their prescribed responses. An undocumented exception will be handled inconsistently. Escalate exceptions not covered here to the SOP owner before proceeding.

---

## References

| # | Reference |
|---|-----------|
| 1 | `{{REFERENCE_1}}` |
| 2 | `{{REFERENCE_2}}` |
| N | `{{REFERENCE_N}}` |

Link to related runbooks, playbooks, upstream SOPs, or regulatory requirements. References must be versioned where applicable.

---

## Change History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| `{{VER_1}}` | `{{DATE_1}}` | `{{AUTHOR_1}}` | `{{CHANGES_1}}` |
| `{{VER_N}}` | `{{DATE_N}}` | `{{AUTHOR_N}}` | `{{CHANGES_N}}` |

Maintain a complete change history. Every change must state what changed and why. Use this log to audit whether the SOP reflects current practice.

---

## Source Attribution

- Source manifests: operations__nist_cisa.md, operations__google_sre.md
- Primary source basis: ISO 9001 quality management system structure and Google SRE operational practice
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27
