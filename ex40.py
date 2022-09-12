# 40. Exibir os vinte primeiros valores da série de Bergamaschi. A série: 1, 1, 1, 3, 5, 9, 17, …

a = -1
b = 1
c = 1
r = a+b+c

for i in range(1, 21, 1):
    print(r)
    c = b
    b = a
    a = r
    r = a+b+c