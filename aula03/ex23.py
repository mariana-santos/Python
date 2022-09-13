# 23. Faça um algoritmo que leia os valores A, B, C e imprima na tela se a soma de A + B é menor que C.

a = int(input('Digite o valor A: '))
b = int(input('Digite o valor B: '))
c = int(input('Digite o valor C: '))

if(a + b < c):
    print(f'{a + b} menor que {c}')
else:
    print(f'{a + b} maior que {c}')