from utils.terminal import show_dashboard_header, show_options_module
from utils.terminal import press_enter_to_continue
from utils.message import WELCOME_DISPLAY_INPUTS

from inputs.manage_input import register_input, list_inputs, update_input, delete_input, read_inputs
from inputs.stock_control import control_stock

def show_choice_inputs():
    
    show_dashboard_header(WELCOME_DISPLAY_INPUTS, 98)
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
            register_input()
            press_enter_to_continue()
        case "2":
            list_inputs()
            press_enter_to_continue()
        case "3":
            update_input()
            press_enter_to_continue()
        case "4":
            delete_input()
            press_enter_to_continue()
        case "5":
            read_inputs()
            press_enter_to_continue()
        case "6":
            control_stock()
            press_enter_to_continue()
        case "0":
            return
        case _:
            print("Opção inválida!")
            press_enter_to_continue()
