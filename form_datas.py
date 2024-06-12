#FORMATAÇÃO DE DATAS PARA COMPATIBILIDADE COM A CONSULTA DE DADOS DA API

import datetime
from datetime import timedelta

def obter_datas_formatadas():

    data_atual = datetime.datetime.now()
    data_anterior = data_atual - timedelta(days=1)
    data_anterior_8h = data_anterior.replace(hour=8, minute=0, second=0, microsecond=0)
    data_atual_formatada = data_atual.strftime('%Y-%m-%d %H:%M:%S')
    data_anterior_8h_formatada = data_anterior_8h.strftime('%Y-%m-%d %H:%M:%S')

    return data_atual_formatada, data_anterior_8h_formatada
