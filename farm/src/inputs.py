import os

from time import sleep
from files import save_data_to_file, generate_id
from utils.logs import INPUTS_REGISTERED
def register_input():
    file_path = os.path.join("farm", "data", "inputs.json")

    print(INPUTS_REGISTERED)


    try:
       
        
        name = str(input("Digite o nome do insumo: ")).strip()
        
        quantity = float(input("Digite a quantidade disponivel no estoque: "))
        if quantity <= 0:
            raise ValueError("a quantidade disponivel no estoque é menor que 0 ?")
        
        unit = str(input("Digite a unidade de medida associada à quantidade: "))
        
        category = input("Digite o status do animal [feed/seed/medicine]: ").strip().lower()
        if category not in ["feed", "seed", "medicine"]:
            raise ValueError("Status inválido")
        
        inputs_data = {
        'id': generate_id(file_path),
        'name': name,
        'quantity': quantity,
        'unit': unit,
        'category': category
        }
        
        save_data_to_file(file_path, inputs_data)
        print("Insumo cadastrado com sucesso!")


    except ValueError as e:
        print(f"\n Erro: {e}")

    except Exception as e2:
        print(f"\n Erro inesperado: {e2}")

    

    sleep(1.5)

