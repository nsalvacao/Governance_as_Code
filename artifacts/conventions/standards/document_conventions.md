---
title: Document Conventions
artifact_type: normative
status: draft
visibility: public
classification: public
owner: governance@org
review_cadence: quarterly
applies_to: repositories that opt into the governance corpus
source_basis: documentation__diataxis, governance__github_docs
source_manifests: documentation__diataxis.md, governance__github_docs.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
---

# Document Conventions

## Scope

This guide defines the canonical rules for reusable artifacts stored in this repository's library. It does not describe the repository-instance files at the root or under `/.github/`, except where those instance files are concrete instantiations of library assets.

## Naming and placement

- Use stable, descriptive filenames (e.g., `artifacts/operations/policies/incident_response_policy.md`).
- Prefer lowercase with hyphen separators.
- Organise reusable assets under `artifacts/<dimension>/<artifact-type>/`.
- Keep the repository root and `/.github/` for instance-specific files only.
- When providing forks or derived branches, add `-<ENV>` suffixes to avoid collisions while keeping a clear tie to the canonical artifact.

## Metadata frontmatter

- Each reusable Markdown artifact uses the YAML frontmatter contract from `artifacts/conventions/schemas/frontmatter.schema.json`.
- Required fields are `title`, `artifact_type`, `status`, `visibility`, `classification`, `owner`, `review_cadence`, `applies_to`, `source_basis`, `source_manifests`, `alignment_mode`, and `updated`.
- Add artifact-specific metadata (e.g., `decision_log_id`, `logic_owner`, `review_notes`) as needed; the schema allows these extensions while the baseline set stays mandatory.
- Prefer a YAML list for `source_manifests`; a single string is allowed only for compatibility with existing material.
- `applies_to` clarifies the types of repositories or teams that should instantiate the document (e.g., `platform services`, `compliance-focused teams`).
- `classification` stays within `public`, `public-redacted`, or `private`.
- Use placeholders for variable content: `{{PROJECT_NAME}}`, `{{OWNER}}`, `{{REVIEW_CADENCE}}`, etc.

## Structural expectations

- Documents stay concise—describe the what, when, and how in under 800 words unless a narrative is required.
- Use `##`-level sections to separate policy, execution, and evidence; `###` headings may annotate automation hooks.
- Include checklists or tables when listing repeated controls.
- Reference related artifacts with cross-links (e.g., link automation rules to `artifacts/conventions/standards/automation_and_ai_execution.md`).

## Automation and AI wiring

- Reference automation hooks explicitly (e.g., “Trigger `validate-governance-artifacts` workflow on `issue_comment`”).
- Mention deterministic steps that GitHub Actions or scripts execute, and tie them to placeholders such as `{{GH_ACTION_NAME}}`.
- Avoid ambiguous statements; describe the expected behavior for agents and the automation surfaces they can consume.

## Selective applicability

- Explicitly call out any prerequisites (e.g., requires `production` environment or `services` team).
- When an artifact is optional, state the decision filter: “Apply when `{{MISSING_CONTROLS}}` equals `true`.”
- Document how to override defaults: use parameterized templates from `artifacts/conventions/templates/partials/` and supply values through `{{UPPER_SNAKE_CASE}}` placeholders.

## Collaboration signals

- Provide reviewer checklists and ownership details in the metadata.
- Surface how a downstream repo requests updates (e.g., “Propose a PR referencing `artifacts/conventions/standards/document_conventions.md` to propose a change”).

## Source Attribution

- Source manifests: documentation__diataxis.md, governance__github_docs.md
- Primary source basis: Diataxis documentation architecture plus GitHub governance guidance
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27
