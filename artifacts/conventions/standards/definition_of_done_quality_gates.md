---
title: Definition of Done and Quality Gates
artifact_type: standard
status: public-draft
visibility: public
classification: public
owner: "{{OWNER_NAME}}"
review_cadence: quarterly
applies_to: work completion criteria
source_basis: Scrum Guide 2020 and GitHub validation conventions
source_manifests:
  - method__scrum_guide.md
  - governance__github_docs.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
---

## Purpose

Define the minimum conditions that must be met before work is considered complete and publishable. The Definition of Done (DoD) is a formal description of the state of an Increment when it meets the quality measures required for the product — not a per-team or per-story checklist, but a shared, transparent standard that applies to every Increment.

## Definition of Done Concept

Per the Scrum Guide 2020, the Definition of Done creates transparency by providing a shared understanding of what it means for work to be complete. Key principles:

- The DoD applies to **every Increment**, regardless of which team or individual produced it.
- If an Increment does not meet the DoD, it must not be released or presented at the Sprint Review as done.
- The DoD is the minimum; Developers may apply more stringent standards but not lower ones.
- The DoD is owned by the Scrum Team and must be visible to all stakeholders.

## Required Quality Gates per Increment

An Increment is not done until all of the following gates pass. Gates are verified in the order listed; a failing gate blocks all subsequent gates.

- [ ] **Coded to standards** — Code or artifact follows all conventions in `coding_standards.md` and passes linting with zero errors.
- [ ] **Unit tests pass** — All unit tests execute green; no skipped tests without an associated issue.
- [ ] **Integration tests pass** — All integration tests for affected module boundaries execute green.
- [ ] **Code reviewed** — A minimum of `{{MIN_REVIEWERS}}` reviewers have approved the change. At least one reviewer must be outside the author's immediate sub-team.
- [ ] **Documentation updated** — Relevant how-to guides, reference docs, or explanations are updated or created to reflect the change.
- [ ] **No new linting errors** — The linting gate in CI passes; no new suppressions without justification.
- [ ] **Security scan passed** — Automated dependency and SAST scans return no new `HIGH` or `CRITICAL` findings. Known accepted risks are documented at `{{SECURITY_EXCEPTIONS_PATH}}`.
- [ ] **Deployed to staging** — The Increment has been deployed to `{{STAGING_ENVIRONMENT}}` and smoke-tested against the happy path.

## Sprint-Level DoD vs Release DoD

The two levels serve different purposes and must not be conflated.

**Sprint-Level DoD** — applied at the end of every Sprint to every Increment produced during the Sprint. An Increment that does not meet the Sprint DoD is considered undone work and must not be included in the Sprint Review as complete.

**Release DoD** — applied to the aggregate of Increments bundled into a release. In addition to all Sprint-level gates, a release must satisfy:
- Changelog reviewed and approved by `{{RELEASE_APPROVER}}`.
- All Sprint-level undone work resolved or explicitly deferred with a tracked issue.
- Rollback procedure documented and verified (see `release_versioning_policy.md`).
- Stakeholder sign-off obtained from `{{RELEASE_SIGNOFF_AUTHORITY}}`.

## Undone Work Policy

Undone work is any work that was started during a Sprint but did not meet the DoD by Sprint end. Per Scrum Guide 2020:

- Undone work must not be released or presented as complete.
- Undone work must be returned to the Product Backlog and re-estimated, not carried forward as "almost done."
- The presence of recurring undone work is a signal that the DoD or Sprint capacity planning needs adjustment.

Teams must track undone work transparently. Releasing undone work — even under deadline pressure — violates this policy and must be escalated to `{{ESCALATION_AUTHORITY}}`.

## DoD Evolution Process

The DoD is a living standard. It must evolve as the team's practices mature, tooling improves, or new risk surfaces are identified. The update process is `{{UPDATE_PROCESS}}` and follows these steps:

1. Any team member may propose a DoD change by opening an issue against this artifact.
2. The Scrum Team discusses the proposal in a retrospective or dedicated working session.
3. Changes are approved by consensus (or by `{{UPDATE_AUTHORITY}}` if consensus is not reached).
4. The approved change is committed to this artifact with a corresponding `updated` date change.
5. The new DoD takes effect at the start of the next Sprint.

Stricter gates may be adopted immediately; relaxing a gate requires a documented rationale explaining why the quality risk is acceptable.

## Source Attribution

- Source manifests: method__scrum_guide.md, governance__github_docs.md
- Primary source basis: Scrum Guide 2020 and GitHub validation conventions
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27
