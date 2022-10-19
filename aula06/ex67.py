matriz = [ [0, 0, 0], [0, 0, 0]  ]

for i in range(0, 2, 1):
    for j in range(0, 3, 1):
        matriz[i][j] = str(input('Digite um nome: '))

for i in range(0, 2, 1):
    print(matriz[i])