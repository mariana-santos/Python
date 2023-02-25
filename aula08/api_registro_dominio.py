from datetime import datetime
from urllib import response
import pip._vendor.requests 

dominio = input('Digite o domínio que deseja pesquisar se está disponível: ')

url = f"https://brasilapi.com.br/api/registrobr/v1/{dominio}"
response = pip._vendor.requests.get(url)

while (response.status_code != 200):
    dominio = input('Domínio inválido. Por favor pesquise outro: ')
    url = f"https://brasilapi.com.br/api/registrobr/v1/{dominio}"
    response = pip._vendor.request.get(url)

dados = response.json()

print(f"Domínio: {dados['fqdn']}")

if(dados['status'] == 'REGISTERED'):
    print(f"Disponível: não")

    data_str = dados['expires-at'][0:18]
    data = datetime.strptime(data_str, '%Y-%m-%dT%H:%M:%S')
    data = data.strftime("%d/%m/%Y")

    print(f"Expira em: {data}")

else:
    print(f"Disponível: sim")