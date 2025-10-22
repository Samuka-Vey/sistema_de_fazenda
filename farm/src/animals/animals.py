def show_choice_animals():
    from utils.terminal import clear_terminal, bars_line
    from utils.terminal import press_enter_to_continue
    clear_terminal()
    bars_line("-", 24)
    print("Gerenciamento de Animais")
    bars_line("-", 24)
    print("[1] Cadastrar Animal")
    print("[2] Listar Animais")
    print("[3] Atualizar Animal")
    print("[4] Pesquisar Animal")
    print("[5] Deletar Animal")
    print("[0] Voltar")
    bars_line("-", 20)
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