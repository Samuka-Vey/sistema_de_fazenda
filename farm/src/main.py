'''
Marcos Samuel Cornelio Barros [Matricula: 2025027554]
João Pedro Aguiar Teixeira [Matricula: 2025012506]
David de Carvalho Santos [Matrícula: 2025012373]
Bruno Vinicius dos Reis Souza [Matricula:2025034595]

'''

from time import sleep
from utils.message import WELCOME
from utils.terminal import bars_line, clear_terminal, show_options_module
from animals.animals import show_choice_animals
from plants.plants import show_choice_plants
from inputs.inputs import show_choice_inputs
from movements.moviments import menu_movements
from reports import generate_inputs_report

def show_menu():
    clear_terminal()
    bars_line("*", 66)
    print(WELCOME)
    show_options_module({
        "1": "Gerencia Animais",
        "2": "Gerencia Plantações",
        "3": "Gerencia Insumos",
        "4": "Gerencia Movimentações",
        "5": "Gerar Relatório de Insumos",
        "0": "Sair"
    })
    bars_line("*", 66)

def main():
    while True:
        show_menu()
        
        try:
            option = input("\nEscolha uma opção: ").strip()
            
            if option == "1":
                show_choice_animals()
            elif option == "2":
                show_choice_plants()
            elif option == "3":
                show_choice_inputs()
            elif option == "4":
                menu_movements()
            elif option == "5":
                generate_inputs_report()
            elif option == "0":
                print("\nEncerrando sistema...")
                sleep(1)
                break
            else:
                print("\n Opção inválida!")
                sleep(1)
                
        except KeyboardInterrupt:
            print("\nSistema interrompido pelo usuário.")
            break
        except Exception as e:
            print(f"\n Erro: {e}")
            sleep(1.5)

if __name__ == "__main__":
    main()