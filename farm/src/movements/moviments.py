
from utils.terminal import press_enter_to_continue
from utils.terminal import show_dashboard_header, show_options_module
from utils.message import WELCOME_DISPLAY_MOVEMENTS
from .movements_animal import register_animal_movement
from .movements_input import register_inputs_movements
from .movements_plants import register_plants_movement

def menu_movements():
    show_dashboard_header(WELCOME_DISPLAY_MOVEMENTS, 85)
    show_options_module({
        "1": "Registrar Movimentação de Animal",
        "2": "Registrar Movimentação de Insumos",
        "3": "Registrar Movimentação de Plantas",
        "0": "Voltar"
    })
   

    option = input("\nEscolha uma opção: ").strip()

    if option == "1":
        register_animal_movement()
        press_enter_to_continue()
    elif option == "2":
        register_inputs_movements()
        press_enter_to_continue()
        
    elif option == "3":
        register_plants_movement()
        press_enter_to_continue()
    elif option == "0":
        return
    else:
        print("\n Opção inválida!")