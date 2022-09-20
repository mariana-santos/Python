numeros = []
maior = 0

for i in range(0, 20, 1):
    num = int(input(f"Digite o {i+1}° valor: "))
    numeros.append(num)

const = int(input('Por favor, digite a constante multiplicativa: '))

for i in range(0, 20, 1):
    numeros[i] = numeros[i] * const

print(f'\nNúmeros multiplicados por {const}')
for i in numeros:
    print(i)