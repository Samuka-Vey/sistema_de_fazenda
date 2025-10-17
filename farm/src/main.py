# Marcos Samuel Cornelio Barros [Matricula: 2025027554]

from utils.register import register
from utils.messages import WELCOME

def main():
    print(WELCOME)


    while True:
        print("\nMenu Principal:")
        print("1. Cadastrar animal")
        print("4. Sair")

        choice = int(input("Escolha uma opção: "))
        register(choice)



if __name__ == "__main__":
    main()