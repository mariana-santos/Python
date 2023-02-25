import pip._vendor.requests as requests

print('---Conversão de Moedas---')
reais = float(input("Qual o valor em R$ que deseja converter? "))

moedas = {1: 'USD', 2: 'EUR', 3: 'BTC'}

while(reais <= 0):
    reais = float(input("Valor inválido. Digite novamente o valor em R$ que deseja converter: "))

opcao = int(input('Deseja converter para: \n 1. Dólar \n 2. Euro \n 3. Bitcoin '))

while(opcao <= 0 or opcao > 3):
    opcao = int(input('Opção inválida. Deseja converter para: \n 1. Dólar \n 2. Euro \n 3. Bitcoin '))

url = f"https://economia.awesomeapi.com.br/json/last/{moedas[opcao]}-BRL"

response = requests.get(url)
dados = response.json();

opcao_str = f'{moedas[opcao]}BRL'

result = reais * float(dados[opcao_str]['ask'])

if response.status_code == 200:

    dados = dados[opcao_str]

    print(dados['name'])
    print(f"{dados['codein']}: {reais:.2f}")
    print(f"{dados['code']}: {result:.2f}")
else: 
    print ('Ocorreu um erro. Por favor, tente novamente mais tarde.')