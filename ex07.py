p1 = float(input("Digite o valor do primeiro produto: "))
p2 = float(input("Digite o valor do segundo produto: "))
p3 = float(input("Digite o valor do terceiro produto: "))
p4 = float(input("Digite o valor do quarto produto: "))
p5 = float(input("Digite o valor do quinto produto: "))

pago = float(input("Digite o valor pago pelos produtos: "))

total = p1 +p2 + p3 + p4

troco = pago - total

print(f"Troco da venda: R${troco}")