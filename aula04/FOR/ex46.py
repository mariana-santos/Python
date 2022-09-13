# 46. Entrar via teclado com “N” valores quaisquer. O valor “N” (que representa a quantidade de números) será digitado, deverá ser positivo, mas menor que vinte. Caso a quantidade não satisfaça a restrição, enviar mensagem de erro e solicitar o valor novamente. Após a digitação dos “N” valores, exibir:
# a) O maior valor;
# b) O menor valor;
# c) A soma dos valores;
# d) A média aritmética dos valores;
# e) A porcentagem de valores que são positivos;
# f) A porcentagem de valores negativos;

# Após exibir os dados, perguntar ao usuário se deseja ou não uma nova execução do programa. Consistir a resposta no sentido de aceitar somente “S” ou “N” e encerrar o programa em função dessa resposta.

opcao = 'S'

while(opcao == 'S'):
    soma = 0
    maior = 0
    menor = 1000
    negativos = 0
    positivos = 0

    qtd = int(input('Digite a quantidade de valores a ser exibido: '))

    while(qtd < 0 or qtd > 20):
        qtd = int(input('Quantidade inválida. Digite outro valor: '))

    for i in range(0, qtd, 1):
        n = int(input(f"Digite o {i + 1}° número: "))
        soma += n

        if(n > maior):
            maior = n

        if(n < menor):
            menor = n

        if(n < 0):
            negativos += 1
        elif n > 0:
            positivos += 1

    print(f"a) O maior valor: {maior}")
    print(f"b) O menor valor: {menor}")
    print(f"c) A soma dos valores: {soma}")
    print(f"d) A média aritmética dos valores: {soma / qtd}")
    print(f"e) A porcentagem de valores que são positivos: {(positivos * 100) / qtd}%")
    print(f"f) A porcentagem de valores negativos: {(negativos * 100) / qtd}%")

    opcao = str(input("Deseja executar o programa novamente(S/N)? ")).upper()

    while (opcao != 'S' and opcao != 'N'):
        opcao = str(input("Deseja executar o programa novamente(S/N)? ")).upper()
