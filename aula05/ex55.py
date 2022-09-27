numeros = []

n = int(input('Quantos valores você deseja armazenar no array? '))

while(n < 0 or n > 20):
    n = int(input('Quantidade inválida. Digite novamente um novo tamanho de array: '))

for i in range (0, n, 1):
    valor = int(input(f'Digite a {i+1}° posição do array: '))
    numeros.append(valor)

opcao = 'S'

while(opcao == 'S'):
    search = int(input('Que número deseja encontrar no array? '))

    resultado = -1

    for i in range (0, n, 1):
        if(search == numeros[i]):
            resultado = i

    if(resultado != -1):
        print(f'Valor {search} encontrado na posição {resultado}')
    else:
        print('Valor não encontrado')

    opcao = str(input('Deseja fazer uma nova consulta? S/N ')).upper()