# 36. Entrar via teclado com um valor (X) qualquer. Travar a digitação, no sentido de aceitar somente valores positivos. Solicitar o intervalo que o programa que deverá calcular a tabuada do valor digitado, sendo que o segundo valor (B), deverá ser maior que o primeiro (A), caso contrário, digitar novamente somente o segundo. Após a validação dos dados, exibir a tabuada do valor digitado, no intervalo decrescente, ou seja, a tabuada de X no intervalo de B para A.

x = int(input('Digite um valor qualquer: '))

while(x < 0):
    print('Números negativos não são aceitos!')
    x = int(input('Digite outro valor: '))

a = int(input('Digite o começo do intervalo da tabuada: '))
b = int(input('Digite o fim do intervalo da tabuada: '))

while (b < a):
    print(f'O intervalo não pode ser [{a}, {b}]. Digite outro intervalo')
    b = int(input('Digite o fim do intervalo da tabuada: '))

# FOR
print(f'Tabuada de {x} com FOR')
for i in range(b, a-1, -1):
    print(f'{x} x {i} = {x * i}')