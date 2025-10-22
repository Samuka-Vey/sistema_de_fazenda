def show_choice_plants():
    from utils.terminal import clear_terminal, bars_line
    from utils.terminal import press_enter_to_continue
    clear_terminal()
    bars_line("-", 26)
    print("Gerenciamento de Plantações")
    bars_line("-", 26)
    print("[1] Cadastrar Plantações")
    print("[2] Listar Plantações")
    print("[3] Atualizar Plantações")
    print("[4] Pesquisar Plantações")
    print("[5] Deletar Plantações")
    print("[0] Voltar")
    bars_line("-", 26)
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