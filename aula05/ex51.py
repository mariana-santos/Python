numeros = []

for i in range(0, 10, 1):
    num = int(input(f"Digite o {i+1}° valor: "))
    numeros.append(num)

for i in range(9, -1, -1):
    print(numeros[i])