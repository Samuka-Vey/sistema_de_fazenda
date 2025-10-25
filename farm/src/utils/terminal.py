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
    
def show_dashboard_header(title):
    clear_terminal()
    bars_line("=")
    print(f"{title:^70}")
    bars_line("=")
    
def show_options_module(options):
    for key, value in options.items():
        print(f"[{key}] {value}")
    bars_line("-")
