import os
from datetime import datetime
from time import sleep
from files import load_data_from_file, save_data_to_file, overwrite_data_in_file

def register_plants_movement():
    plants_file = os.path.join("farm", "data", "plants.json")
    movements_file = os.path.join("farm", "data", "movements.json")

    plants = load_data_from_file(plants_file)

    if not plants:
        print("Nenhuma planta cadastrada.")
        sleep(1.5)
        return

    try:
        plant_id = int(input("\nDigite o ID da planta: "))
    except ValueError:
        print("\nID inválido!")
        sleep(1.5)
        return

    plant = None
    for a in plants:
        if a["id"] == plant_id:
            plant = a
            break

    if not plant:
        print(f"\nPlanta com ID {plant_id} não encontrada!")
        sleep(1.5)
        return

    print(f"\nPlanta encontrada: {plant.get('crop_type', 'N/D')} (Status atual: {plant.get('status', 'N/D')})")
    print("[1] Plantada")
    print("[2] Colhida")
    print("[3] Cultura em rotação")
    print("[4] Inativa")
    option = input("Escolha o tipo de movimentação: ").strip()

    new_status = None
    description = ""
    area = None
    buyer = None
    price = None

    if option == "1":
        new_status = "planted"
        description = input("Descrição do novo plantio: ")
        try:
            area = float(input("Qual área plantada em hectares?: "))
        except ValueError:
            print("\nValor inválido! Movimentação cancelada.")
            sleep(1.5)
            return

    elif option == "2":
        new_status = "harvested"
        description = input("Descrição da colheita: ")
        try:
            area = float(input("Digite a área colhida em hectares: "))
        except ValueError:
            print("\nValor inválido! Movimentação cancelada.")
            sleep(1.5)
            return

        print("\nVocê deseja vender a colheita?")
        print("[1] Desejo vender")
        print("[2] Não desejo vender")
        suboption = input("Escolha uma opção: ").strip()

        if suboption == "1":
            try:
                price = float(input("Digite o valor da venda em R$: "))
                buyer = input("Digite o nome do comprador: ").strip()
                new_status = "sold"
            except ValueError:
                print("\nValor inválido! Venda não aprovada.")
                sleep(1.5)
                return
        elif suboption == "2":
            print("\nColheita registrada sem venda.")
        else:
            print("\nOpção não reconhecida. Colheita será registrada apenas como colhida.")

    elif option == "3":
        new_status = "rotated"
        description = input("Descreva os motivos da rotação de cultura: ")

    elif option == "4":
        new_status = "inactive"
        description = input("Explique por que a área está inativa: ")

    else:
        print("\nOpção inválida.")
        sleep(1.5)
        return

    plant["status"] = new_status
    overwrite_data_in_file(plants_file, plants)

    movement = {
        "type": "plant",
        "plant_id": plant_id,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "status": new_status,
        "description": description,
        "area": area,
        "buyer": buyer,  
        "price": price
    }

    save_data_to_file(movements_file, movement)

    print("\nMovimentação registrada com sucesso!")
    sleep(1.5)
