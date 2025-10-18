import os
from time import sleep
from files import save_data_to_file, generate_id
from utils.logs import ANIMAL_REGISTERED

def register_animal():
    file_path = os.path.join("farm", "data", "animals.json")
    
    print(ANIMAL_REGISTERED)
    
    try:
        species = input("Digite a espécie do animal: ").strip()
        if not species:
            raise ValueError("Espécie não pode ser vazia")
        
        age = float(input("Digite a idade do animal: "))
        if age < 0:
            raise ValueError("Idade não pode ser negativa")
        
        weight = float(input("Digite o peso do animal (em kg): "))
        if weight <= 0:
            raise ValueError("Peso deve ser maior que zero")
        
        status = input("Digite o status do animal [active/sold/dead]: ").strip().lower()
        if status not in ["active", "sold", "dead"]: # se o status for diferente dessas opções retorna erro
            raise ValueError("Status inválido")
        
        animal_data = {
            "id": generate_id(file_path),
            "species": species,
            "age": age,
            "weight": weight,
            "status": status
        }
        
        save_data_to_file(file_path, animal_data)
        print("\n Animal cadastrado com sucesso!")
        
    except ValueError as e:
        print(f"\n Erro: {e}")
    except Exception as e:
        print(f"\n Erro inesperado: {e}")

    sleep(1.5)

