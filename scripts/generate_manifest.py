import os
import re
import json

def parse_readme(readme_path):
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()

    sections = content.split('<details>')
    parsed_dimensions = []

    for idx, section in enumerate(sections):
        if idx == 0:
            continue
            
        details_content = section.split('</details>')[0]
        
        # Match dimension header: <summary><b>01. Governance & Method (Foundation & Norms)</b></summary>
        summary_match = re.search(r'<summary><b>(\d{2})\. (.*?) \((.*?)\)<\/b><\/summary>', details_content, re.IGNORECASE)
        if summary_match:
            dim_id = summary_match.group(1)
            dim_name = summary_match.group(2).strip()
            dim_focus = summary_match.group(3).strip()
            
            dim = {
                'id': dim_id,
                'name': dim_name,
                'focus': dim_focus,
                'primary': [],
                'supporting': []
            }
            
            parts = details_content.split('### Supporting Artifacts')
            
            # Primary Corpus
            dim['primary'] = parse_table(parts[0], is_supporting=False)
            
            # Supporting Artifacts
            if len(parts) > 1:
                dim['supporting'] = parse_table(parts[1], is_supporting=True)
                
            parsed_dimensions.append(dim)
            
    return parsed_dimensions

def parse_table(block, is_supporting):
    lines = block.strip().split('\n')
    items = []
    
    sep_index = -1
    for i, line in enumerate(lines):
        if '---|' in line:
            sep_index = i
            break
            
    for idx, line in enumerate(lines):
        # Allow header (sep_index - 1) up to separator (sep_index).
        if '|' not in line or idx == sep_index or idx == sep_index - 1:
            continue
            
        cols = [c.strip() for c in line.split('|')]
        # Filter empty columns at start/end from splitting "| cell | cell |"
        cols = [c for c in cols if c]
        
        if len(cols) >= 4:
            title_raw = cols[0]
            title_match = re.search(r'\[(.*?)\]', title_raw)
            clean_title = title_match.group(1) if title_match else title_raw.strip()
            
            path_match = re.search(r'\(\.\/(.*?)\)', line)
            path = path_match.group(1) if path_match else ''
            
            if '✅' in line:
                status = 'ready'
            elif '🟡' in line:
                status = 'hardening'
            else:
                status = 'draft'
                
            if is_supporting:
                items.append({
                    'title': clean_title,
                    'role': cols[1],
                    'maturity': cols[2],
                    'nature': 'Supporting',
                    'source': cols[3],
                    'status': status,
                    'path': path
                })
            else:
                items.append({
                    'title': clean_title,
                    'nature': cols[1],
                    'role': cols[2],
                    'source': cols[3],
                    'status': status,
                    'path': path
                })
                
    return items

def main():
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    readme_path = os.path.join(repo_root, 'README.md')
    manifest_path = os.path.join(repo_root, 'docs', 'manifest.json')
    
    dimensions = parse_readme(readme_path)
    print(f"Parsed {len(dimensions)} dimensions.")
    
    # Calculate totals
    total_items = sum(len(d['primary']) + len(d['supporting']) for d in dimensions)
    print(f"Total items parsed: {total_items}")
    
    os.makedirs(os.path.dirname(manifest_path), exist_ok=True)
    with open(manifest_path, 'w', encoding='utf-8') as f:
        json.dump(dimensions, f, indent=2, ensure_ascii=False)
        
    print(f"Manifest written to {manifest_path}")

if __name__ == '__main__':
    main()
