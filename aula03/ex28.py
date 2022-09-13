# 28. Escreva um algoritmo que leia três valores inteiros e diferentes e mostre-os em ordem crescente.

a = int(input('Digite o valor A: '))
b = int(input('Digite o valor B: '))
c = int(input('Digite o valor C: '))

if (a <= b and b <= c):
      print(f"A ordem crescente: {a}, {b}, {c}")
elif (a <= c and c <= b):
    print(f"A ordem crescente: {a}, {c}, {b}")
elif (b <= a and a <= c):
    print(f"A ordem crescente: {b}, {a}, {c}")
elif (b <= c and c <= a) :
    print(f"A ordem crescente: {b}, {c}, {a}")
elif (c <= a and a <= b):
    print(f"A ordem crescente: {c}, {a}, {b}")
else:
    print(f"A ordem crescente: {c}, {b}, {a}")