# Exercício 09 - Verificar se três valores quaisquer (A, B, C) que serão digitados formam ou não um triângulo retângulo. Lembre-se que o quadrado da hipotenusa é igual a soma dos quadrados dos catetos.

a = float(input("Insira o valor do lado A"))
b = float(input("Insira o valor do lado B"))
c = float(input("Insira o valor do lado C"))

if (a*a > b*b + c*c) and (b*b > a*a + c*c) and (c*c > b*b + a*a):
    print("É um triângulo retângulo")
else:
    print("Não é um triângulo retângulo")