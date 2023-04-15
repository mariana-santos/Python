produtos = list()

for i in range(3):
    print('\n----------Dados do '+ str(i + 1) + '° produto----------')
    nome = input('Por favor, digite o nome: ')
    qtd = int(input('Por favor, digite a quantidade: '))
    preco = float(input('Por favor, digite o preço: '))

    produtos.append(nome + ',' + str(qtd) + ',' + str(preco) + '\n')

arquivo_produtos = open('C:\\Users\\User\\Documents\\FIAP\\Python\\aula15\\lista.txt', 'w')

arquivo_produtos.writelines(produtos)