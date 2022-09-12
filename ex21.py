print('1 – Multiplicação')
print('2 – Adição')
print('3 – Divisão')
print('4 – Subtração')
print('5 – Fim de processo (sair do programa)')

opcao = input('Bem-vindo! Selecione selecione alguma das opções acima para calcular: ')

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

if(opcao == 1):
    print(f"Resultado: {n1 * n2}")
elif (opcao == 2):
    print(f"Resultado: {n1 + n2}")
elif (opcao == 3):
    if(n1 == 0):
        print('Divisor inválido')
    else:
        print(f"Resultado: {n1 / n2}")
elif(opcao == 4):
    print(f"Resultado: {n1 - n2}")
elif(opcao == 5):
    print('Fim do programa.')
else:
    print('Opção inválida.')
