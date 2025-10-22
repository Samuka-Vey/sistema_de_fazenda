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
def delete_plants():
    from files import load_data_from_file, overwrite_data_in_file
    file_path = os.path.join("farm", "data", "plants.json")
    
    try:
        plants = load_data_from_file(file_path)
        plants_id = int(input("Digite o ID da plantação que deseja deletar: "))
        
        for i, inp in enumerate(plants):
            if inp['id'] == plants_id:
                confirm = input(f"Tem certeza que deseja deletar a plantação '{inp['name']}'? (s/n): ").strip().lower()
                if confirm == 's':
                    plants.pop(i)
                    overwrite_data_in_file(file_path, plants)
                    print("Plantação deletado com sucesso!")
                else:
                    print("Operação de deleção cancelada.")
                break
        else:
            print("Insumo com o ID fornecido não encontrado.")
    except ValueError as e:
        print(f"\n Erro: {e}")
    except Exception as e:
        print(f"\n Erro inesperado: {e}")
def update_plants():
    from files import load_data_from_file, overwrite_data_in_file
    file_path = os.path.join("farm", "data", "plants.json")
    
    try:
        plants = load_data_from_file(file_path)
        plant_id = int(input("Digite o ID da plantação que deseja atualizar: "))
        
        for plant in plants:
            if plant['id'] == plant_id:
                print(f"Atualizando plantação ID {plant_id}:")
                
                new_crop_type = input(f"Cultura ({plant['crop_type']}): ").strip()
                if new_crop_type:
                    plant['crop_type'] = new_crop_type
                
                new_area = input(f"Área ({plant['area']} ha): ").strip()
                if new_area:
                    area_value = float(new_area)
                    if area_value < 0:
                        raise ValueError("Área não pode ser negativa")
                    plant['area'] = area_value
                
                new_planting_date = input(f"Data do Plantio ({plant['planting_date']}): ").strip()
                if new_planting_date:
                    plant['planting_date'] = validate_date_iso(new_planting_date)
                
                new_harvest_date = input(f"Data da Colheita ({plant['harvest_date']}): ").strip()
                if new_harvest_date:
                    plant['harvest_date'] = validate_date_iso(new_harvest_date)
                
                new_status = input(f"Status ({plant['status']}): ").strip().lower()
                if new_status in ["planted","harvested","rotated","inactive"]:
                    plant['status'] = new_status
                elif new_status:
                    raise ValueError("Status inválido")
                
                overwrite_data_in_file(file_path, plants)
                print("Dados da plantação atualizados com sucesso!")
                break
        else:
            print("Plantação com o ID fornecido não encontrado.")
    except ValueError as e:
        print(f"\n Erro: {e}")
    except Exception as e:
        print(f"\n Erro inesperado: {e}")
    
    sleep(1.5)