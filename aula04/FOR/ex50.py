a = int(input('Digite um valor qualquer: '))
b = int(input('Digite um valor qualquer: '))

for a in range(a, b + 1, 1):
    if (a % 2 == 0 and a > 10):
        print(a)
