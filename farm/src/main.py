from time import sleep
from utils.logs import WELCOME

def show_menu():
    print("="*70)

    print(WELCOME)

    print("="*70)
    print("\n[1] Cadastrar Animal")
    print("[2] Cadastrar Plantação")
    print("[3] Cadastrar Insumo")
    print("[4] Listar Animais")
    print("[5] Listar Plantações")
    print("[6] Listar Insumos")
    print("[7] Registrar Movimentação")
    print("[8] Gerar Relatórios")
    print("[9] Pesquisar Registro")
    print("[0] Sair")
    print("="*70)

def main():
    while True:
        show_menu()
        
        try:
            from animals import register_animal
            option = input("\nEscolha uma opção: ").strip()
            
            if option == "1":
                register_animal()

            elif option == "4":
                from animals import search_animal
                search_animal()
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