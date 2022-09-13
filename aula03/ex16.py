# Exercício 16 - Verificar se três valores quaisquer (A, B, C) que serão digitados formam ou não um triângulo retângulo. Lembre-se que o quadrado da hipotenusa é igual a soma dos quadrados dos catetos.

a = float(input("Insira o valor do lado A: "))
b = float(input("Insira o valor do lado B: "))
c = float(input("Insira o valor do lado C: "))

if(a > b and a > c):
    h = a
    c1 = b
    c2 = c
elif (b > a and b > c):
    h = b
    c1 = c
    c2 = a
else:
    h = c
    c1 = b
    c2 = a


if (h * h == (c1* c1 + c2 * c2)):
    print("É um triângulo retângulo")
else:
    print("Não é um triângulo retângulo")