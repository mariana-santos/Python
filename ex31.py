# 31. Criar uma rotina de entrada que aceite somente um valor positivo.

valor = int(input('Digite um valor qualquer: '))

# While
while(valor < 0):
    print('Números negativos não são aceitos!')
    valor = int(input('Digite outro valor: '))

print(f'{valor} positivo. :)')

# for i in range()