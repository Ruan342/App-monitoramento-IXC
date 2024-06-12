#SALVAMENTO DO ARQUIVO DE RELATORIO

import json
import form_datas
import os


def save_data_to_file(data):
    data_atual_para_arquivo = form_datas.datetime.datetime.now().strftime('%Y%m%d')
    filename = f'login_connection_data_{data_atual_para_arquivo}.json'
    filepath = os.path.join('C:', filename)  #ALTERE O CAMINHO PARA O DESTINO ONDE SERÃO ARMAZENADOS OS RELATORIOS 

    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)
    
    print(f'Dados salvos em: {filepath}')