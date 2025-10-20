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

def read_animal():
    from files import load_data_from_file
    file_path = os.path.join("farm", "data", "animals.json")
    
    animals = load_data_from_file(file_path)
    
    search = input("Digite o id ou nome do animal: ")
    
    if not search:
        print("Entrada inválida")
        return
    
    find = []
    
    for animal in animals:
        if str(animal['id']) == search:
            find.append(animal)
        elif search in animal['species'].lower():
            find.append(animal) 
            
    if find:
        print(f'\n{len(find)} animal(is) encontrado(s):')
        for a in find:
            print(f"ID: {a['id']} | Espécie: {a['species']} | Idade: {a['age']} | Peso: {a['weight']} | Status: {a['status']}")
    else:
        print("Nenhum animal encontrado.")
def list_animals():
    from files import load_data_from_file
    file_path = os.path.join("farm", "data", "animals.json")
    
    animals = load_data_from_file(file_path)
    
    if not animals:
        print("\n Nenhum animal cadastrado.")
    else:
        print("\n Lista de Animais Cadastrados:\n")
        for animal in animals:
            print(f"ID: {animal['id']}")
            print(f"Espécie: {animal['species']}")
            print(f"Idade: {animal['age']} anos")
            print(f"Peso: {animal['weight']} kg")
            print(f"Status: {animal['status']}")
            print("-"*30)
    
    sleep(1.5)