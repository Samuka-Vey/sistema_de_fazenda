def show_choice_inputs():
    from utils.terminal import show_dashboard_header, show_options_module
    from utils.terminal import press_enter_to_continue
    show_dashboard_header("Gerenciamento de Insumos")
    show_options_module({
        "1": "Cadastrar Insumo",
        "2": "Listar Insumos",
        "3": "Atualizar Insumo",
        "4": "Deletar Insumo",
        "5": "Pesquisar Insumo",
        "6": "Controlar Estoque",
        "0": "Voltar"
    })
   
    choice = input("Escolha uma opção: ").strip()
    
    match choice:
        case "1":
            from inputs.manage_input import register_input
            register_input()
            press_enter_to_continue()
        case "2":
            from inputs.manage_input import list_inputs
            list_inputs()
            press_enter_to_continue()
        case "3":
            from inputs.manage_input import update_input
            update_input()
            press_enter_to_continue()
        case "4":
            from inputs.manage_input import delete_input
            delete_input()
            press_enter_to_continue()
        case "5":
            from inputs.manage_input import read_input
            read_input()
            press_enter_to_continue()
        case "6":
            from inputs.stock_control import control_stock
            control_stock()
            press_enter_to_continue()
        case "0":
            return
        case _:
            print("Opção inválida!")
            press_enter_to_continue()
