import os
import json
from datetime import datetime
from files import load_data_from_file  
from utils.terminal import press_enter_to_continue


def type_register():
     
    json_path_inputs = os.path.join("farm", "data", "inputs.json")
    json_path_plants = os.path.join("farm", "data", "plants.json")
    json_path_animals = os.path.join("farm", "data", "animals.json")

    report_path = os.path.join("farm", "data", "report.txt")
    inputs = load_data_from_file(json_path_inputs)
    animals = load_data_from_file(json_path_animals)

    print(""" GERADOR DE RELATORIOS 
            1. para ordernar por nome (A,Z)
            2. para ordernar por ID (A,Z)
            3. para ordernar em ordem descrescente 
          
""")
    choice2 = int(input("escolha o metodo de ordenamento: "))

    if choice2 == 1:
        inputs.sort(key=lambda i: i.get("name", "").lower())
        animals.sort(key=lambda i: i.get("species", "").lower())
    elif choice2 == 2:
        inputs.sort(key=lambda i: str(i.get("id", "")).lower())
        animals.sort(key=lambda i: str(i.get("id", "")).lower())
    elif choice2 == 3:
        inputs.sort(key=lambda i: float(i.get("quantity", 0)), reverse=True)
        animals.sort(key=lambda i: float(i.get("weight", 0)), reverse=True)
    else:
        print("Opção inválida. Relatório ordenado por nome por padrão.")
        inputs.sort(key=lambda i: i.get("name", "").lower())
        animals.sort(key=lambda i: i.get("species", "").lower())



def generate_inputs_report():
    
    json_path_inputs = os.path.join("farm", "data", "inputs.json")
    json_path_animals = os.path.join("farm", "data", "animals.json")
    report_path = os.path.join("farm", "data", "report.txt")

    try:
        inputs = load_data_from_file(json_path_inputs)
        animals = load_data_from_file(json_path_animals)
        if not inputs and not animals:
            print("Nenhum dado encontrado para gerar relatório.")
            return
    except FileNotFoundError:
        print("Arquivo não encontrado.")
        return
    except json.JSONDecodeError:
        print("Erro ao ler o arquivo JSON.")
        return
    
    print(""" PARA QUEM GOSTARIA DE GERAR O RELATORIO
          1. para animais
          2. para insumos
          3. para plantas
""")
    
    choice1 = int(input("resposta: "))
    

    with open(report_path, "a", encoding="utf-8") as file:
        if choice1 == 1:
            file.write("\n===== RELATÓRIO DE ANIMAIS =====\n")
            file.write(f"Data de geração: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")
            file.write("================================\n\n")
            type_register()
            
            for animal in animals:
                file.write(f"ID: {animal.get('id', 'N/A')} | ")
                file.write(f"Espécie: {animal.get('species', 'N/A')} | ")
                file.write(f"Idade: {animal.get('age', 'N/A')} | ")
                file.write(f"Peso: {animal.get('weight', 'N/A')} | ")
                file.write(f"Status: {animal.get('status', 'N/A')}\n")
            file.write("\n--------------------------------\n")
            file.write(f"Total de animais cadastrados: {len(animals)}\n")
            print("\n")
            press_enter_to_continue()

        elif choice1 == 2:
            file.write("\n===== RELATÓRIO DE INSUMOS =====\n")
            file.write(f"Data de geração: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")
            file.write("================================\n\n")
            type_register()
            for insumo in inputs:
                file.write(f"ID: {insumo.get('id', 'N/A')} | ")
                file.write(f"Nome: {insumo.get('name', 'N/A')} | ")
                file.write(f"Quantidade: {insumo.get('quantity', 0)} {insumo.get('unit', '')} | ")
                file.write(f"Categoria: {insumo.get('category', 'N/A')}\n")
            file.write("\n--------------------------------\n")
            file.write(f"Total de insumos cadastrados: {len(inputs)}\n")

            press_enter_to_continue()

        elif choice1 == 3:
            type_register()    

    print(f"✅ Relatório gerado com sucesso em: {report_path}")
