arquivo_produtos = open('C:\\Users\\User\\Documents\\FIAP\\Python\\aula15\\lista.txt', 'r')

produtos = list()
produtos = arquivo_produtos.readlines()

total = list()

for produto in produtos:
    valores = produto.split(',')

    valores[2] = valores[2].replace('\\n', '')
    
    nome = valores[0]
    qtd = int(valores[1])
    preco = float(valores[2])

    total.append(nome + ',' +str(qtd * preco) + '\n')
    
arquivo_total = open('C:\\Users\\User\\Documents\\FIAP\\Python\\aula15\\total.txt', 'w')

arquivo_total.writelines(total)

# for i, valor in enumerate(produtos):
    # print(valor)
    # if (i % 3 != 0):
    #     produtos.pop(i)

# print(valores)