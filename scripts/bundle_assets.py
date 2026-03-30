import os
import urllib.request
import re

def download_file(url, target_path):
    os.makedirs(os.path.dirname(target_path), exist_ok=True)
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response, open(target_path, 'wb') as out_file:
        data = response.read()
        out_file.write(data)
    print(f"Downloaded: {target_path}")
    return data

def main():
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    assets_js = os.path.join(repo_root, 'docs', 'assets', 'js')
    assets_css = os.path.join(repo_root, 'docs', 'assets', 'css')
    assets_fonts = os.path.join(repo_root, 'docs', 'assets', 'fonts')
    
    # 1. Download JS
    download_file('https://cdn.tailwindcss.com', os.path.join(assets_js, 'tailwindcss.js'))
    download_file('https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js', os.path.join(assets_js, 'mermaid.min.js'))
    
    # 2. Download Google Fonts CSS
    fonts_url = "https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;700&display=swap"
    css_data = download_file(fonts_url, os.path.join(assets_css, 'fonts.css')).decode('utf-8')
    
    # 3. Parse CSS for WOFF2 URLs and download them
    urls = re.findall(r'url\((https://[^)]+)\)', css_data)
    for i, url in enumerate(set(urls)):
        font_filename = f"font_{i}.woff2"
        font_path = os.path.join(assets_fonts, font_filename)
        download_file(url, font_path)
        # Update CSS to point to local fonts
        css_data = css_data.replace(url, f"../fonts/{font_filename}")
        
    with open(os.path.join(assets_css, 'fonts.css'), 'w', encoding='utf-8') as f:
        f.write(css_data)
        
    print("Asset bundling complete!")

if __name__ == '__main__':
    main()
