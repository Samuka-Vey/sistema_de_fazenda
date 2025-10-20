import json
import os
from files import save_data_to_file
from files import load_data_from_file


def list_inputs():
    file_path = os.path.join("farm", "data", "inputs.json")

    if not os.path.exists(file_path):
        print("Nenhum insumo cadastradado")
        return []

    with open(file_path, 'r', encoding="utf-8") as file:
        try:
            inputs = json.load(file)
        except json.JSONDecodeError:
            print("Erro ao ler arquivos de insumos")
            return []
    if not inputs:
        print("Nenhum insumo cadastrado")

    print("\n========= estoque atual de insumos =========")
    for _input in inputs:
        print(f"""ID: {_input['id']}] | nome: {_input['name']} | quantidade: {_input['quantity']} | \n
              unidade: {_input['unit']} | categoria: {_input['category']}""")

    print()
    return inputs


def read_inputs():
    file_path = os.path.join("farm", "data", "inputs.json")

    inputs = load_data_from_file(file_path)

    search = input("Digite nome ou id do insumo: ")

    if not search:
        print("Entrada invalida")
        return []

    find = []

    for _input in inputs:
        if str(_input["id"]) == search:
            find.append(_input)

        elif search in _input['name'].lower():
            find.append(_input)

    if find:
        print(f"{len(find)} insumo(s) encontrado(s). Segue as informações:\n")
        for i in find:
            print(
                f"ID: {i['id']} | Nome: {i['name']} | Quantidade: {i['quantity']} | Unidade: {i['unit']} | Categoria: {i['category']}")
    else:
        print("Deu ruim!")


print(""" O que deseja fazer?:\n
      1. diminuir estoque
      2. aumentar estoque
      3. deletar estoque
      """)
