# 37. Exibir a tabuada dos valores de um a vinte, no intervalo de um a dez. Entre as tabuadas, solicitar que o usuário pressione uma tecla.

# WHILE
i = 1
numero = 1
while(numero <= 20 ):  
    print(f'Tabuada de {numero} com WHILE')
    i = 1
    while(i <= 10):
        print(f'{i} x {numero} = {numero * i}')
        i += 1
    if(numero != 20):
        input('Aperte qualquer tecla para continuar: ')
    
    numero += 1