# 37. Exibir a tabuada dos valores de um a vinte, no intervalo de um a dez. Entre as tabuadas, solicitar que o usuário pressione uma tecla.

# FOR
for numero in range (1, 21, 1):
    print(f'Tabuada de {numero} com FOR')
    for i in range (1, 11, 1):
        print(f'{i} x {numero} = {numero * i}')

    if(numero != 20):
        input('Aperte qualquer tecla para continuar: ')