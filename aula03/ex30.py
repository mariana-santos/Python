# 30. Elabore um algoritmo que calcule o que deve ser pago por um produto, considerando o preço normal de etiqueta e a escolha da condição de pagamento. Utilize os códigos da tabela a seguir para ler qual a condição de pagamento escolhida e efetuar o cálculo adequado e exibir o valor a ser pago no final.

preco = float(input('Digite o valor do preço normal em R$: '))

print('Códigos de condição de pagamento: ')
print('1 - À vista em dinheiro ou cheque, recebe 10% de desconto')
print('2 - À vista no cartão de crédito, recebe 15% de desconto')
print('3 - Em duas vezes, preço normal de etiqueta sem juros')
print('4 - Em quatro vezes, preço normal de etiqueta mais juros de 10%')

cod = int(input('Digite o código de condição de pagamento: '))

if(cod == 1):
    total = preco - (preco * 0.1)
    qtd = 1
elif (cod == 2):
    total = preco - (preco * 0.15)
    qtd = 1
elif(cod == 3):
    total = preco
    qtd = 2
else:
    total = preco + (preco * 0.1)
    qtd = 4

print(f'Você pagará {qtd} parcela(s) de {total / qtd}. Total: {total}')