from __future__ import annotations

import urllib.request
import os
import re
import time


FONT_BLOCK_PATTERN = re.compile(r"@font-face\s*\{(?P<body>.*?)\}", re.DOTALL)
FIELD_PATTERN = re.compile(r"(?P<name>font-family|font-style|font-weight|src)\s*:\s*(?P<value>[^;]+);")
URL_PATTERN = re.compile(r"url\((https://[^)]+)\)")
TAILWIND_BROWSER_URL = "https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4.2.2/dist/index.global.js"
MERMAID_URL = "https://cdn.jsdelivr.net/npm/mermaid@11.13.0/dist/mermaid.min.js"
FONTS_STYLESHEET_URL = (
    "https://fonts.googleapis.com/css2?"
    "family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;700&display=swap"
)
REQUEST_TIMEOUT_SECONDS = 20
MAX_DOWNLOAD_ATTEMPTS = 3


def slugify(value):
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def download_file(url, target_path):
    os.makedirs(os.path.dirname(target_path), exist_ok=True)
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})

    last_error = None
    for attempt in range(1, MAX_DOWNLOAD_ATTEMPTS + 1):
        try:
            with urllib.request.urlopen(req, timeout=REQUEST_TIMEOUT_SECONDS) as response, open(target_path, 'wb') as out_file:
                data = response.read()
                out_file.write(data)
            print(f"Downloaded: {target_path}")
            return data
        except Exception as exc:
            last_error = exc
            if attempt == MAX_DOWNLOAD_ATTEMPTS:
                break
            sleep_seconds = attempt
            print(f"Retrying download ({attempt}/{MAX_DOWNLOAD_ATTEMPTS}) for {url} after {sleep_seconds}s: {exc}")
            time.sleep(sleep_seconds)

    raise RuntimeError(f"Failed to download {url}") from last_error


def parse_font_blocks(css_data):
    blocks = []
    for match in FONT_BLOCK_PATTERN.finditer(css_data):
        fields = {}
        for field_match in FIELD_PATTERN.finditer(match.group("body")):
            name = field_match.group("name")
            value = field_match.group("value").strip().strip("'\"")
            fields[name] = value
        url_match = URL_PATTERN.search(fields.get("src", ""))
        if not url_match:
            continue
        fields["url"] = url_match.group(1)
        blocks.append(fields)
    return blocks


def build_font_filename(fields, used_names):
    family = slugify(fields.get("font-family", "font"))
    style = slugify(fields.get("font-style", "normal"))
    weight = slugify(fields.get("font-weight", "400"))
    filename = f"{family}-{style}-{weight}.woff2"
    if filename in used_names:
        index = 2
        while f"{family}-{style}-{weight}-{index}.woff2" in used_names:
            index += 1
        filename = f"{family}-{style}-{weight}-{index}.woff2"
    used_names.add(filename)
    return filename


def main():
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    assets_js = os.path.join(repo_root, 'docs', 'assets', 'js')
    assets_css = os.path.join(repo_root, 'docs', 'assets', 'css')
    assets_fonts = os.path.join(repo_root, 'docs', 'assets', 'fonts')
    
    # 1. Download JS
    download_file(TAILWIND_BROWSER_URL, os.path.join(assets_js, 'tailwindcss.js'))
    download_file(MERMAID_URL, os.path.join(assets_js, 'mermaid.min.js'))
    
    # 2. Download Google Fonts CSS
    css_data = download_file(FONTS_STYLESHEET_URL, os.path.join(assets_css, 'fonts.css')).decode('utf-8')
    
    # 3. Parse CSS for WOFF2 URLs and download them deterministically
    used_names = set()
    for fields in parse_font_blocks(css_data):
        url = fields["url"]
        font_filename = build_font_filename(fields, used_names)
        font_path = os.path.join(assets_fonts, font_filename)
        download_file(url, font_path)
        css_data = css_data.replace(url, f"../fonts/{font_filename}")
        css_data = css_data.replace("format('truetype')", "format('woff2')")
        
    with open(os.path.join(assets_css, 'fonts.css'), 'w', encoding='utf-8') as f:
        f.write(css_data)
        
    print("Asset bundling complete!")

if __name__ == '__main__':
    main()
