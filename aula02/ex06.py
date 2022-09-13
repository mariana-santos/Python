# 6. Entrar via teclado com o valor da cotação do dólar e uma certa quantidade de dólares. Calcular e exibir o valor correspondente em Reais (R$).

d = float(input("Digite a cotação atual do dólar: "))
c = float(input("Digite o valor em dólares a ser convertido: "))

r = d * c

print(f"${d} dólares equivalem a R${r} na cotação atual.")