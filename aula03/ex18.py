# Exercício 18 ->  A partir dos valores da aceleração (a em m/s2), da velocidade inicial (v0 em m/s) e do tempo de percurso (t em s). Calcular e exibir a velocidade final de automóvel em km/h. Exibir mensagem de acordo com a tabela:

a = float(input("Digite a aceleração do veículo em m/s² "))
v0 = float(input("Digite a velocidade inicial do veículo em m/s "))
t = float(input("Digite o tempo de percurso em segundos "))

# fórmula velocidade inicial
v = v0 + a*t

# transformando em km/h
v = v * 3.6

print(f"Velocidade final: {v}km/h")

if(v <= 40):
    print('Veículo muito lento')
elif(v > 40 and v <= 60):
    print('Velocidade permitida')
elif(v > 60 and v <= 80):
    print('Velocidade de cruzeiro')
elif (v > 80 and v <= 120):
    print('Veículo rápido')
else:
    print('Veículo muito rápido')