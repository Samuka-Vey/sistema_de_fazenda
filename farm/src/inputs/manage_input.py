
import os

from time import sleep
from files import save_data_to_file, generate_id
from utils.paths import get_data_path
from utils.message import INPUTS_REGISTERED

FILE_PATH = get_data_path("inputs.json")

def register_input():

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
        'id': generate_id(FILE_PATH),
        'name': name,
        'quantity': quantity,
        'unit': unit,
        'category': category
        }
        
        save_data_to_file(FILE_PATH, inputs_data)
        print("Insumo cadastrado com sucesso!")


    except ValueError as e:
        print(f"\n Erro: {e}")

    except Exception as e2:
        print(f"\n Erro inesperado: {e2}")

    

    sleep(1.5)
def list_inputs():
    from files import load_data_from_file
    
    inputs = load_data_from_file(FILE_PATH)
    
    if not inputs:
        print("\n Nenhum insumo cadastrado.")
    else:
        print("\n Lista de Insumos Cadastrados:\n")
        for inp in inputs:
            print(f"ID: {inp['id']}")
            print(f"Nome: {inp['name']}")
            print(f"Quantidade em Estoque: {inp['quantity']:.1f} {inp['unit']}")
            print(f"Categoria: {inp['category']}")
            print("-"*30)
    
    sleep(1.5)
def read_inputs():
    from files import load_data_from_file
    inputs = load_data_from_file(FILE_PATH)
    search = input("Digite o id ou nome do insumo: ")
    if not search:
        print("Entrada inválida")
        return
    find = []
    search_lower = search.lower()  
    for inp in inputs:
        if str(inp['id']) == search:
            find.append(inp)
        elif search_lower in inp['name'].lower():
            find.append(inp)
    if find:
        print(f'\n{len(find)} insumo(s) encontrado(s):')
        for i in find:
            print(f"ID: {i['id']} | Nome: {i['name']} | Quantidade em Estoque: {i['quantity']:.1f} {i['unit']} | Categoria: {i['category']}")
    else:
        print("Nenhum insumo encontrado.")

def update_input():
    from files import load_data_from_file, overwrite_data_in_file
    
    try:
        inputs = load_data_from_file(FILE_PATH)
        input_id = int(input("Digite o ID do insumo que deseja atualizar: "))
        
        for inp in inputs:
            if inp['id'] == input_id:
                print(f"Atualizando insumo: {inp['name']}")
                
                name = str(input(f"Novo nome ({inp['name']}): ") or inp['name']).strip()
                quantity_input = input(f"Nova quantidade em estoque ({inp['quantity']}): ")
                quantity = float(quantity_input) if quantity_input else inp['quantity']
                
                if quantity <= 0:
                    raise ValueError("A quantidade em estoque deve ser maior que 0.")
                
                unit = str(input(f"Nova unidade de medida ({inp['unit']}): ") or inp['unit']).strip()
                
                category_input = input(f"Nova categoria ({inp['category']}): ").strip().lower()
                category = category_input if category_input else inp['category']
                
                if category not in ["feed", "seed", "medicine"]:
                    raise ValueError("Categoria inválida.")
                
                inp['name'] = name
                inp['quantity'] = quantity
                inp['unit'] = unit
                inp['category'] = category
                
                overwrite_data_in_file(FILE_PATH, inputs)
                print("Dados do insumo atualizados com sucesso!")
                break
        else:
            print("Insumo com o ID fornecido não encontrado.")
    except ValueError as e:
        print(f"\n Erro: {e}")
    except Exception as e:
        print(f"\n Erro inesperado: {e}")
def delete_input():
    from files import load_data_from_file, overwrite_data_in_file
    
    try:
        inputs = load_data_from_file(FILE_PATH)
        input_id = int(input("Digite o ID do insumo que deseja deletar: "))
        
        for i, inp in enumerate(inputs):
            if inp['id'] == input_id:
                confirm = input(f"Tem certeza que deseja deletar o insumo '{inp['name']}'? (s/n): ").strip().lower()
                if confirm == 's':
                    inputs.pop(i)
                    overwrite_data_in_file(FILE_PATH, inputs)
                    print("Insumo deletado com sucesso!")
                else:
                    print("Operação de deleção cancelada.")
                break
        else:
            print("Insumo com o ID fornecido não encontrado.")
    except ValueError as e:
        print(f"\n Erro: {e}")
    except Exception as e:
        print(f"\n Erro inesperado: {e}")