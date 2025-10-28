from utils.terminal import show_dashboard_header, show_options_module, press_enter_to_continue
from utils.message import WELCOME_DISPLAY_PLANTATION
from plants.manage_plants import register_plants, list_plants, update_plants, read_plants, delete_plants
def show_choice_plants():
    
    show_dashboard_header(WELCOME_DISPLAY_PLANTATION, 110)
    show_options_module({
        "1": "Cadastrar Plantações",
        "2": "Listar Plantações",
        "3": "Atualizar Plantações",
        "4": "Pesquisar Plantações",
        "5": "Deletar Plantações",
        "0": "Voltar"
    })
    choice = input("Escolha uma opção: ").strip()
    
    match choice:
        case "1":
            register_plants()
            press_enter_to_continue()
        case "2":
            list_plants()
            press_enter_to_continue()
        case "3":
            update_plants()
            press_enter_to_continue()
        case "4":
            read_plants()
            press_enter_to_continue()
        case "5":
            delete_plants()
            press_enter_to_continue()
        case "0":
            return
        case _:
            print("Opção inválida!")
            press_enter_to_continue()