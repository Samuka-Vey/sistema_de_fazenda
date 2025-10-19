import os
from time import sleep
from files import save_data_to_file, generate_id
from utils.logs import PLANTS_REGISTERED
from datetime import datetime

def validate_date_iso(dateinput):
    try:
        planting_date_obj = datetime.striptime(dateinput,'%d/%m/%Y')
        return planting_date_obj.strftime('%Y/%m/%d')
    except ValueError:
        raise ValueError("A data deve ser no formato dd/mm/aaaa e ser uma data válida")

def register_plants():
    file_path = os.path.join("farm", "data", "plants.json")
    
    print(PLANTS_REGISTERED)
    
    try:
        crop_type = input("Digite a cultura plantada: ").strip()
        if not crop_type:
            raise ValueError("Cultura plantada não pode ser vazia")
        
        area = float(input("Digite a área plantada em hectares: "))
        if area < 0:
            raise ValueError("Área plantada não pode ser negativa")
        
        planting_date = input("Digite a data do plantio (dd/mm/aaaa): ") #Dúvida sobre string formato ISO
        planting_date_iso = validate_date_iso(planting_date)
        
        
        harvest_date = (input("Digite a data estipulada para colheita (dd/mm/aaaa): "))
        if harvest_date <= 0:
            raise ValueError("A data deve ser no formato dd/mm/aaaa")
        
        status = input("Digite o status da cultura [planted/harvested/rotated/inactive]: ").strip().lower()
        if status not in ["planted","harvested","rotated","inactive"]: # se o status for diferente dessas opções retorna erro
            raise ValueError("Status inválido")
        
        plants_data = {
            "id": generate_id(file_path),
            "crop_type": crop_type,
            "area": area,
            "planting_date": planting_date_iso,
            "harvest_date": harvest_date,
            "status": status
        }
        
        save_data_to_file(file_path, plants_data)
        print("\n Cultura de planta cadastrada com sucesso!")
        
    except ValueError as e:
        print(f"\n Erro: {e}")
    except Exception as e:
        print(f"\n Erro inesperado: {e}")

    sleep(1.5)