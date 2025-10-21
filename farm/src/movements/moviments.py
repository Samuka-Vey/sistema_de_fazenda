from movements.movements_animal import register_animal_movement


def menu_movements():
    print("\n=== Menu de Movimentações ===")
    print("[1] Registrar Movimentação de Animal")
    
    print("[0] Voltar ao Menu Principal")

    option = input("\nEscolha uma opção: ").strip()

    if option == "1":
        register_animal_movement()
    elif option == "0":
        return
    else:
        print("\n Opção inválida!")