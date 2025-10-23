'''

Marcos Samuel Cornelio Barros [Matricula: 2025027554]
João Pedro Aguiar Teixeira [Matricula: 2025012506]
David de Carvalho Santos [Matrícula: 2025012373]
Bruno Vinicius dos Reis Souza [Matricula:2025034595]

'''

from time import sleep
from utils.message import WELCOME
from utils.terminal import bars_line, clear_terminal
def show_menu():
    clear_terminal()
    bars_line("*", 66)
    print(WELCOME)

    bars_line("-", 66)
    print("[1] Gerenciar Animais")
    print("[2] Gerenciar Plantações")
    print("[3] Gerenciar Insumos")
    print("[4] Registrar Movimentação")
    print("[5] Gerar Relatórios")
    print("[6] Pesquisar Registro")
    print("[0] Sair")
    bars_line("-", 66)

def main():
    while True:
        show_menu()
        
        try:
            option = input("\nEscolha uma opção: ").strip()
            
            if option == "1":
                from animals.animals import show_choice_animals
                show_choice_animals()
            elif option == "2":
                from plants.plants import show_choice_plants
                show_choice_plants()
            elif option == "3":
                from inputs.inputs import show_choice_inputs
                show_choice_inputs()
            elif option == "4":
                from movements.moviments import menu_movements
                menu_movements()
            elif option == "5":
                from register import generate_inputs_report
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