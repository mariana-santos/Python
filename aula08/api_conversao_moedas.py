import requests

print('---Conversão de Moedas---')
reais = float(input("Qual o valor em R$ que deseja converter? "))

while(reais <= 0):
    reais = float(input("Valor inválido. Digite novamente o valor em R$ que deseja converter: "))

opcao = int(input('Deseja converter para: \n 1. Dólar \n 2. Euro \n 3. Bitcoin '))

while(opcao <= 0 or opcao > 3):
    opcao = int(input('Opção inválida. Deseja converter para: \n 1. Dólar \n 2. Euro \n 3. Bitcoin '))

if(opcao == 1):
    opcao_str = 'USD-BRL'
elif (opcao == 2):
    opcao_str = 'EUR-BRL'
else:
    opcao_str = 'BTC-BRL'

url = f"https://economia.awesomeapi.com.br/json/last/{opcao_str}"

response = requests.get(url)
dados = response.json();

opcao_str = opcao_str.replace('-', '')

result = reais * float(dados[opcao_str]['ask'])

if response.status_code == 200:

    dados = dados[opcao_str]

    print(dados['name'])
    print(f"{dados['codein']}: {reais:.2f}")
    print(f"{dados['code']}: {result:.2f}")
else: 
    print ('Ocorreu um erro. Por favor, tente novamente mais tarde.')