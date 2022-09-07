# 38. Exibir a soma dos números inteiros positivos do intervalo de um a cem.

i = 1
soma = 0

while(i <= 100):
    soma += i
    i = i + 1

print(f'Soma dos 100 primeiros números com WHILE: {soma}')

soma = 0

for i in range(1, 101, 1):
    soma += i

print(f'Soma dos 100 primeiros números com FOR: {soma}')