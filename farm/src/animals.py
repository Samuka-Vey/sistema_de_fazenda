import os
from time import sleep
from files import save_data_to_file, generate_id

FILE_PATH = os.path.join("farm", "data", "animals.json")
from utils.logs import ANIMAL_REGISTERED
def register_animal():
    
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
            "id": generate_id(FILE_PATH),
            "species": species,
            "age": age,
            "weight": weight,
            "status": status
        }
        
        save_data_to_file(FILE_PATH, animal_data)
        print("\n Animal cadastrado com sucesso!")
        
    except ValueError as e:
        print(f"\n Erro: {e}")
    except Exception as e:
        print(f"\n Erro inesperado: {e}")

    sleep(1.5)


def search_animal():
    from files import load_data_from_file
    animals = load_data_from_file(FILE_PATH)

    search = input("Digite o ID ou nome do animal: ").strip().lower()
    if not search:
        print("Entrada inválida.")
        return

    encontrados = []
    for animal in animals:
        if str(animal["id"]) == search:
            encontrados.append(animal)
        elif search in animal["species"].lower():
            encontrados.append(animal)

    if encontrados:
        print(f"\n{len(encontrados)} animal(is) encontrado(s):")
        for a in encontrados:
            print(f"ID: {a['id']} | Espécie: {a['species']} | Idade: {a['age']} | Peso: {a['weight']} | Status: {a['status']}")
    else:
        print("Nenhum animal encontrado.")
