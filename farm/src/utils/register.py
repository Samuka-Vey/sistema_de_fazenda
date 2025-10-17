'''
code service register: 1 - cadastrar animal 2 - Cadastrar plantação 3 - Cadastrar insumos
'''
import json
from time import sleep
from animals import register_animal
import os


def register(code_service):
    if code_service == 1:
        register_animal()
    
    
           
    else:
        print("Opção inválida. Tente novamente.")
        sleep(1.5)


def save_data_to_file(file_path, data):
    '''
    Save data to a JSON file.
    Args:
        file_path (str): The path to the JSON file.
        data (dict): The data to be saved.
    '''
    # Verifica se o arquivo existe
    if os.path.exists(file_path):
        # Ler os dados existentes
        with open(file_path, 'r', encoding='utf-8') as file:
            try:
                existing_data = json.load(file)
            except json.JSONDecodeError:
                existing_data = []
    else:
        existing_data = []

    # Adiciona o novo dado
    existing_data.append(data)

    # Salva os dados atualizados de volta no arquivo
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(existing_data, file, ensure_ascii=False, indent=4)



def generate_id(file_path):
 
    data = []

    if os.path.exists(file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                if not isinstance(data, list):
                    data = []
        except (json.JSONDecodeError, IOError):
            data = []

    if not data:
        return 1

    last_id = data[-1].get('id', 1) 
    return last_id + 1


