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

    planta = None
    for a in plants:
        if a["id"] == plant_id:
            planta = a
            break

    if not planta:
        print(f"\nPlanta com ID {plant_id} não encontrada!")
        sleep(1.5)
        return

    print(f"\nPlanta encontrada: {planta.get('crop_type', 'N/D')} (Status atual: {planta.get('status', 'N/D')})")
    print("[1] Plantada")
    print("[2] Colhida")
    print("[3] Cultura em rotação")
    print("[4] Inativa")
    opcao = input("Escolha o tipo de movimentação: ").strip()

    novo_status = None
    descricao = ""
    area = None
    comprador = None
    price = None

    if opcao == "1":
        novo_status = "planted"
        descricao = input("Descrição do novo plantio: ")
        try:
            area = float(input("Qual área plantada em hectares?: "))
        except ValueError:
            print("\nValor inválido! Movimentação cancelada.")
            sleep(1.5)
            return

    elif opcao == "2":
        novo_status = "harvested"
        descricao = input("Descrição da colheita: ")
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
                comprador = input("Digite o nome do comprador: ").strip()
                novo_status = "sold"
            except ValueError:
                print("\nValor inválido! Venda não aprovada.")
                sleep(1.5)
                return
        elif suboption == "2":
            print("\nColheita registrada sem venda.")
        else:
            print("\nOpção não reconhecida. Colheita será registrada apenas como colhida.")

    elif opcao == "3":
        novo_status = "rotated"
        descricao = input("Descreva os motivos da rotação de cultura: ")

    elif opcao == "4":
        novo_status = "inactive"
        descricao = input("Explique por que a área está inativa: ")

    else:
        print("\nOpção inválida.")
        sleep(1.5)
        return

    planta["status"] = novo_status
    overwrite_data_in_file(plants_file, plants)

    movement = {
        "type": "plant",
        "planta_id": plant_id,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "status": novo_status,
        "description": descricao,
        "area": area,
        "buyer": comprador,  
        "price": price
    }

    save_data_to_file(movements_file, movement)

    print("\nMovimentação registrada com sucesso!")
    sleep(1.5)
