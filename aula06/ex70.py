matriz = []

linhas = int(input('Quantas linhas terá a matriz? '))

while(linhas > 10):
    linhas = int(input('Quantidade de linhas inválida. Digite novamente quantas linhas terá a matriz: '))

colunas = int(input('Quantas colunas terá a matriz? '))

while(colunas > 10):
    colunas = int(input('Quantidade de colunas inválida. Digite novamente quantas colunas terá a matriz: '))

for i in range (0, linhas, 1):
    matriz.append([])

for i in range (0, linhas, 1):
    for j in range (0, colunas, 1):
        n = int(input('Digite um número: '))
        matriz[i].append(n)

opcao = 'S'

while(opcao == 'S'):

    for i in range (0, linhas, 1):
        print(matriz[i])
    
    consulta = int(input('Digite o valor que deseja consultar: '))

    qtdEncontrada = 0

    for i in range (0, linhas, 1):
        for j in range (0, colunas, 1):
            if(matriz[i][j] == consulta):
                print(f'Valor encontrado na linha {i + 1}, coluna {j + 1}')
                qtdEncontrada += 1

    if(qtdEncontrada == 0): print('Nenhum valor encontrado')

    opcao = str(input('Deseja consultar outro valor? (S/N) ')).upper()