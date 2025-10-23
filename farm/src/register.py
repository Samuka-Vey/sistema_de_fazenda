import os
import json
from datetime import datetime
from files import load_data_from_file  



def type_register():
     
    json_path_inputs = os.path.join("farm", "data", "inputs.json")
    json_path_plants = os.path.join("farm", "data", "plants.json")
    json_path_animals = os.path.join("farm", "data", "animals.json")

    report_path = os.path.join("farm", "data", "report.txt")
    inputs = load_data_from_file(json_path_inputs)
    # animals = 
    # plans = 

    print(""" GERADOR DE RELATORIOS 
            1. para ordernar por nome (A,Z)
            2. para ordernar por ID (A,Z)
            3. para ordernar em ordem descrescente 
          
""")
    choice2 = int(input("escolha o metodo de ordenamento: "))

    if choice2 == 1:
        inputs.sort(key=lambda i: i.get("name", "").lower())
    elif choice2 == 2:
        inputs.sort(key=lambda i: str(i.get("id", "")).lower())
    elif choice2 == 3:
        inputs.sort(key=lambda i: float(i.get("quantity", 0)), reverse=True)
    else:
        print("Opção inválida. Relatório ordenado por nome por padrão.")
        inputs.sort(key=lambda i: i.get("name", "").lower())
   

def generate_inputs_report():
    
    json_path = os.path.join("farm", "data", "inputs.json")
    report_path = os.path.join("farm", "data", "report.txt")

    try:
        inputs = load_data_from_file(json_path)
        if not inputs:
            print("Nenhum insumo cadastrado para gerar relatório.")
            return
    except FileNotFoundError:
        print("Arquivo de insumos não encontrado.")
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
    

    with open(report_path, "w", encoding="utf-8") as file:
        file.write("===== RELATÓRIO DE INSUMOS =====\n")
        file.write(f"Data de geração: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")
        file.write("================================\n\n")


        if choice1 == 1:
            type_register()
        elif choice1 == 2:
            type_register()
            for insumo in inputs:
                    file.write(f"ID: {insumo.get('id', 'N/A')} | ")
                    file.write(f"Nome: {insumo.get('name', 'N/A')} | ")
                    file.write(f"Quantidade: {insumo.get('quantity', 0)} {insumo.get('unit', '')} | ")
                    file.write(f"Categoria: {insumo.get('category', 'N/A')}\n")
        elif choice1 == 3:
            type_register()    
        
    

       
        file.write("\n--------------------------------\n")
        file.write(f"Total de insumos cadastrados: {len(inputs)}\n")
    print(f"✅ Relatório gerado com sucesso em: {report_path}")

