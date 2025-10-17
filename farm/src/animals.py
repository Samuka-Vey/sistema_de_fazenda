import os
from time import sleep
import json
def register_animal():
    from utils.register import save_data_to_file
    from utils.register import generate_id
    
    file_path = os.path.join("farm", "data", "animals.json")

    
    
    print("Cadastramento de animal.")
    animal_data = {
        "id": generate_id(file_path),
        "species": input("Digite a espécie do animal: "),
        "age": int(input("Digite a idade do animal: ")),
        "weight": float(input("Digite o peso do animal (em kg): ")),
        "health_status": input("Digite o estado de saúde do animal [active, sold, dead]: ")
    }


    save_data_to_file(file_path, animal_data)

    sleep(1.5)

    print("Animal cadastrado com sucesso!...")