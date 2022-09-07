a = int(input('Digite o valor A: '))
b = int(input('Digite o valor B: '))
c = int(input('Digite o valor C: '))

nums = [a, b, c]

nums = sorted(nums, reverse = True)
print('Valores em ordem decrescente: ', nums)