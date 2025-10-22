import json
import os
from files import overwrite_data_in_file, save_data_to_file,load_data_from_file


def description():
    description = str(input("Digite aqui a descrição da alteração e para que será usado:  "))
    return description


def register_inputs_movements():
    inputs = os.path.join("farm","data","inputs.json")
    moviments_file_inputs = os.path.join("farm","data","moviments_inputs.json")

    load_inputs = load_data_from_file(inputs)

    if not load_inputs:
        print("Nenhum insumo cadastrado")
        return
    
    
    try:
        id_inputs = int(input("Digite o ID do insumo: "))
    except ValueError:
        print("ID invalido")
        print(f"insumo com {id_inputs} não encontrado")
        return

    option_moviments = int(input("Qual tipo de movimentação gostaria de fazer?\n" \
    "1. Entrada\n" \
    "2. Saida\n" \
    "Digite aqui sua opção: "))


    find_inputs = print(f"""encotra-se insumo {load_inputs['id']} | atual quantidade no estoque: {load_inputs['quantity']} | 
                        unidade de armazenamento: {load_inputs['unit']} """)

    for inputs in load_inputs:
        try:
            if id_inputs == (inputs["id"]):
                if option_moviments == 1:
                    action = "entrada"
                    quantity = float(input("Quanto deseja adicionar?: "))
                    inputs["quantity"] =  inputs["quantity"] + quantity
                    description_add = description()

                    
            elif option_moviments == 2:
                action = "saida"
                quantity = float(input("Quanto deseja remover?: "))
                inputs["quantity"] = inputs["quamtity"] - quantity
                description_add = description()


        except ValueError:
            print("Algo não parece certo, reveja as informações.")

        else:
            print("Opçao invalida!")             



        overwrite_data_in_file(moviments_file_inputs, inputs)

        moviments = {
            'type': "insumo",
            'id':id_inputs,
            "description_and_use":description_add,
            # "date":
            'action': action,
            "quantity": quantity,
            "unit": load_inputs["unit"],
            "categoty": load_inputs["category"]
            }
                
        save_data_to_file(moviments,load_inputs)