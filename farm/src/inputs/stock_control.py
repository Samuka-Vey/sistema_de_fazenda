import json
import os
from files import save_data_to_file
from files import load_data_from_file


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
