# 41. Calcular e exibir a soma dos “N” primeiros valores da seqüência abaixo. O valor “N” será digitado, deverá ser positivo, mas menor que cem. Caso o valor não satisfaça a restrição, enviar mensagem de erro e solicitar o valor novamente. A seqüência: 2, 5, 10, 17, 26, ....

a = 1
r = 2

n = int(input('Digite a quantidade de valores a ser exibido: '))

while(n < 0 or n > 100):
    n = int(input('Quantidade inválida. Digite outro valor: '))

i = 1

while(i <= n):
    print(r)
    a += 2
    r += a

    i += 1