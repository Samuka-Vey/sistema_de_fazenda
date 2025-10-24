def show_choice_plants():
    from utils.terminal import show_dashboard_header, show_options_module
    from utils.terminal import press_enter_to_continue
    show_dashboard_header("Gerenciamento de Plantações")
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
            from plants.manage_plants import register_plants
            register_plants()
            press_enter_to_continue()
        case "2":
            from plants.manage_plants import list_plants
            list_plants()
            press_enter_to_continue()
        case "3":
            from plants.manage_plants import update_plants
            update_plants()
            press_enter_to_continue()
        case "4":
            from plants.manage_plants import read_plants
            read_plants()
            press_enter_to_continue()
        case "5":
            from plants.manage_plants import delete_plants
            delete_plants()
            press_enter_to_continue()
        case "0":
            return
        case _:
            print("Opção inválida!")
            press_enter_to_continue()