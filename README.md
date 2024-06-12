# App-monitoramento-IXC
Relatório de desconexões de clientes para provedora de internet

# Projeto de Monitoramento de desconexões de clientes IXCsoft

Este projeto foi desenvolvido utilizando a API de desenvolvimento da IXCsoft, com o objetivo de monitorar a conexão e quedas dos clientes de uma provedora de internet. O script realiza requisições para a API e salva os dados de login e desconexões em arquivos JSON, permitindo uma análise detalhada da performance da rede.

## Descrição do Projeto

Este projeto faz uso da API da IXCsoft para obter informações sobre a queda de conexão dos clientes e e possiveis problemas constantes de quedas. Ele foi desenvolvido em Python e inclui funcionalidades para:

- Obter dados de login e desconexão dos clientes.
- Otimizar o tempo de resposta de provedoras no caso de quedas de sinal.
- Salvar esses dados em arquivos JSON para posterior análise.
- Realizar autenticação utilizando tokens de API.

## Bibliotecas Utilizadas

- **requests**: Para fazer as requisições HTTP à API da IXCsoft.
- **base64**: Para codificar o token de autenticação.
- **json**: Para manipular os dados retornados pela API.
- **datetime**: Para manipulação de datas e horários.
- **python-dotenv**: Para gerenciar variáveis de ambiente de forma segura.

## Dificuldades Encontradas

Durante o desenvolvimento do projeto, enfrentamos algumas dificuldades, tais como:

- Manipulação de datas e horários para garantir que as requisições estejam sempre atualizadas e compativeis com a formatação da API.
- Gerenciamento seguro de credenciais e tokens da API.
- Tratamento de respostas da API e manipulação/conversão de dados para JSON.

## Estrutura do Projeto

```plaintext
IXC-Monitoring/
├── .env
├── README.md
├── app_get.py
├── conf.py
├── form_datas.py
└── salvar_arquivo.py

