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


def enter_inputs():
    file_path = os.path.join("farm","data","inputs.json")

    inputs = load_data_from_file(file_path)

    id_entering = input("Digite o id no insumo que deseja modificar")

    entering = float(input("Quanto deseja adicionar?: "))

    for enter in inputs:
        if (enter['id']) == id_entering:
            enter["quantity"] = enter["quantity"] + entering

            with open(file_path, "w", encoding="utf-8") as file:
                json.dump(inputs, file ,ensure_ascii=False, indent= 4)
                break
        else:
            print("Insumo não encontrado")


def removal_inputs():
    file_path = os.path.join("farm","data","inputs.json")

    inputs = load_data_from_file(file_path)

    id_removing  = input("Digite o id no insumo que deseja modificar")
    removing = input("Quanto deseja remover?: ")

    for enter in inputs:
        if (enter["id"]) == id_removing:
            enter["quantity"] = enter["quantity"] - removing
            with open(file_path, "w", encoding="utf-8") as file:
                json.dump(inputs, file , ensure_ascii=8, indent=4)
                break
        else:
            print("Insumo não encontrado")

        
def control_stock():
    file_path = os.path.join("farm","data","inputs.json")
    inputs = load_data_from_file(file_path)

    print("Qual operação deseja fazer?" \
    "1. Adicionar entrada de insumo" \
    "2. Retirar insumos do estoque" \
    "")

    operation = input("Qual operação será realizada?: ")

    if operation == "1":
        enter_inputs
    elif operation == "2":
        removal_inputs
        

