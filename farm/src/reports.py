import os
import json
from datetime import datetime
from files import load_data_from_file  
from utils.terminal import press_enter_to_continue
from utils.terminal import show_dashboard_header, show_options_module
from utils.message import WELCOME_DISPLAY_REPORTS

def type_register(inputs, animals, plants):
    """
    Pergunta o critério e retorna as listas ordenadas (inputs, animals, plants).
    """
    show_dashboard_header(WELCOME_DISPLAY_REPORTS, 85)
    show_options_module({
        "1": "Ordenar por nome (A-Z)",
        "2": "Ordenar por ID (A-Z)",
        "3": "Ordenar em ordem decrescente"
    })
    try:
        choice2 = int(input("escolha o metodo de ordenamento: "))
    except ValueError:
        choice2 = 1  # padrão

    if choice2 == 1:
        inputs_sorted  = sorted(inputs,  key=lambda i: i.get("name", "").lower())
        animals_sorted = sorted(animals, key=lambda i: i.get("species", "").lower())
        plants_sorted  = sorted(plants,  key=lambda i: i.get("crop_type", "").lower())
    elif choice2 == 2:
        inputs_sorted  = sorted(inputs,  key=lambda i: str(i.get("id", "")))
        animals_sorted = sorted(animals, key=lambda i: str(i.get("id", "")))
        plants_sorted  = sorted(plants,  key=lambda i: str(i.get("id", "")))
    elif choice2 == 3:
        inputs_sorted  = sorted(inputs,  key=lambda i: float(i.get("quantity", 0) or 0), reverse=True)
        animals_sorted = sorted(animals, key=lambda i: float(i.get("weight",   0) or 0), reverse=True)
        plants_sorted  = sorted(plants,  key=lambda i: float(i.get("area",     0) or 0), reverse=True)
    else:
        print("Opção inválida. Relatório ordenado por nome por padrão.")
        inputs_sorted  = sorted(inputs,  key=lambda i: i.get("name", "").lower())
        animals_sorted = sorted(animals, key=lambda i: i.get("species", "").lower())
        plants_sorted  = sorted(plants,  key=lambda i: i.get("crop_type", "").lower())

    return inputs_sorted, animals_sorted, plants_sorted


def generate_inputs_report():
    json_path_inputs  = os.path.join("farm", "data", "inputs.json")
    json_path_animals = os.path.join("farm", "data", "animals.json")
    json_path_plants  = os.path.join("farm", "data", "plants.json")
    report_path       = os.path.join("farm", "data", "report.txt")

    try:
        inputs  = load_data_from_file(json_path_inputs)
        animals = load_data_from_file(json_path_animals)
        plants  = load_data_from_file(json_path_plants)

        if not inputs and not animals and not plants:
            print("\nNenhum dado encontrado para gerar relatório. \n")
            return
    except FileNotFoundError:
        print("Arquivo não encontrado.")
        return
    except json.JSONDecodeError:
        print("Erro ao ler o arquivo JSON.")
        return

    show_options_module({
        "1": "Gerar relatório de Animais",
        "2": "Gerar relatório de Insumos",
        "3": "Gerar relatório de Plantações"
    })
    try:
        choice1 = int(input("resposta: "))
    except ValueError:
        print("Opção inválida.")
        return

    with open(report_path, "a", encoding="utf-8") as file:
        agora = datetime.now().strftime('%d/%m/%Y %H:%M:%S')

        if choice1 == 1:
            inputs, animals, plants = type_register(inputs, animals, plants)

            file.write("\n===== RELATÓRIO DE ANIMAIS =====\n")
            file.write(f"Data de geração: {agora}\n")
            file.write("================================\n\n")

            for animal in animals:
                file.write(
                    f"ID: {animal.get('id','N/A')} | "
                    f"Espécie: {animal.get('species','N/A')} | "
                    f"Idade: {animal.get('age','N/A')} | "
                    f"Peso: {animal.get('weight','N/A')} | "
                    f"Status: {animal.get('status','N/A')}\n"
                )

            file.write("\n--------------------------------\n")
            file.write(f"Total de animais cadastrados: {len(animals)}\n")
            print("\n")
            press_enter_to_continue()

        elif choice1 == 2:
            inputs, animals, plants = type_register(inputs, animals, plants)

            file.write("\n===== RELATÓRIO DE INSUMOS =====\n")
            file.write(f"Data de geração: {agora}\n")
            file.write("================================\n\n")

            for insumo in inputs:
                file.write(
                    f"ID: {insumo.get('id','N/A')} | "
                    f"Nome: {insumo.get('name','N/A')} | "
                    f"Quantidade: {insumo.get('quantity',0)} {insumo.get('unit','')} | "
                    f"Categoria: {insumo.get('category','N/A')}\n"
                )

            file.write("\n--------------------------------\n")
            file.write(f"Total de insumos cadastrados: {len(inputs)}\n")
            press_enter_to_continue()

        elif choice1 == 3:
            inputs, animals, plants = type_register(inputs, animals, plants)

            file.write("\n===== RELATÓRIO DE PLANTAÇÕES =====\n")
            file.write(f"Data de geração: {agora}\n")
            file.write("===================================\n\n")

            for plant in plants:
                file.write(
                    f"ID: {plant.get('id','N/A')} | "
                    f"Cultura: {plant.get('crop_type','N/A')} | "
                    f"Área: {plant.get('area','N/A')} | "
                    f"Plantio: {plant.get('planting_date','N/A')} | "
                    f"Colheita: {plant.get('harvest_date','N/A')} | "
                    f"Status: {plant.get('status','N/A')}\n"
                )

            file.write("\n-----------------------------------\n")
            file.write(f"Total de plantações cadastradas: {len(plants)}\n")
            press_enter_to_continue()

        else:
            print("Opção inválida.")
