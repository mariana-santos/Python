# 32. Entrar com dois valores via teclado, onde o segundo deverá ser maior que o primeiro. Caso contrário solicitar novamente apenas o segundo valor.

a = int(input('Digite o valor A: '))
b = int(input('Digite o valor B: '))

# While
while(b <= a):
    print(f'Valor {b} menor ou igual ao valor {a}. Digite o segundo valor novamente')
    b = int(input('Digite outro valor: '))

print(f'valor {b} maior que o valor {a}. Fim')