# 43. Calcular e exibir a soma dos “N” primeiros valores da seqüência abaixo. O valor “N” será digitado, deverá ser positivo, mas menor que cinqüenta. Caso o valor não satisfaça a restrição, enviar mensagem de erro e solicitar o valor novamente. A seqüência: 2, 5/8, 10/27

a = 1
divisor = 2

dividendo = 1

n = int(input('Digite a quantidade de valores a ser exibido: '))

while(n < 0 or n > 50):
    n = int(input('Quantidade inválida. Digite outro valor: '))

i = 1

while (i <= n):

    # dividendo elevado a 3
    dividendo = i ** 3

    r = divisor / dividendo

    print(f"{divisor} ÷ {dividendo} = {r:.2f}")

    a += 2;
    divisor += a;

    i+= 1