import os
from time import sleep
from files import save_data_to_file, generate_id
from utils.message import ANIMAL_REGISTERED


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
    search_lower = search.lower()  
    for animal in animals:
        if str(animal['id']) == search:
            find.append(animal)
        elif search_lower in animal['species'].lower():
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
def update_animal():    
    from files import load_data_from_file, overwrite_data_in_file
    file_path = os.path.join("farm", "data", "animals.json")
    
    animals = load_data_from_file(file_path)
    
    try:
        animal_id = int(input("Digite o ID do animal que deseja atualizar: "))
        
        for animal in animals:
            if animal['id'] == animal_id:
                print(f"Atualizando dados do animal ID {animal_id}:")
                
                new_species = input(f"Espécie ({animal['species']}): ").strip()
                if new_species:
                    animal['species'] = new_species
                
                new_age = input(f"Idade ({animal['age']}): ").strip()
                if new_age:
                    animal['age'] = float(new_age)
                
                new_weight = input(f"Peso ({animal['weight']}): ").strip()
                if new_weight:
                    animal['weight'] = float(new_weight)
                
                new_status = input(f"Status ({animal['status']}): ").strip().lower()
                if new_status in ["active", "sold", "dead"]:
                    animal['status'] = new_status
                elif new_status:
                    raise ValueError("Status inválido")
                
                overwrite_data_in_file(file_path, animals)
                print("Dados do animal atualizados com sucesso!")
                break
        else:
            print("Animal com o ID fornecido não encontrado.")
    
    except ValueError as e:
        print(f"\n Erro: {e}")
    except Exception as e:
        print(f"\n Erro inesperado: {e}")
    
    sleep(1.5)
def delete_animal():
    from files import load_data_from_file, overwrite_data_in_file
    file_path = os.path.join("farm", "data", "animals.json")
    
    animals = load_data_from_file(file_path)
    
    try:
        animal_id = int(input("Digite o ID do animal que deseja deletar: "))
        
        for i, animal in enumerate(animals):
            if animal['id'] == animal_id:
                confirm = input(f"Tem certeza que deseja deletar o animal ID {animal_id} (s/n)? ").strip().lower()
                if confirm == 's':
                    animals.pop(i)
                    overwrite_data_in_file(file_path, animals)
                    print("Animal deletado com sucesso!")
                else:
                    print("Operação cancelada.")
                break
        else:
            print("Animal com o ID fornecido não encontrado.")
    
    except ValueError as e:
        print(f"\n Erro: {e}")
    except Exception as e:
        print(f"\n Erro inesperado: {e}")
    
    sleep(1.5)