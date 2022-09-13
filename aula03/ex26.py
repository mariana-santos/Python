# 26. Encontrar o dobro de um número caso ele seja positivo e o seu triplo caso seja negativo, imprimindo o resultado.

valor = int(input('Digite um número qualquer: '))

if(valor < 0 ):
    print(f'Triplo de {valor} é {valor * 3}')
else:
    print(f'Dobro de {valor} é {valor * 2}')