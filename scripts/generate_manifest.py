#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from pathlib import Path


SUMMARY_PATTERN = re.compile(
    r"<summary><b>(?P<id>\d{2})\. (?P<name>.*?) \((?P<focus>.*?)\)</b></summary>",
    re.IGNORECASE,
)
LINK_PATTERN = re.compile(r"\[([^\]]+)\]\(\./([^)]+)\)")


def map_maturity_to_status(maturity: str) -> str:
    normalized = maturity.strip().lower()
    if normalized == "public":
        return "ready"
    if normalized == "public draft":
        return "hardening"
    return "draft"


def parse_table(block: str, *, is_supporting: bool) -> list[dict[str, str]]:
    lines = block.strip().splitlines()
    items: list[dict[str, str]] = []

    separator_index = -1
    for index, line in enumerate(lines):
        if "---|" in line:
            separator_index = index
            break

    for index, line in enumerate(lines):
        if "|" not in line or index in {separator_index, separator_index - 1}:
            continue

        columns = [column.strip() for column in line.split("|")]
        columns = [column for column in columns if column]
        if len(columns) < 4:
            continue

        title_match = LINK_PATTERN.search(columns[0])
        title = title_match.group(1) if title_match else columns[0].strip()
        path_match = LINK_PATTERN.search(line)
        path = path_match.group(2) if path_match else ""

        if is_supporting:
            if len(columns) < 5:
                continue
            maturity = columns[2]
            items.append(
                {
                    "title": title,
                    "role": columns[1],
                    "maturity": maturity,
                    "nature": "Supporting",
                    "source": columns[3],
                    "status": map_maturity_to_status(maturity),
                    "path": path,
                }
            )
        else:
            if len(columns) < 6:
                continue
            maturity = columns[4]
            items.append(
                {
                    "title": title,
                    "nature": columns[1],
                    "role": columns[2],
                    "source": columns[3],
                    "maturity": maturity,
                    "status": map_maturity_to_status(maturity),
                    "path": path,
                }
            )

    return items


def parse_readme(readme_path: Path) -> list[dict[str, object]]:
    content = readme_path.read_text(encoding="utf-8")
    sections = content.split("<details>")
    parsed_dimensions: list[dict[str, object]] = []

    for index, section in enumerate(sections):
        if index == 0:
            continue

        details_content = section.split("</details>", 1)[0]
        summary_match = SUMMARY_PATTERN.search(details_content)
        if not summary_match:
            continue

        parts = details_content.split("### Supporting Artifacts", 1)
        parsed_dimensions.append(
            {
                "id": summary_match.group("id"),
                "name": summary_match.group("name").strip(),
                "focus": summary_match.group("focus").strip(),
                "primary": parse_table(parts[0], is_supporting=False),
                "supporting": parse_table(parts[1], is_supporting=True) if len(parts) > 1 else [],
            }
        )

    return parsed_dimensions


def main() -> int:
    repo_root = Path(__file__).resolve().parent.parent
    readme_path = repo_root / "README.md"
    manifest_path = repo_root / "docs" / "manifest.json"

    dimensions = parse_readme(readme_path)
    total_items = sum(len(dimension["primary"]) + len(dimension["supporting"]) for dimension in dimensions)

    print(f"Parsed {len(dimensions)} dimensions.")
    print(f"Total items parsed: {total_items}")

    if not dimensions or total_items == 0:
        raise SystemExit("Manifest generation failed: parsed zero dimensions or zero items from README.md")

    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(json.dumps(dimensions, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Manifest written to {manifest_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
