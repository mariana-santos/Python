# 27. Faça um algoritmo que leia uma variável e some 5 caso seja par ou some 8 caso seja ímpar, imprimir o resultado desta operação.

valor = int(input('Digite um número qualquer: '))

if(valor % 2 == 0):
    print(f'{valor} é par. {valor} + 5 = {valor + 5}')
else:
    print(f'{valor} é ímpar. {valor} + 8 = {valor + 8}') 