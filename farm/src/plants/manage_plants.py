import os
from time import sleep
from files import save_data_to_file, generate_id
from datetime import datetime, timedelta
def validate_date_iso(dateinput):
    try:
        
        planting_date_obj = datetime.strptime(dateinput, '%d/%m/%Y')
        return planting_date_obj.strftime('%Y-%m-%d')
    except ValueError:
        raise ValueError("A data deve ser no formato dd/mm/aaaa e ser uma data válida")   
def register_plants():
    file_path = os.path.join("farm", "data", "plants.json")
    
    
    try:
        crop_type = input("Digite a cultura plantada: ").strip()
        if not crop_type:
            raise ValueError("Cultura plantada não pode ser vazia")
        
        area = float(input("Digite a área plantada em hectares: "))
        if area < 0:
            raise ValueError("Área plantada não pode ser negativa")
        
        planting_date = input("Digite a data do plantio (dd/mm/aaaa): ")
        planting_date_iso = validate_date_iso(planting_date)
        
        planting_date_obj = datetime.strptime(planting_date_iso, "%Y-%m-%d").date() # Conversão para objeto date para realizar cálculos
 
        days_harvest = {
            "milho": 120,
            "soja": 110,
            "arroz": 100,
            "hortaliças": 30
        }
        days_until_harvest = days_harvest.get(crop_type.lower(), 90)
        harvest_date_obj = planting_date_obj + timedelta(days=days_until_harvest)

        harvest_date_iso = harvest_date_obj.isoformat() # Conversão para ISO
        
        status = input("Digite o status da cultura [planted/harvested/rotated/inactive]: ").strip().lower()
        if status not in ["planted","harvested","rotated","inactive"]:
            raise ValueError("Status inválido")
        
        plants_data = {
            "id": generate_id(file_path),
            "crop_type": crop_type,
            "area": area,
            "planting_date": planting_date_iso,
            "harvest_date": harvest_date_iso,
            "status": status
        }
        
        save_data_to_file(file_path, plants_data)
        print("\nCultura de planta cadastrada com sucesso!")


    except ValueError as e:
        print(f"\nErro: {e}")
    except Exception as e:
        print(f"\nErro inesperado: {e}")

    sleep(1.5)
def read_plants():
    from files import load_data_from_file 
    file_path= os.path.join("farm","data","plants.json") 
    plants=load_data_from_file(file_path) 

    search = input("digite o id ou nome da plantação: ")

    if not search:
        print("entrada invalida") 
        return 
    
    find = [] 

    for plant in plants:
        if str(plant['id']) == search: 
            find.append(plant) 
        elif search in plant ['crop_type'].lower(): 
            find.append(plant) 

    if not find:
        print("\nNenhuma plantação encontrada.")
    else:
        print("\nLista de plantações encontradas:\n")
        for plant in find:
                print(f"id: {plant['id']} ")
                print(f"tipo_de_colheita: {plant['crop_type']}")
                print(f"Area: {plant['area']} hectare")
                print(f"data_de_plantio: {plant['planting_date']}")
                print(f"data_de_colheita: {plant['harvest_date']}")
                print(f"situação: {plant['status']}")
                print("-"*30)
                sleep(1.5)
def list_plants():
    from files import load_data_from_file
    file_path = os.path.join("farm", "data", "plants.json")
    
    plants = load_data_from_file(file_path)
    
    if not plants:
        print("Nenhuma plantação cadastrada.")
        return
    
    print("\nPlantações Cadastradas:")
    for plant in plants:
        print(f"ID: {plant['id']}")
        print(f"Cultura: {plant['crop_type']}")
        print(f"Área (ha): {plant['area']}")
        print(f"Data do Plantio: {plant['planting_date']}")
        print(f"Data da Colheita: {plant['harvest_date']}")
        print(f"Status: {plant['status']}")
        print("-"*30)
    
    sleep(2)
   