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

**Do NOT open a public GitHub issue for security vulnerabilities.** Use the private reporting channel below.

---

## Supported Versions

The following versions of `{{REPOSITORY_NAME}}` / associated artifacts are currently supported with security updates:

| Version / Branch | Supported |
|---|---|
| `{{VERSION_OR_BRANCH_1}}` | ✅ Yes |
| `{{VERSION_OR_BRANCH_2}}` | ❌ No — upgrade to `{{RECOMMENDED_VERSION}}` |

---

## Reporting a Vulnerability

### Private Reporting (preferred)

Use GitHub's private vulnerability reporting:
**[Report a vulnerability](https://github.com/{{ORG_NAME}}/{{REPOSITORY_SLUG}}/security/advisories/new)**

Or contact the security team directly:
**`{{SECURITY_CONTACT}}`**

Include in your report:
- Description of the vulnerability and its potential impact
- Steps to reproduce (proof-of-concept if possible)
- Affected versions or artifact paths
- CVSS base score estimate (if known) — use CVSS v3.1 calculator at `{{CVSS_CALCULATOR_LINK}}`
- Any proposed mitigation or patch

Do NOT include sensitive details in public issue comments, PR descriptions, or commit messages.

### When to use the public issue tracker

Use `.github/ISSUE_TEMPLATE/incident_report.yml` ONLY when:
- The vulnerability is already publicly disclosed
- The report concerns a non-sensitive automation failure
- The issue is a follow-up tracking item after private disclosure is complete

---

## Triage and Response SLAs

| Severity (CVSS v3.1) | Score Range | Acknowledgement | Triage | Resolution Target |
|---|---|---|---|---|
| Critical | 9.0–10.0 | Within `{{CRITICAL_ACK_SLA}}` | Within `{{CRITICAL_TRIAGE_SLA}}` | `{{CRITICAL_RESOLUTION_TARGET}}` |
| High | 7.0–8.9 | Within `{{HIGH_ACK_SLA}}` | Within `{{HIGH_TRIAGE_SLA}}` | `{{HIGH_RESOLUTION_TARGET}}` |
| Medium | 4.0–6.9 | Within `{{MEDIUM_ACK_SLA}}` | Within `{{MEDIUM_TRIAGE_SLA}}` | `{{MEDIUM_RESOLUTION_TARGET}}` |
| Low | 0.1–3.9 | Within `{{LOW_ACK_SLA}}` | Within `{{LOW_TRIAGE_SLA}}` | `{{LOW_RESOLUTION_TARGET}}` |

`{{SECURITY_TEAM}}` is responsible for triage. If the issue is actionable for downstream repositories, a `{{SECURITY_TRIAGE_LABEL}}` is applied and affected automation is redlined.

---

## Coordinated Disclosure Process

1. **Report received** — security team acknowledges within the SLA above.
2. **Triage** — `{{SECURITY_TEAM}}` assesses impact, assigns CVSS score, and determines affected scope.
3. **Remediation** — patch developed in a private branch; affected downstream repos notified under embargo.
4. **CVE assignment** — request CVE via `{{CVE_AUTHORITY}}` (e.g., GitHub Advisory, MITRE) if CVSS ≥ `{{CVE_THRESHOLD}}`.
5. **Embargo period** — `{{EMBARGO_DURATION}}` from triage completion to allow downstream patching.
6. **Disclosure** — GitHub Security Advisory published; patch released; public issue opened for tracking.
7. **Post-disclosure** — credit reporter (unless they request anonymity) in the advisory.

Disclosure timeline target (Critical/High): `{{DISCLOSURE_TIMELINE_TARGET}}` from initial report.

---

## Scope

**In scope**:
- `{{IN_SCOPE_1}}` (e.g., Vulnerabilities in validator logic affecting artifact integrity)
- `{{IN_SCOPE_2}}` (e.g., Injection risks in GitHub Actions workflows)
- `{{IN_SCOPE_3}}` (e.g., Sensitive data exposure in public artifacts)

**Out of scope**:
- `{{OUT_OF_SCOPE_1}}` (e.g., Social engineering of maintainers)
- `{{OUT_OF_SCOPE_2}}` (e.g., Vulnerabilities in downstream repository instances — report to that repo)
- Denial of service against GitHub infrastructure

---

## Safe Harbour

We will not pursue legal action against researchers who:
- Report issues through the private reporting channel above
- Act in good faith and do not exploit vulnerabilities beyond what is needed to demonstrate impact
- Do not access, modify, or delete data of other users

## Source Attribution

- Source manifests: `governance__github_docs.md`
- Primary source basis: GitHub Docs security policy guidance + coordinated vulnerability disclosure model
- Alignment mode: `direct-adaptation`
- Reviewed on: 2026-03-27
