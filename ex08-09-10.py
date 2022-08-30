# print("hello world")

# soma
# n1 = float(input('digite o primeiro número: '))
# n2 = float(input('digite o segundo número: '))
# print (n1 + n2)

n1 = float(input('digite o primeiro número: '))
n2 = float(input('digite o segundo número: '))

# Exercício 1 -> maior valor entre dois números
if n1 > n2:
    print(f"{n1} maior")
else :
    print(f"{n2} maior")

# Exercício 2 -> Entrar via teclado, com dois valores distintos. Exibir o menor deles.
if n1 < n2:
    print(f"{n1} menor")
else :
    print(f"{n2} menor")

# Exercício 3 -> Entrar com dois valores quaisquer. Exibir o maior deles, se existir, caso contrário, enviar mensagem avisando que os números são idênticos.
if n1 > n2:
    print(f"{n1} maior")
elif n2 > n1 :
    print(f"{n2} maior")
else:
    print("Números iguais")