n1 = float(input('digite o primeiro número: '))
n2 = float(input('digite o segundo número: '))

# Exercício 3 -> Entrar com dois valores quaisquer. Exibir o maior deles, se existir, caso contrário, enviar mensagem avisando que os números são idênticos.
if n1 > n2:
    print(f"{n1} maior")
elif n2 > n1 :
    print(f"{n2} maior")
else:
    print("Números iguais")