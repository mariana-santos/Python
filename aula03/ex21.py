# 21. Entrar via teclado com dois valores quaisquer. Após a digitação, exibir um seletor de opções (“menu”) com as seguintes opções: (Fazer esse exercício utilizando If..Else e/ou Case)

# 1 – Multiplicação
# 2 – Adição
# 3 – Divisão
# 4 – Subtração
# 5 – Fim de processo (sair do programa)

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
