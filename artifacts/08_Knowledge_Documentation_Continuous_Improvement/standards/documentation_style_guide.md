---
title: Documentation Style Guide
artifact_type: standard
status: public-draft
visibility: public
classification: public
owner: knowledge-platform
review_cadence: semiannual
applies_to: public documentation and reusable governance artifacts
source_basis: Google Developer Documentation Style Guide
source_manifests:
  - governance__github_docs.md
  - documentation__diataxis.md
alignment_mode: hybrid-synthesis
updated: 2026-03-27
---

## Purpose

Define the editorial rules that keep documentation for `{{REPOSITORY_NAME}}` consistent, clear, and automation-friendly. This guide adapts the Google Developer Documentation Style Guide to the conventions of this repository.

## Voice and Tone

Use second person, active voice, and present tense throughout. These rules apply to all documentation types except explanation, where a more discursive tone is acceptable.

### Second person ("you")

Address the reader directly using "you". Avoid "the user", "one", or passive constructions that remove the reader from the action.

- Correct: `{{EXAMPLE_CORRECT_SECOND_PERSON}}`
- Incorrect: `{{EXAMPLE_INCORRECT_SECOND_PERSON}}`

### Active voice

Make the subject of the sentence perform the action. Passive voice obscures who does what and makes sentences harder to parse.

- Correct: `{{EXAMPLE_CORRECT_ACTIVE}}`
- Incorrect: `{{EXAMPLE_INCORRECT_ACTIVE}}`

### Present tense

Describe what happens now, not what will happen. Future tense ("will") is reserved for conditions and consequences.

- Correct: `{{EXAMPLE_CORRECT_PRESENT}}`
- Incorrect: `{{EXAMPLE_INCORRECT_PRESENT}}`

### Tone guidelines

- Be direct and task-focused; avoid filler phrases such as "simply", "just", "easy", or "obvious".
- Do not editorialize. Document behavior; do not praise it.
- Be consistent: if a term is introduced with a specific form, use that form everywhere.

## Language

### Simple English

Prefer short sentences and common words. Technical accuracy does not require complexity.

- Maximum recommended sentence length: `{{MAX_SENTENCE_WORDS}}` words.
- Avoid jargon that is not defined in this repository. Example of forbidden unexplained jargon: `{{FORBIDDEN_JARGON_EXAMPLE}}`.

### Acronyms and abbreviations

Spell out every acronym on first use in each document, followed by the acronym in parentheses.

- Pattern: `{{ACRONYM}} ({{FULL_FORM}})`
- After first use, the acronym alone is acceptable.
- Exception: acronyms that are universally known in the target audience (`{{UNIVERSAL_ACRONYM_EXCEPTIONS}}`).

### Inclusive language

- Avoid terms with exclusionary connotations. Use `{{INCLUSIVE_ALTERNATIVE}}` instead of `{{EXCLUSIONARY_TERM}}`.
- Do not use gendered pronouns for generic references; use "they" or rewrite to avoid pronouns.
- Avoid metaphors rooted in violence or hierarchy when neutral alternatives exist.
- Full inclusive language checklist: `{{INCLUSIVE_LANGUAGE_CHECKLIST_LINK}}`.

## Headings

### Case and style

- Use sentence case for all headings: capitalize only the first word and proper nouns.
- For procedural sections (how-to guides, tutorials): use imperative verb phrases that describe the reader's action.
  - Example: `{{EXAMPLE_IMPERATIVE_HEADING}}`
- For reference sections: use noun phrases that describe the subject.
  - Example: `{{EXAMPLE_NOUN_HEADING}}`

### Depth

- Maximum heading depth: `{{MAX_HEADING_DEPTH}}` levels (H1 through H`{{MAX_HEADING_DEPTH}}`).
- H1 is the document title; do not repeat it in the body.
- Avoid single-child headings: if a heading has only one subsection, flatten the structure.

## Lists

- Use unordered (bullet) lists for items without inherent sequence.
- Use numbered lists for steps, ranked items, or any sequence that must be followed in order.
- Do not nest lists more than 2 levels deep. Deeper nesting signals a structural problem in the content.
- Every list item should be grammatically parallel.
- Avoid lists with a single item; convert to prose.

## Code Formatting

### Inline code

Use backtick-delimited inline code for: command names, file paths, variable names, parameter names, literal strings the reader must type, and short code expressions.

- Example: run `{{INLINE_CODE_EXAMPLE}}` to initialize the environment.

### Code blocks

Use fenced code blocks with an explicit language tag for all multi-line code, commands, and configuration samples.

````
```{{LANGUAGE_TAG}}
{{CODE_BLOCK_EXAMPLE}}
```
````

- Always specify the language tag (e.g., `bash`, `yaml`, `python`, `json`). Use `text` when no language applies.
- Code in blocks is assumed to be copy-pasteable. Ensure it is correct and tested.

## Links

- Use descriptive anchor text that tells the reader what they will find at the destination.
- Never use "click here", "here", "this page", or "this link" as anchor text.
- Example: instead of `see [here]({{URL}})`, write `see [{{DESCRIPTIVE_LINK_TEXT}}]({{URL}})`.
- External links should open in the same tab unless a specific UX reason requires otherwise.
- Verify that all links resolve before committing. Broken links are remediated within `{{BROKEN_LINK_SLA}}`.

## Images and Diagrams

- Every image must have an alt text attribute that describes the content for screen readers and broken-image fallback.
  - Pattern: `![{{ALT_TEXT}}]({{IMAGE_PATH}})`
- Alt text should describe the information conveyed, not just the visual form. Instead of "diagram", write what the diagram shows.
- Diagrams must have a caption or inline description explaining their relevance.
- Prefer vector formats (SVG) for diagrams; use PNG for screenshots.
- Do not embed sensitive data, credentials, or personal information in images.

## Dates and Numbers

- Date format: `{{DATE_FORMAT}}` (example: `2026-03-27` for ISO 8601, or `{{LOCALE_DATE_EXAMPLE}}` if locale-specific).
- Use numerals for all numbers in technical contexts (steps, measurements, counts).
- Spell out numbers under 10 in prose contexts unless they appear alongside units.
- Use SI prefixes for storage sizes (KB, MB, GB); be explicit about whether KB means 1000 or 1024 bytes when precision matters.

## File Paths and Commands

- Render all file paths and shell commands in monospace (inline code or code block).
- When a command differs by OS, show OS-specific variants in clearly labelled tabs or sections.
  - Example: `{{OS_SPECIFIC_COMMAND_EXAMPLE}}`
- Use placeholder values in the form `{{UPPER_SNAKE_CASE}}` for values the reader must substitute.
- Avoid hard-coding environment-specific values (home directories, usernames) in examples.

## Source Attribution

- Source manifests: governance__github_docs.md, documentation__diataxis.md
- Primary source basis: Google Developer Documentation Style Guide
- Alignment mode: hybrid-synthesis
- Reviewed on: 2026-03-27
