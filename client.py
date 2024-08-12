import requests
import json

# Função para carregar dados de um arquivo .txt
def load_data_from_txt(file_path):
    with open(file_path, 'r') as file:
        data = file.read()
        # Convertendo os dados do arquivo de texto para um formato JSON
        json_data = json.loads(data)
    return json_data

# Caminho para o arquivo .txt que contém os dados
file_path = 'dados_jogo.txt'

# Carregando os dados do arquivo
data = load_data_from_txt(file_path)

# Converta os dados para JSON (se necessário)
json_data = json.dumps(data)

# Endereço IPv6 do servidor (substitua pelo endereço real do servidor)
server_address = 'http://[::1]:5000/analyze'

# Enviar para o servidor
response = requests.post(server_address, data=json_data, headers={'Content-Type': 'application/json'})

# Imprimir a resposta do servidor
print(response.json())
