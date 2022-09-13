# 39. Exibir os trinta primeiros valores da série de Fibonacci. A série: 1, 1, 2, 3, 5, 8, ...

a = 0
b = 1
f = a + b

i = 1

while(i <= 30):
    print(f)
    b = a
    a = f
    f = a+b
    i += 1