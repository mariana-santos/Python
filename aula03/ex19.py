# Exercício 19 -> Fazer um programa para entrar via teclado com os valores das notas (P1 e P2) e calcular a média. Exibir a situação final do aluno (“Aprovado ou Reprovado”), sabendo que a média de aprovação é igual a cinco.

p1 = float(input("Digite a primeira nota: "))
p2 = float(input("Digite a segunda nota: "))

media = (p1 + 2*p2) /3

if(media >= 5):
    print(f"Média final {media}. Aluno aprovado. :)")
else:
    print(f"Média final {media}. Aluno reprovado. :/")