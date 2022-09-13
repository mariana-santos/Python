# Exercício 22 -> Exibir o seguinte seletor de opções e em função de uma escolha, solicitar os dados necessários para o cálculo da respectiva área. Enviar mensagem de erro se o usuário escolher uma opção inexistente.

print('1 – Triângulo')
print('2 – Quadrado')
print('3 – Retângulo')
print('4 – Círculo')
print('5 – Fim de processo (sair do programa)')

opcao = int(input('Bem-vindo! Selecione selecione alguma das opções acima para calcular a área: '))

if(opcao == 1 or opcao == 2 or opcao == 3 or opcao == 4 or opcao == 5):
    if(opcao == 1):
        base = float(input('Digite a base do triângulo: '))
        alt = float(input('Digite a altura do triângulo: '))
        print(f'Área do triângulo equivale a {(base * alt) / 2}')
    elif (opcao == 2):
        lado = float(input('Digite o lado do quadrado: '))
        print(f'Área do quadrado equivale a {lado * lado}')
    elif (opcao == 3):
        base = float(input('Digite a base do retângulo: '))
        alt = float(input('Digite a altura do retângulo: '))
        print(f'Área do triângulo equivale a {base * alt}')
    elif(opcao == 4):
        r = float(input('Digite o raio do círculo: '))
        print(f'Área do círculo equivale a {3.14 * (r * r)}')
    else:
        print('Fim do programa.')
else:
    print('Opção inválida.')