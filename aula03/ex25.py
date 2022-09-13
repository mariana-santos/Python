# 25. Faça um algoritmo para receber um número qualquer e informar na tela se é par ou ímpar. Utilize o operador %

valor = int(input('Digite um número qualquer: '))

if(valor % 2 == 0):
    print(f'{valor} é par')
else:
    print(f'{valor} é ímpar')