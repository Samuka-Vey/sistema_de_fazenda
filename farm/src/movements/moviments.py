from movements.movements_animal import register_animal_movement
from movements.movements_input import register_inputs_movements
def menu_movements():
    print("\n=== Menu de Movimentações ===")
    print("[1] Registrar Movimentação de Animal")
    print("[2] Registrar Movimentação de Insumos")
    print("[0] Voltar ao Menu Principal")

    option = input("\nEscolha uma opção: ").strip()

    if option == "1":
        register_animal_movement()
    elif option == "2":
        register_inputs_movements()
    elif option == "0":
        return
    else:
        print("\n Opção inválida!")