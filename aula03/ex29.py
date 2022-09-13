# 29. Escreva um algoritmo que leia três valores inteiros e diferentes e mostre-os em ordem dedecrescente.

a = int(input('Digite o valor A: '))
b = int(input('Digite o valor B: '))
c = int(input('Digite o valor C: '))

if (a >= b and b >= c):
      print(f"A ordem decrescente: {a}, {b}, {c}")
elif (a >= c and c >= b):
    print(f"A ordem decrescente: {a}, {c}, {b}")
elif (b >= a and a >= c):
    print(f"A ordem decrescente: {b}, {a}, {c}")
elif (b >= c and c >= a) :
    print(f"A ordem decrescente: {b}, {c}, {a}")
elif (c >= a and a >= b):
    print(f"A ordem decrescente: {c}, {a}, {b}")
else:
    print(f"A ordem decrescente: {c}, {b}, {a}")