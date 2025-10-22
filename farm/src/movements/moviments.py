
from utils.terminal import press_enter_to_continue, clear_terminal
def menu_movements():
    print("\n=== Menu de Movimentações ===")
    print("[1] Registrar Movimentação de Animal")
    print("[2] Registrar Movimentação de Insumos")
    print("[3] Registrar Movimentação de Plantas")
    print("[0] Voltar ao Menu Principal")

    option = input("\nEscolha uma opção: ").strip()

    if option == "1":
        from movements.movements_animal import register_animal_movement 
        register_animal_movement()
        press_enter_to_continue()
    elif option == "2":
        from movements.movements_input import register_inputs_movements
        register_inputs_movements()
        press_enter_to_continue()
        
    elif option == "3":
        from movements.movements_plants import register_plants_movement
        register_plants_movement()
        press_enter_to_continue()
    elif option == "0":
        return
    else:
        print("\n Opção inválida!")