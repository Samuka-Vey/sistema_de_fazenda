import json
import os
from files import overwrite_data_in_file, save_data_to_file, load_data_from_file
from datetime import datetime


def description():
    description = str(
        input("Digite aqui a descrição da alteração e para que será usado:  "))
    return description


def register_inputs_movements():
    items = os.path.join("farm", "data", "inputs.json")
    moviments_file_inputs = os.path.join(
        "farm", "data", "movements.json")

    load_inputs = load_data_from_file(items)

    if not load_inputs:
        print("Nenhum insumo cadastrado")
        return

    option_moviments = int(input("Qual tipo de movimentação gostaria de fazer?\n"
                                 "1. Entrada\n"
                                 "2. Saida\n"
                                 "Digite aqui sua opção: "))

    try:
        id_inputs = int(input("Digite o ID do insumo: "))
    except ValueError:
        print("ID invalido")
        print(f"insumo com {id_inputs} não encontrado")
        return

    found = None
    for inputs in load_inputs:
        if inputs["id"] == id_inputs:
            found = inputs
            print(f"""encotra-se insumo com id: {inputs['id']} | nome do insumo: {inputs['name']} | atual quantidade no estoque: {inputs['quantity']} | 
                            unidade de armazenamento: {inputs['unit']} """)

            break

    try:
        if found:
            if option_moviments == 1:
                action = "entrada"
                quantity = float(input("Quanto deseja adicionar?: "))
                inputs["quantity"] = inputs["quantity"] + quantity
                description_add = description()

            elif option_moviments == 2:
                action = "saida"
                quantity = float(input("Quanto deseja remover?: "))
                inputs["quantity"] = inputs["quantity"] - quantity
                description_add = description()
                if quantity > inputs["quantity"]:
                    print("Erro: quantidade maior que o estoque disponível.")
                    return

        else:
            print("Opçao invalida!")

    except ValueError:
        print("Algo não parece certo, reveja as informações.")

    overwrite_data_in_file(items, load_inputs)
    movements = {
        'type': "insumo",
        'id': id_inputs,
        'name': found.get("name"),
        "description_and_use": description_add,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'action': action,
        "quantity": quantity,
        "unit": found.get("unit", ""),
        "category": found.get("category", "sem categoria")
    }

    save_data_to_file(moviments_file_inputs, movements)

    if not found:
        print("Insumo nao cadastrado")
