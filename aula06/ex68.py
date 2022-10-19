matriz = [ [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]  ]

for i in range(0, 2, 1):
    for j in range(0, 3, 1):
        matriz[i][j] = int(input('Digite um número: '))

const = int(input("Digite uma constante multiplicativa: "))

for i in range(0, 2, 1):
    for j in range(0, 3, 1):
        matriz[i][j] = matriz[i][j] * const

for i in range(0, 2, 1):
    print(matriz[i])