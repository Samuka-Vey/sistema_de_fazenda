import os
from datetime import datetime
from time import sleep
from files import load_data_from_file, save_data_to_file, overwrite_data_in_file

def register_animal_movement():
    animals_file = os.path.join("farm", "data", "animals.json")
    movements_file = os.path.join("farm", "data", "movements.json")

    animals = load_data_from_file(animals_file)

    if not animals:
        print("\nNenhum animal cadastrado.")
        sleep(1.5)
        return

    try:
        animal_id = int(input("\nDigite o ID do animal: "))
    except ValueError:
        print("\nID inválido!")
        sleep(1.5)
        return

    animal = None
    for a in animals:
        if a["id"] == animal_id:
            animal = a
            break

    if not animal:
        print(f"\nAnimal com ID {animal_id} não encontrado!")
        sleep(1.5)
        return

    print(f"\nAnimal encontrado: {animal['species']} (Status atual: {animal['status']})")
    print("[1] Venda")
    print("[2] Falecimento")
    option = input("Escolha o tipo de movimentação: ")

    if option == "1":
        new_status = "sold"
        description = input("Descrição da venda: ")
        buyer = input("Nome do comprador: ")
        try:
            value = float(input("Valor da venda (em R$): "))
        except ValueError:
            print("\nValor inválido! Movimentação cancelada.")
            sleep(1.5)
            return
    elif option == "2":
        new_status = "dead"
        description = input("Descrição do falecimento: ")
        buyer = None
        value = 0.0
    else:
        print("\nOpção inválida.")
        sleep(1.5)
        return

    animal["status"] = new_status
    overwrite_data_in_file(animals_file, animals)

    movement = {
        "type": "animal",
        "animal_id": animal_id,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "status": new_status,
        "description": description,
        "buyer": buyer,
        "value": value,
    }

    save_data_to_file(movements_file, movement)

    print("\nMovimentação registrada com sucesso!")
    sleep(1.5)
