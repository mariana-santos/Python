numeros = []
maior = 0

for i in range(0, 10, 1):
    num = int(input(f"Digite o {i+1}° valor: "))
    numeros.append(num)

for i in range(0, 10, 1):
    if(numeros[i] > maior):
        maior = numeros[i]

print(f"Maior número do array: {maior}")