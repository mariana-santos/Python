# Exercício 20 -> Fazer um programa para entrar via teclado com o valor da primeira nota (P1) e o programa deverá calcular e exibir quanto o aluno precisa tirar na segunda nota minimamente (P2) para ser aprovado, sabendo que a média de aprovação é igual a cinco.

p1 = float(input("Digite a primeira nota: "))

p2 = (15 - p1) / 2

print(f'Você precisa de {p2} na próxima nota para ser aprovado. Boa sorte!')