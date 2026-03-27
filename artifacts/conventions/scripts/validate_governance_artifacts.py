#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Iterable, Sequence, Tuple


REQUIRED_FRONTMATTER_KEYS = [
    "title",
    "artifact_type",
    "status",
    "visibility",
    "classification",
    "owner",
    "review_cadence",
    "applies_to",
    "source_basis",
    "source_manifests",
    "alignment_mode",
    "updated",
]

FRONTMATTER_PATHS = [
    Path("artifacts"),
]

ROOT_MARKDOWN_PATHS = [
    Path("README.md"),
    Path("GOVERNANCE.md"),
    Path("CONTRIBUTING.md"),
    Path("CODE_OF_CONDUCT.md"),
    Path("SUPPORT.md"),
    Path("SECURITY.md"),
    Path("decision_log.md"),
]

GITHUB_META_PATHS = [
    Path(".github/ISSUE_TEMPLATE"),
    Path(".github/PULL_REQUEST_TEMPLATE.md"),
    Path(".github/CODEOWNERS"),
    Path(".github/workflows"),
]

ARTIFACT_META_PATHS = [
    Path("artifacts"),
]

SCHEMA_PATHS = [
    Path("artifacts"),
]


def iter_markdown_paths() -> Iterable[Path]:
    for base in FRONTMATTER_PATHS:
        if not base.exists():
            continue
        for path in base.rglob("*.md"):
            if path.name == "PULL_REQUEST_TEMPLATE.md":
                continue
            yield path


def iter_comment_paths() -> Iterable[Path]:
    for base in GITHUB_META_PATHS:
        if base.name.endswith(".md") or base.name == "CODEOWNERS":
            if base.exists():
                yield base
            continue
        if not base.exists():
            continue
        for path in base.rglob("*.yml"):
            yield path


def iter_artifact_meta_paths() -> Iterable[Path]:
    for base in ARTIFACT_META_PATHS:
        if not base.exists():
            continue
        for path in base.rglob("*.yml"):
            yield path
        for path in base.rglob("PULL_REQUEST_TEMPLATE.md"):
            yield path
        for path in base.rglob("CODEOWNERS"):
            yield path


def iter_schema_paths() -> Iterable[Path]:
    for base in SCHEMA_PATHS:
        if not base.exists():
            continue
        for path in base.rglob("*.json"):
            yield path


def iter_root_markdown_paths() -> Iterable[Path]:
    for path in ROOT_MARKDOWN_PATHS:
        if path.exists():
            yield path


def parse_frontmatter(text: str) -> Tuple[dict[str, str], str | None]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, None
    fm_lines: list[str] = []
    for line in lines[1:]:
        if line.strip() == "---":
            break
        fm_lines.append(line)
    else:
        return {}, None
    fm_data: dict[str, str] = {}
    for line in fm_lines:
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        fm_data[key.strip()] = value.strip()
    return fm_data, "\n".join(lines[len(fm_lines) + 2 :])


def has_source_attribution(text: str) -> bool:
    return "Source Attribution" in text


def check_markdown(path: Path) -> list[str]:
    content = path.read_text(encoding="utf-8")
    fm_data, _ = parse_frontmatter(content)
    problems: list[str] = []
    if not fm_data:
        problems.append("missing frontmatter")
        return problems
    missing = [key for key in REQUIRED_FRONTMATTER_KEYS if key not in fm_data]
    if missing:
        problems.append(f"missing frontmatter keys: {', '.join(missing)}")
    if not has_source_attribution(content):
        problems.append("missing '## Source Attribution'")
    return problems


def check_root_markdown(path: Path) -> list[str]:
    content = path.read_text(encoding="utf-8")
    fm_data, _ = parse_frontmatter(content)
    problems: list[str] = []
    if fm_data:
        missing = [key for key in REQUIRED_FRONTMATTER_KEYS if key not in fm_data]
        if missing:
            problems.append(f"missing frontmatter keys: {', '.join(missing)}")
    if not has_source_attribution(content):
        problems.append("missing '## Source Attribution'")
    return problems


def check_comment_file(path: Path) -> list[str]:
    content = path.read_text(encoding="utf-8")
    if not has_source_attribution(content):
        return ["missing 'Source Attribution' marker"]
    return []


def run_checks(paths: Iterable[Path], checker) -> list[Tuple[Path, Sequence[str]]]:
    failures: list[Tuple[Path, Sequence[str]]] = []
    for path in paths:
        problems = checker(path)
        if problems:
            failures.append((path, problems))
    return failures


def gather_all_checks() -> list[Tuple[Path, Sequence[str]]]:
    failures = []
    failures.extend(run_checks(iter_markdown_paths(), check_markdown))
    failures.extend(run_checks(iter_root_markdown_paths(), check_root_markdown))
    failures.extend(run_checks(iter_comment_paths(), check_comment_file))
    failures.extend(run_checks(iter_artifact_meta_paths(), check_comment_file))
    failures.extend(run_checks(iter_schema_paths(), check_schema_file))
    return failures


def check_schema_file(path: Path) -> list[str]:
    content = path.read_text(encoding="utf-8")
    problems: list[str] = []
    try:
        json.loads(content)
    except json.JSONDecodeError as exc:
        problems.append(f"invalid JSON: {exc.msg}")
        return problems
    if "source_manifests" not in content:
        problems.append("missing 'source_manifests' reference")
    if "alignment_mode" not in content:
        problems.append("missing 'alignment_mode' reference")
    return problems


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate frontmatter and traceability for governance artifacts."
    )
    parser.add_argument(
        "--report-only",
        action="store_true",
        help="Print findings without changing the exit status.",
    )
    args = parser.parse_args()
    failures = gather_all_checks()
    if not failures:
        print("Validator: OK (no issues found).")
        return 0
    for path, problems in failures:
        print(f"{path}:")
        for problem in problems:
            print(f"  - {problem}")
    if args.report_only:
        print("Validator: issues reported in report-only mode.")
        return 0
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
