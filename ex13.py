# Exercício 06 -> Entrar via teclado com três valores distintos. Exibir o maior deles.

maior = float(input("Insira o primeiro número: "))
n2 = float(input("Insira o segundo número: "))
n3 = float(input("Insira o terceiro número: "))

if n2 > maior and n2 > n3:
    maior = n2
elif n3 > maior and n3 > n2:
    maior = n3

print(f"Maior número: {maior}")