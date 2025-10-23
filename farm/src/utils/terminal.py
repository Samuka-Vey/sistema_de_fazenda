import os


def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
def bars_line(type_line, length=70):
    match type_line:
        case "-":
            print("-" * length)
        case "=":
            print("=" * length)
        case "*":
            print("*" * length)
def press_enter_to_continue():
    input("\n✅ Pressione (ENTER) para continuar...")