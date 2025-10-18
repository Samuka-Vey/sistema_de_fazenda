import os

from time import sleep


def register_inputs():

    file_path = os.path.join("farm", "data", "inputs.json")

    print("Cadastramento de Insumos.")
    inputs_data = {
        'id': input("Digite o ID do insumo: "),

        'name': str(input("Digite o nome do insumo: ")),

        'quantity': float(input("Digite a quantidade disponivel no estoque "
                                " Pode ser representada em kg, litros,pacotes, etc.: ")),

        'unit': str(input("Digite unidade de medida associada à quantidade: ")),

        'category': str(input('Digite Classificação do insumo '
                              'ex: "feed" , "seed" , "fertilizer" "medicine".'))

    }

    save_data_to_file = (file_path, inputs_data)

    sleep(1, 5)

    print("Insumo cadastrado com sucesso!")
