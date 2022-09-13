# 47. Calcular o fatorial de um valor que será digitado. Este valor não poderá ser negativo. Enviar mensagem de erro e solicitar o valor novamente, se necessário. Perguntar se o usuário deseja ou não fazer um novo cálculo, consistir a resposta em “S” ou “N”.
# N! = N x N-1 x N-2 x N-3 x ....... x (N - (N-1))
# Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

opcao = 'S'

while(opcao == 'S'):
    x = int(input('Digite um valor qualquer: '))

    while(x < 0):
        print('Números negativos não são aceitos!')
        x = int(input('Digite outro valor: '))

    # LÓGICA
    resultado = 1
    i = 1

    while i <= x:
        resultado *= i
        i += 1

    print(f"Fatorial de {x} = {resultado}")

    opcao = str(input("Deseja executar o programa novamente(S/N)? ")).upper()

    while (opcao != 'S' and opcao != 'N'):
        opcao = str(input("Deseja executar o programa novamente(S/N)? ")).upper()
