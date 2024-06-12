#EXECUÇÃO DA REQUISIÇÃO

import requests
import conf
import form_datas
import salvar_arquivo

data_atual_formatada, data_anterior_8h_formatada = form_datas.obter_datas_formatadas()

data = {
    "qtype": "radacct.radacctid",
    'tipo_conexao': '',
    'ultima_atualizacao': 'CURRENT_TIMESTAMP',
    'ultima_conexao_inicial': '',
    'ultima_conexao_final': '',
    'motivo_desconexao': '',
    'count_desconexao': '',
    "query": "1",
    "oper": ">=",
    "page": "1",
    "rp": "1000",
    "sortname": "radacct.radacctid",
    "sortorder": "desc",
    "grid_param": '[{"TB":"radacct.acctstarttime", "OP" : ">=", "P" : "{data_anterior_8h_formatada}"},{"TB":"radacct.acctstarttime", "OP" : "<=", "P" : "{data_atual_formatada}"}]'
} 

response = requests.get(conf.url, headers=conf.headers, data=salvar_arquivo.json.dumps(data))

if response.status_code == 200:
    print("Requisição bem-sucedida!")
    response_data = response.json()
    salvar_arquivo.save_data_to_file(response_data)
else:
    print(f"Falha. Status code: {response.status_code}")
    print("Resposta:", response.text)
