# 42. Calcular e exibir a soma dos “N” primeiros valores da seqüência abaixo. O valor “N” será digitado, deverá ser positivo, mas menor que cinqüenta. Caso o valor não satisfaça a restrição, enviar mensagem de erro e solicitar o valor novamente. A sequência 1/2 2/3 3/4 4/5

divisor = 1
dividendo = 2

n = int(input('Digite a quantidade de valores a ser exibido: '))

while(n < 0 or n > 50):
    n = int(input('Quantidade inválida. Digite outro valor: '))

for i in range(0, n, 1):
    r = divisor / dividendo
    print(f"{divisor} ÷ {dividendo} = {r:.2f}")
    divisor += 1
    dividendo += 1