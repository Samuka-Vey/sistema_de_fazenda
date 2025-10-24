def show_choice_animals():
    from utils.terminal import show_dashboard_header, show_options_module
    from utils.terminal import press_enter_to_continue
    
    show_dashboard_header("Gerenciamento de Animais")
   
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
            from  animals.manage_animals import register_animal
            register_animal()
            press_enter_to_continue()
        case "2":
            from animals.manage_animals import list_animals
            list_animals()
            press_enter_to_continue()
        case "3":
            from animals.manage_animals import update_animal
            update_animal()
            press_enter_to_continue()
        case "4":
            from animals.manage_animals import read_animal
            read_animal()
            press_enter_to_continue()
        case "5":
            from animals.manage_animals import delete_animal
            delete_animal()
            press_enter_to_continue()
        case "0":
            return
        case _:
            print("Opção inválida!")
            press_enter_to_continue()