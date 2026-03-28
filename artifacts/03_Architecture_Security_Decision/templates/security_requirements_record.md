---
title: Security Requirements Record Template
artifact_type: template
status: public-draft
visibility: public
classification: public
owner: architecture-platform
review_cadence: quarterly
applies_to: design and delivery security requirements that must be tracked explicitly
source_basis: OWASP ASVS (Application Security Verification Standard) 4.0
source_manifests:
  - platform__microsoft_learn.md
  - operations__nist_cisa.md
alignment_mode: direct-adaptation
updated: 2026-03-27
---

## Purpose

Record security requirements in a form that can be traced to the design, implementation, and validation work that satisfies them. This template is structured around the OWASP Application Security Verification Standard (ASVS) 4.0 categories, which provide a complete and testable security requirements framework.

## Template

---

### Record metadata

- **Record ID:** `{{RECORD_ID}}`
- **Date:** `{{RECORD_DATE}}`
- **Author:** `{{AUTHOR}}`
- **System context:** `{{SYSTEM_CONTEXT}}`
- **ASVS target level:** `{{ASVS_LEVEL}}` (1 = automated/opportunistic | 2 = standard software | 3 = high-value/high-trust)
- **Related threat model:** `{{THREAT_MODEL_ID}}`
- **Related ADR:** `ADR-{{ADR_REFERENCE}}`
- **Acceptance criteria:** `{{ACCEPTANCE_CRITERIA}}`

---

### How to use this template

1. Select the ASVS target level (`{{ASVS_LEVEL}}`) appropriate for the system's risk profile.
2. For each ASVS category below, add rows for the requirements that apply to this system.
3. Set the status for each requirement: `required` | `out-of-scope` | `deferred`.
4. For `out-of-scope` or `deferred` entries, document the rationale.
5. Link each implemented requirement to the evidence (test, code reference, or audit record) that satisfies it.

---

### Requirements table

Each requirement row follows this structure:

| Req ID | ASVS ID | Category | Requirement description | Verification method | Status |
|---|---|---|---|---|---|
| `{{REQ_ID}}` | `{{ASVS_ID}}` | `{{ASVS_CATEGORY}}` | `{{REQUIREMENT_DESCRIPTION}}` | `{{VERIFICATION_METHOD}}` | `{{STATUS}}` |

- **Req ID:** local identifier for this record, e.g. `SR-001`
- **ASVS ID:** the ASVS 4.0 control identifier, e.g. `V2.1.1`
- **Verification method:** `{{VERIFICATION_METHOD}}` — how this requirement will be verified (automated test | manual review | penetration test | code review | configuration audit)
- **Status:** `required` | `out-of-scope` | `deferred`

---

### V1 — Architecture, Design, and Threat Modeling

Requirements in this category ensure that security is considered in the design phase. Add rows from ASVS V1 that apply to `{{SYSTEM_CONTEXT}}`.

| Req ID | ASVS ID | Category | Requirement description | Verification method | Status |
|---|---|---|---|---|---|
| `{{REQ_ID}}` | `V1.x.x` | Architecture | `{{REQUIREMENT_DESCRIPTION}}` | `{{VERIFICATION_METHOD}}` | `{{STATUS}}` |

### V2 — Authentication

Requirements in this category verify that authentication controls are implemented correctly for `{{SYSTEM_CONTEXT}}`.

| Req ID | ASVS ID | Category | Requirement description | Verification method | Status |
|---|---|---|---|---|---|
| `{{REQ_ID}}` | `V2.x.x` | Authentication | `{{REQUIREMENT_DESCRIPTION}}` | `{{VERIFICATION_METHOD}}` | `{{STATUS}}` |

### V3 — Session Management

Requirements in this category verify that sessions are created, managed, and terminated securely.

| Req ID | ASVS ID | Category | Requirement description | Verification method | Status |
|---|---|---|---|---|---|
| `{{REQ_ID}}` | `V3.x.x` | Session Management | `{{REQUIREMENT_DESCRIPTION}}` | `{{VERIFICATION_METHOD}}` | `{{STATUS}}` |

### V4 — Access Control

Requirements in this category verify that access control policies are enforced correctly.

| Req ID | ASVS ID | Category | Requirement description | Verification method | Status |
|---|---|---|---|---|---|
| `{{REQ_ID}}` | `V4.x.x` | Access Control | `{{REQUIREMENT_DESCRIPTION}}` | `{{VERIFICATION_METHOD}}` | `{{STATUS}}` |

### V5 — Validation, Sanitization, and Encoding

Requirements in this category verify that all input is validated and all output is encoded to prevent injection and related vulnerabilities.

| Req ID | ASVS ID | Category | Requirement description | Verification method | Status |
|---|---|---|---|---|---|
| `{{REQ_ID}}` | `V5.x.x` | Validation | `{{REQUIREMENT_DESCRIPTION}}` | `{{VERIFICATION_METHOD}}` | `{{STATUS}}` |

### V7 — Error Handling and Logging

Requirements in this category verify that errors are handled securely and that security-relevant events are logged.

| Req ID | ASVS ID | Category | Requirement description | Verification method | Status |
|---|---|---|---|---|---|
| `{{REQ_ID}}` | `V7.x.x` | Error Handling | `{{REQUIREMENT_DESCRIPTION}}` | `{{VERIFICATION_METHOD}}` | `{{STATUS}}` |

### V8 — Data Protection

Requirements in this category verify that sensitive data is protected at rest and in transit.

| Req ID | ASVS ID | Category | Requirement description | Verification method | Status |
|---|---|---|---|---|---|
| `{{REQ_ID}}` | `V8.x.x` | Data Protection | `{{REQUIREMENT_DESCRIPTION}}` | `{{VERIFICATION_METHOD}}` | `{{STATUS}}` |

### V9 — Communications Security

Requirements in this category verify that all communications use current and correctly configured protocols.

| Req ID | ASVS ID | Category | Requirement description | Verification method | Status |
|---|---|---|---|---|---|
| `{{REQ_ID}}` | `V9.x.x` | Communications | `{{REQUIREMENT_DESCRIPTION}}` | `{{VERIFICATION_METHOD}}` | `{{STATUS}}` |

### V10 — Malicious Code

Requirements in this category verify that the codebase does not contain malicious or unintended back-doors.

| Req ID | ASVS ID | Category | Requirement description | Verification method | Status |
|---|---|---|---|---|---|
| `{{REQ_ID}}` | `V10.x.x` | Malicious Code | `{{REQUIREMENT_DESCRIPTION}}` | `{{VERIFICATION_METHOD}}` | `{{STATUS}}` |

### V12 — Files and Resources

Requirements in this category verify that file upload, download, and processing are handled securely.

| Req ID | ASVS ID | Category | Requirement description | Verification method | Status |
|---|---|---|---|---|---|
| `{{REQ_ID}}` | `V12.x.x` | Files and Resources | `{{REQUIREMENT_DESCRIPTION}}` | `{{VERIFICATION_METHOD}}` | `{{STATUS}}` |

### V13 — API and Web Service

Requirements in this category verify that APIs are secure by design and by default.

| Req ID | ASVS ID | Category | Requirement description | Verification method | Status |
|---|---|---|---|---|---|
| `{{REQ_ID}}` | `V13.x.x` | API | `{{REQUIREMENT_DESCRIPTION}}` | `{{VERIFICATION_METHOD}}` | `{{STATUS}}` |

### V14 — Configuration

Requirements in this category verify that security configuration is hardened and that defaults are safe.

| Req ID | ASVS ID | Category | Requirement description | Verification method | Status |
|---|---|---|---|---|---|
| `{{REQ_ID}}` | `V14.x.x` | Configuration | `{{REQUIREMENT_DESCRIPTION}}` | `{{VERIFICATION_METHOD}}` | `{{STATUS}}` |
### V6 — Stored Cryptography

Requirements in this category verify that stored cryptographic secrets are managed securely.

| Req ID | ASVS ID | Category | Requirement description | Verification method | Status |
|---|---|---|---|---|---|
| `{{REQ_ID}}` | `V6.x.x` | Stored Cryptography | `{{REQUIREMENT_DESCRIPTION}}` | `{{VERIFICATION_METHOD}}` | `{{STATUS}}` |

### V11 — Business Logic

Requirements in this category verify that business logic is free of security vulnerabilities.

| Req ID | ASVS ID | Category | Requirement description | Verification method | Status |
|---|---|---|---|---|---|
| `{{REQ_ID}}` | `V11.x.x` | Business Logic | `{{REQUIREMENT_DESCRIPTION}}` | `{{VERIFICATION_METHOD}}` | `{{STATUS}}` |

---

### Acceptance criteria summary

Restate the acceptance criteria for this record: `{{ACCEPTANCE_CRITERIA}}`. All requirements with status `required` must be verified before the system is considered compliant with the target ASVS level.

---

## Guidance

- Keep requirements specific, testable, and linked to the threat model or architecture record.
- Use the same Req ID across downstream implementation and review artifacts.
- At ASVS Level 1, automated scanning is the primary verification method; at Level 2, code review and functional testing are expected; at Level 3, architecture review and penetration testing are required.
- `out-of-scope` entries must include a documented rationale; they are not a mechanism to silently skip requirements.

## Source Attribution

- Source manifests: `platform__microsoft_learn.md`, `operations__nist_cisa.md`
- Primary source basis: OWASP ASVS (Application Security Verification Standard) 4.0
- Alignment mode: direct-adaptation
- Reviewed on: 2026-03-27
