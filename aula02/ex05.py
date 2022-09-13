# 5. Entrar via teclado com o valor de uma temperatura em graus Celsius, calcular e exibir sua temperatura equivalente em Fahrenheit.

c = float(input("Digite o valor da temperatura em °C: "))

f = (c * 9/5) + 32

print(f"{c}°C equivalem a {f}F")