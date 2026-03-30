---
title: Security Policy
artifact_type: policy
status: public
visibility: public
classification: public
owner: quality-platform
review_cadence: quarterly
applies_to: vulnerability reporting and supported security response boundaries
source_basis: GitHub Docs security policy guidance
source_manifests:
  - governance__github_docs.md
alignment_mode: direct-adaptation
updated: 2026-03-30
---

## Purpose

Define how security vulnerabilities are reported, triaged, and disclosed, applying GitHub Docs security policy structure and OWASP Top 10 baseline categories.

## Supported Scope

This policy covers security issues in the following:

- `{{SUPPORTED_VERSIONS}}` — versions that receive security fixes (e.g., `>= 2.0`, last two major releases)
- `{{SUPPORTED_ENVIRONMENTS}}` — environments in scope (e.g., production deployments, official releases)

Out of scope: `{{OUT_OF_SCOPE_ITEMS}}` (e.g., third-party dependencies not controlled by this team, development/staging environments).

## Reporting a Vulnerability

**Do NOT open a public GitHub issue for security vulnerabilities.**

Report vulnerabilities via:

1. **GitHub private advisory** (preferred): Navigate to `Security` → `Advisories` → `Report a vulnerability` in the repository
2. **Email** (alternative): `{{SECURITY_EMAIL}}` — use subject line `[SECURITY] {{REPO_NAME}} — brief description`
3. **PGP-encrypted email** (for sensitive disclosures): Key fingerprint `{{PGP_KEY_FINGERPRINT}}`

Include the following in your report:

```
Type: {{VULNERABILITY_TYPE}}  (e.g., XSS, SQL injection — OWASP Top 10 category)
Component: {{AFFECTED_COMPONENT}}
Version(s): {{AFFECTED_VERSIONS}}
CVSS Score (if known): {{CVSS_SCORE}}
Description: {{VULNERABILITY_DESCRIPTION}}
Reproduction steps: {{REPRODUCTION_STEPS}}
Proof of concept: {{POC_LINK_OR_INLINE}}
Impact: {{IMPACT_ASSESSMENT}}
Suggested fix (optional): {{SUGGESTED_FIX}}
```

## OWASP Top 10 Baseline Categories

All disclosures are triaged against the following OWASP Top 10 categories:

| ID | Category | Internal Owner |
|---|---|---|
| A01 | Broken Access Control | `{{ACCESS_CONTROL_OWNER}}` |
| A02 | Cryptographic Failures | `{{CRYPTO_OWNER}}` |
| A03 | Injection (SQLi, XSS, etc.) | `{{INJECTION_OWNER}}` |
| A04 | Insecure Design | `{{DESIGN_OWNER}}` |
| A05 | Security Misconfiguration | `{{PLATFORM_SECURITY_OWNER}}` |
| A06 | Vulnerable and Outdated Components | `{{DEPENDENCY_OWNER}}` |
| A07 | Identification and Authentication Failures | `{{AUTH_OWNER}}` |
| A08 | Software and Data Integrity Failures | `{{INTEGRITY_OWNER}}` |
| A09 | Security Logging and Monitoring Failures | `{{MONITORING_OWNER}}` |
| A10 | Server-Side Request Forgery | `{{SSRF_OWNER}}` |

## Triage and Response SLA

| Severity | CVSS Range | Acknowledgement | Fix Target | Disclosure |
|---|---|---|---|---|
| Critical | 9.0–10.0 | `{{CRITICAL_ACK_SLA}}` (e.g., 24 hours) | `{{CRITICAL_FIX_SLA}}` (e.g., 7 days) | After patch release |
| High | 7.0–8.9 | `{{HIGH_ACK_SLA}}` (e.g., 48 hours) | `{{HIGH_FIX_SLA}}` (e.g., 30 days) | After patch release |
| Medium | 4.0–6.9 | `{{MEDIUM_ACK_SLA}}` | `{{MEDIUM_FIX_SLA}}` | After patch release |
| Low | 0.1–3.9 | `{{LOW_ACK_SLA}}` | Next scheduled release | 90 days |

## CVE Assignment and Disclosure Timeline

1. **Acknowledgement**: Confirm receipt within `{{ACKNOWLEDGEMENT_SLA}}`
2. **Triage**: Severity classification and initial investigation within `{{TRIAGE_SLA}}`
3. **Coordination**: Align with reporter on fix timeline and CVE request via `{{CVE_REQUEST_CHANNEL}}`
4. **Fix**: Develop and test patch; request CVE ID from `{{CVE_AUTHORITY}}` (e.g., GitHub, MITRE)
5. **Pre-disclosure**: Share draft advisory with reporter for review `{{PRE_DISCLOSURE_NOTICE_DAYS}}` days before release
6. **Release**: Publish patched version
7. **Disclosure**: Publish GitHub Security Advisory; announce via `{{ANNOUNCEMENT_CHANNEL}}`

Coordinated disclosure embargo period: `{{EMBARGO_PERIOD}}` (default 90 days from initial report).

## Canonical Relationship

- The repository-instance security surface lives in the root `SECURITY.md`.
- This policy is the reusable quality-layer counterpart for downstream repositories.

## Source Attribution

- Source manifests: `governance__github_docs.md`
- Primary source basis: GitHub Docs security policy guidance
- Alignment mode: direct-adaptation
- Reviewed on: 2026-03-30
