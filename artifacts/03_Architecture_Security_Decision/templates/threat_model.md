---
title: Threat Model Template
artifact_type: template
status: public
visibility: public
classification: public
owner: "{{ARCHITECTURE_OWNER}}"
review_cadence: quarterly
applies_to: systems or changes that require explicit security threat analysis
source_basis: Microsoft STRIDE threat modeling; OWASP Threat Modeling (owasp.org/www-community/Threat_Modeling)
source_manifests:
  - platform__microsoft_learn.md
  - operations__nist_cisa.md
alignment_mode: direct-adaptation
updated: 2026-03-30
---

## Purpose

Describe the trust boundaries, threats, and mitigations relevant to a design in a way that can be reviewed and reused. This template follows Microsoft STRIDE and OWASP Threat Modeling practices.

STRIDE categories: **S**poofing | **T**ampering | **R**epudiation | **I**nformation Disclosure | **D**enial of Service | **E**levation of Privilege.

## Template

---

### Threat model metadata

- **Threat model ID:** `{{THREAT_MODEL_ID}}`
- **Date:** `{{THREAT_MODEL_DATE}}`
- **Author:** `{{AUTHOR}}`
- **Review date:** `{{REVIEW_DATE}}`
- **Related ADR:** `ADR-{{ADR_REFERENCE}}`
- **Related security requirements record:** `{{SECURITY_REQUIREMENTS_ID}}`
- **Risk acceptance authority:** `{{RISK_ACCEPTANCE_AUTHORITY}}`

---

### 1. System description

Describe `{{SYSTEM_DESCRIPTION}}` at a level sufficient for a security reviewer unfamiliar with the system to follow the rest of this document. Include:

- System purpose and primary user personas
- Technology stack summary
- Deployment model (cloud-native, on-premises, hybrid)
- Data sensitivity level (`{{DATA_SENSITIVITY_LEVEL}}`)

### 2. Scope and assumptions

State what is in scope and what is explicitly out of scope for this threat model. Undocumented scope assumptions are a common source of incomplete threat models.

**In scope:**
- `{{IN_SCOPE_ITEM}}` — describe the component, flow, or feature included.

**Out of scope:**
- `{{OUT_OF_SCOPE_ITEM}}` — describe what is excluded and why.

**Assumptions:**
- `{{ASSUMPTION}}` — list security-relevant assumptions (e.g. "the cloud provider's hypervisor is trusted"). If an assumption is invalidated, this model must be revisited.

### 3. Assets inventory

List all assets that have security value and that an attacker might target. For each asset, state its value to an attacker and to the organisation.

| Asset name | Description | Attacker value | Business value |
|---|---|---|---|
| `{{ASSET_NAME}}` | `{{ASSET_DESCRIPTION}}` | `{{ASSET_VALUE}}` | `{{ASSET_BUSINESS_VALUE}}` |

### 4. Trust boundaries

Describe the trust boundaries in the system. A trust boundary exists wherever the level of trust changes — e.g. between the public internet and the DMZ, between a user-controlled client and a server, between microservices with different privilege levels.

**Trust boundary description:** `{{TRUST_BOUNDARY_DESCRIPTION}}`

| Boundary ID | Boundary name | From (lower trust) | To (higher trust) | Authentication required |
|---|---|---|---|---|
| `{{BOUNDARY_ID}}` | `{{BOUNDARY_NAME}}` | `{{SOURCE_ZONE}}` | `{{TARGET_ZONE}}` | `{{AUTH_REQUIRED}}` |

### 5. Data flow table

Map each significant data flow in the system, especially flows that cross trust boundaries.

| Flow ID | Source | Destination | Protocol | Data classification | Crosses boundary |
|---|---|---|---|---|---|
| `{{FLOW_ID}}` | `{{FLOW_SOURCE}}` | `{{FLOW_DESTINATION}}` | `{{FLOW_PROTOCOL}}` | `{{DATA_CLASSIFICATION}}` | `{{BOUNDARY_ID}}` |

Data classification values: public | internal | confidential | restricted.

### 6. STRIDE threat table

STRIDE requires comprehensive coverage of **all six categories**. Before finalising this threat model, confirm at least one threat has been considered per category. An undocumented absence is an incomplete threat model — if a category yields no threats, justify it explicitly below.

**STRIDE coverage checklist:**

| STRIDE Category | At least one threat identified? | If none: justification |
|---|---|---|
| S — Spoofing | `{{STRIDE_S_COVERED}}` (Yes / No) | `{{STRIDE_S_JUSTIFICATION}}` |
| T — Tampering | `{{STRIDE_T_COVERED}}` (Yes / No) | `{{STRIDE_T_JUSTIFICATION}}` |
| R — Repudiation | `{{STRIDE_R_COVERED}}` (Yes / No) | `{{STRIDE_R_JUSTIFICATION}}` |
| I — Information Disclosure | `{{STRIDE_I_COVERED}}` (Yes / No) | `{{STRIDE_I_JUSTIFICATION}}` |
| D — Denial of Service | `{{STRIDE_D_COVERED}}` (Yes / No) | `{{STRIDE_D_JUSTIFICATION}}` |
| E — Elevation of Privilege | `{{STRIDE_E_COVERED}}` (Yes / No) | `{{STRIDE_E_JUSTIFICATION}}` |

For each identified threat, complete one row. Threat IDs should be stable and referenced in the mitigations register.

| Threat ID | STRIDE category | Component | Threat description | Likelihood | Impact | Mitigation ref |
|---|---|---|---|---|---|---|
| `{{THREAT_ID}}` | `{{STRIDE_CATEGORY}}` | `{{COMPONENT}}` | `{{THREAT_DESCRIPTION}}` | `{{LIKELIHOOD}}` | `{{IMPACT}}` | `{{MITIGATION_REF}}` |

- **STRIDE category:** S (Spoofing) | T (Tampering) | R (Repudiation) | I (Information Disclosure) | D (Denial of Service) | E (Elevation of Privilege)
- **Likelihood:** H (High) | M (Medium) | L (Low)
- **Impact:** H (High) | M (Medium) | L (Low)

### 7. Mitigations register

For each threat in the STRIDE table, describe the control or mitigation applied or planned.

| Mitigation ID | Addresses threat(s) | Control description | Control type | Status | Owner |
|---|---|---|---|---|---|
| `{{MITIGATION_ID}}` | `{{THREAT_ID}}` | `{{MITIGATION}}` | `{{CONTROL_TYPE}}` | `{{MITIGATION_STATUS}}` | `{{MITIGATION_OWNER}}` |

- **Control type:** preventive | detective | corrective | compensating
- **Status:** implemented | planned | accepted-risk | not-applicable

### 8. Residual risk acceptance

List threats where the residual risk (after mitigations) is accepted rather than further mitigated. Each acceptance must be authorised by `{{RISK_ACCEPTANCE_AUTHORITY}}`.

| Threat ID | Residual risk description | Acceptance rationale | Accepted by | Acceptance date |
|---|---|---|---|---|
| `{{THREAT_ID}}` | `{{RESIDUAL_RISK}}` | `{{ACCEPTANCE_RATIONALE}}` | `{{RISK_ACCEPTANCE_AUTHORITY}}` | `{{ACCEPTANCE_DATE}}` |

---

## Guidance

- Capture threats at the level needed for action, not at the level of speculative detail.
- Link to security requirements and architecture decisions where relevant.
- Review this model whenever the system boundary, trust boundaries, or data flows change significantly.
- Every threat in the STRIDE table must have either a mitigation entry or a residual risk acceptance entry.

## Source Attribution

- Source manifests: `platform__microsoft_learn.md`, `operations__nist_cisa.md`
- Primary source basis: Microsoft STRIDE threat modeling; OWASP Threat Modeling (owasp.org/www-community/Threat_Modeling)
- Alignment mode: direct-adaptation
- Reviewed on: 2026-03-30
