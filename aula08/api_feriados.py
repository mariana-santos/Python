from datetime import datetime
from urllib import response
import pip._vendor.requests 

data = input('Digite a data que deseja saber se há feriado no formato (dd/mm): ')
data = data + '/2023'
data = datetime.strptime(data, '%d/%m/%Y')
data = data.strftime("%d/%m/%Y")

url = f"https://brasilapi.com.br/api/feriados/v1/2023"
response = pip._vendor.requests.get(url)

dados = response.json()

feriados = []

ehferiado = False

for feriado in dados:
    data_feriado = datetime.strptime(feriado['date'], '%Y-%m-%d')
    data_feriado = data_feriado.strftime("%d/%m/%Y")

    if(data_feriado == data):
        print(f'{data} é feriado de {feriado["name"]}')
        ehferiado = True

    elif(str(data_feriado)[3:6] == str(data)[3:6]):
        feriados.append({"data": data_feriado, "descricao": feriado['name']})

if len(feriados) > 0:
    print(f'Existe(m) outros {len(feriados)} feriado(s) nesse mês.')

    for feriado in feriados:
        print(f'{feriado["data"]} é feriado de {feriado["descricao"]}')

elif ehferiado == False:
    print(f'{data} não é feriado e não existem outros feriados neste mês')