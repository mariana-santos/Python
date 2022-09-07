# 35. Entrar via teclado com um valor qualquer. Travar a digitação, no sentido de aceitar somente valores positivos. Após a digitação, exibir a tabuada do valor solicitado, no intervalo de um a dez.

valor = int(input('Digite um valor qualquer: '))

while(valor < 0):
    print('Números negativos não são aceitos!')
    valor = int(input('Digite outro valor: '))

# While
i = 1
print(f'Tabuada de {valor} com WHILE')
while(i <= 10):
    print(f'{valor} x {i} = {valor * i}')
    i  = i + 1

# FOR
print(f'Tabuada de {valor} com FOR')
for i in range(1, 11, 1):
    print(f'{valor} x {i} = {valor * i}')