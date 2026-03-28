---
title: Document Conventions
artifact_type: normative
status: public-draft
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

## Document Types and Their Conventions

Every artifact belongs to exactly one document type. The type determines structural expectations, review triggers, and reuse patterns.

| Type | Nature | Purpose | Placeholder requirement |
|---|---|---|---|
| **Normative** | Authoritative rule | Defines what must be true; enforced by tooling | All instance-specific values must use `{{UPPER_SNAKE_CASE}}` |
| **Operational** | Process guidance | Describes how to execute a process or runbook | Workflow steps and role names use `{{UPPER_SNAKE_CASE}}` |
| **Instantiable** | Template | Filled by downstream consumers; not a final document | Every instance-specific value uses `{{UPPER_SNAKE_CASE}}` |
| **Evidence** | Audit record | Records that something happened; not a prescription | Dates and identifiers use `{{UPPER_SNAKE_CASE}}` until instantiated |

When the type is ambiguous, prefer a more restrictive type (normative over operational, operational over instantiable).

## Frontmatter Requirements

All Markdown artifacts under `artifacts/` require YAML frontmatter. Required fields are defined in `artifacts/01_Governance_Method/schemas/frontmatter.schema.json`. The mandatory set is:

- `title`
- `artifact_type`
- `status`
- `visibility`
- `classification`
- `owner`
- `review_cadence`
- `applies_to`
- `source_basis`
- `source_manifests`
- `alignment_mode`
- `updated`
Additional artifact-specific keys (e.g., `decision_log_id`, `logic_owner`) are allowed as extensions. Downstream consumers may add their own keys without violating the base schema. Use `{{UPPER_SNAKE_CASE}}` for all values that are instance-specific.

## Heading Hierarchy Rules

Heading levels communicate document structure. Violations make automated parsing unreliable.

- **H1 (`#`):** The document title only. One H1 per document. For documents that use frontmatter `title`, the H1 may be omitted; if present, it must match `title`.
- **H2 (`##`):** Major sections. Used for top-level thematic breaks (e.g., `## Purpose`, `## Requirements`, `## Source Attribution`).
- **H3 (`###`):** Subsections within an H2. Used for automation hooks, sub-categories, or detailed breakdowns.
- **H4 and below:** Use sparingly. Deep nesting is a signal that the document should be split.

Never skip heading levels (e.g., do not place an H3 directly under an H1 without an intervening H2).

## Placeholder Syntax

All instance-specific values that downstream consumers must replace follow the pattern: `{{UPPER_SNAKE_CASE}}`

- Examples: `{{OWNER_NAME}}`, `{{REVIEW_CADENCE}}`, `{{ADR_STORAGE_PATH}}`
- Placeholders appear in both the frontmatter and the document body.
- Never use bare text where a placeholder is required; it makes the template appear instantiated when it is not.
- Automation validates that no artifact in the library contains un-replaced placeholders from a known set.

## Link Format

- **Same-repository links:** Use relative paths (e.g., `../policies/adr_policy.md`). Absolute URLs break when the repository is forked or renamed.
- **Cross-repository links:** Use absolute URLs. Prefer URLs that resolve to a specific tagged version rather than `main` to avoid link rot.
- **External documentation:** Use absolute URLs. Add a note if the external resource is likely to change (e.g., versioned specifications).

## File Naming Convention

Files follow the pattern: `{{NAMING_PATTERN}}` (default: lowercase, hyphen-separated words, `.md` extension for Markdown).

- Examples: `adr_policy.md`, `source_attribution_standard.md`
- Underscores are acceptable for artifact files to match the existing corpus; new files should use underscores for consistency with existing peers.
- Do not use spaces, uppercase letters, or special characters other than hyphens and underscores.
- Directories follow the same convention.

## Language

- **Technical content:** English (EN). This applies to all artifacts in this library regardless of the team's primary language.
- **Comments and inline guidance:** English (EN).
- Locale-specific variations (date formats, number formats) must use ISO standards: dates as `YYYY-MM-DD`, numbers without locale separators.

## Line Length

Wrap prose at `{{MAX_LINE_LENGTH}}` characters (default: 120). Code blocks and tables are exempt from line length limits. Consistent wrapping makes diffs readable in side-by-side views.

## Code Block Language Tags

All fenced code blocks must include a language tag. This enables syntax highlighting and communicates intent.

```yaml
# Correct: language tag present
key: value
```

A block without a language tag must use ` ```text ` to make the omission explicit rather than accidental.

## Automation and AI Wiring

- Reference automation hooks explicitly (e.g., "Trigger `validate-governance-artifacts` workflow on `issue_comment`").
- Mention deterministic steps that GitHub Actions or scripts execute, and tie them to placeholders such as `{{GH_ACTION_NAME}}`.
- Avoid ambiguous statements; describe the expected behavior for agents and the automation surfaces they can consume.

## Selective Applicability

- Explicitly call out any prerequisites (e.g., requires `production` environment or `services` team).
- When an artifact is optional, state the decision filter: "Apply when `{{MISSING_CONTROLS}}` equals `true`."
- Document how to override defaults: use parameterized templates from `artifacts/01_Governance_Method/templates/partials/` and supply values through `{{UPPER_SNAKE_CASE}}` placeholders.

## Collaboration Signals

- Provide reviewer checklists and ownership details in the metadata.
- Surface how a downstream repo requests updates (e.g., "Propose a PR referencing `artifacts/01_Governance_Method/standards/document_conventions.md` to propose a change").

## Source Attribution

- Source manifests: documentation__diataxis.md, governance__github_docs.md
- Primary source basis: Diataxis documentation architecture plus GitHub governance guidance
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27
