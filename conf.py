#AUTENTICAÇÃO DA API

import base64
import os
from dotenv import load_dotenv

load_dotenv()

host = os.getenv('HOST')
url =  os.getenv('URL').format(host)
token = os.getenv('token').encode('utf-8')


headers = {
    'ixcsoft': 'listar',
    'Content-Type': 'application/json',
    'Authorization': 'Basic {}'.format(base64.b64encode(token).decode('utf-8')),
}
