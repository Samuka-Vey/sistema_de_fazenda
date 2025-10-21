import json
import os

def save_data_to_file(file_path, data):
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            try:
                existing_data = json.load(file)
            except json.JSONDecodeError:
                existing_data = []
    else:
        existing_data = []
    
    existing_data.append(data)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(existing_data, file, ensure_ascii=False, indent=4)

def load_data_from_file(file_path):
    if not os.path.exists(file_path):
        return []
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data if isinstance(data, list) else []
    except (json.JSONDecodeError, IOError):
        return []

def overwrite_data_in_file(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
        
def generate_id(file_path):
    data = load_data_from_file(file_path)
    if not data:
        return 1
    return data[-1].get('id', 0) + 1