from datetime import datetime
from urllib import response
import pip._vendor.requests 

data = input('Digite a data que deseja saber se há feriado no formato (dd/mm): ')
data = data + '/2023'
data = datetime.strptime(data, '%d/%m/%Y')
data = data.strftime("%Y-%m-%d")

url = f"https://brasilapi.com.br/api/feriados/v1/2023"
response = pip._vendor.requests.get(url)

dados = response.json()

for feriado in dados:
    data_feriado = datetime.strptime(feriado['date'], '%Y-%m-%d')
    data_feriado = data_feriado.strftime("%Y-%m-%d")

    if(data_feriado == data):
        print(f'{data} é feriado de {feriado["name"]}')
    else:
        if(data_feriado[5:6] == data[5:6]):
            print(f'{data} não é feriado, mas {data_feriado} é {feriado["name"]}')



# print(f"Domínio: {dados['fqdn']}")

# if(dados['status'] == 'REGISTERED'):
#     print(f"Disponível: não")

#     data_str = dados['expires-at'][0:18]
#     data = datetime.strptime(data_str, '%Y-%m-%dT%H:%M:%S')
#     data = data.strftime("%d/%m/%Y")

#     print(f"Expira em: {data}")

# else:
#     print(f"Disponível: sim")