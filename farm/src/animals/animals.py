from utils.terminal import show_dashboard_header, show_options_module, press_enter_to_continue
from utils.message import WELCOME_DISPLAY_ANIMAL
from animals.manage_animals import register_animal, list_animals, update_animal, read_animal, delete_animal

def show_choice_animals():
    show_dashboard_header(WELCOME_DISPLAY_ANIMAL, 98)

    show_options_module({
        "1": "Cadastrar Animal",
        "2": "Listar Animais",
        "3": "Atualizar Animal",
        "4": "Pesquisar Animal",
        "5": "Deletar Animal",
        "0": "Voltar"
    })
    
    choice = input("Escolha uma opção: ").strip()
    
    match choice:
        case "1":
            register_animal()
            press_enter_to_continue()
        case "2":
            list_animals()
            press_enter_to_continue()
        case "3":
            update_animal()
            press_enter_to_continue()
        case "4":
            read_animal()
            press_enter_to_continue()
        case "5":
            delete_animal()
            press_enter_to_continue()
        case "0":
            return
        case _:
            print("Opção inválida!")
            press_enter_to_continue()