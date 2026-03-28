import os
import re
import json
import yaml

def extract_frontmatter(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            # Procura por blocos delimitados por ---
            match = re.search(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
            if match:
                return yaml.safe_load(match.group(1))
    except Exception as e:
        print(f"Erro ao ler {file_path}: {e}")
    return None

def generate_catalog(base_dir='artifacts'):
    catalog = []
    
    # Percorrer as pastas 01 a 10
    for dimension_folder in sorted(os.listdir(base_dir)):
        if not re.match(r'^\d{2}_', dimension_folder):
            continue
            
        dim_id = dimension_folder.split('_')[0]
        dim_path = os.path.join(base_dir, dimension_folder)
        
        # Percorrer subpastas (policies, standards, templates)
        for sub_folder in ['policies', 'standards', 'templates']:
            sub_path = os.path.join(dim_path, sub_folder)
            if not os.path.exists(sub_path):
                continue
                
            for file_name in os.listdir(sub_path):
                if file_name.endswith('.md'):
                    file_path = os.path.join(sub_path, file_name)
                    metadata = extract_frontmatter(file_path)
                    
                    if metadata:
                        # Limpar e normalizar os dados
                        catalog_entry = {
                            "id": metadata.get('id', file_name.replace('.md', '').upper()),
                            "dimension": dim_id,
                            "title": metadata.get('title', 'Untitled'),
                            "nature": metadata.get('artifact_type', sub_folder.rstrip('s')).capitalize(),
                            "status": metadata.get('status', 'unknown'),
                            "source": metadata.get('source_basis', 'Multiple'),
                            "path": f"./artifacts/{dimension_folder}/{sub_folder}/{file_name}"
                        }
                        catalog.append(catalog_entry)
                        
    return catalog

if __name__ == "__main__":
    catalog_data = generate_catalog()
    output_path = os.path.join('docs', 'catalog.json')
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(catalog_data, f, indent=2, ensure_ascii=False)
        
    print(f"Catálogo gerado com sucesso em {output_path} ({len(catalog_data)} itens)")
