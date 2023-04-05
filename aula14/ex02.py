from cliente import Cliente
from produto import Produto

base_dados = "CJose dos Santos,42,Sao Paulo;CSandra Silva,36,Sao Jose do Rio Preto;CAugusto Soares,22,Sao Paulo;CVanderlei Azevedo,45,Santos;CVanessa Ferreira,27,Sao Paulo;PMouse,1,9.90;PTeclado,3,19.90;PMonitor,2,349.90;PHD SSD,2,199.90;PProcessador,1,350.00"

dados = base_dados.split(';')

id_cliente = 0
id_produto = 0

lista_clientes = {}
lista_produtos = {}

for dado in dados:
    campos = dado.split(",")
    tipo = campos[0]
    tipo = tipo[0]

    nome = campos[0]
    nome = nome[1:len(nome)]

    if(tipo == 'C'):
        idade = campos[1]
        cidade = campos[2]
        cliente = Cliente(nome, idade, cidade)
        
        lista_clientes[id_cliente] = cliente
        id_cliente += 1
    else:
        qtd = campos[1]
        preco = campos[2]
        produto = Produto(nome, qtd, preco)

        lista_produtos[id_produto] = produto
        id_produto += 1

print('Clientes: \n')
for id_cliente, cliente in lista_clientes.items():
    print(f'Nome: {cliente.nome}')
    print(f'Idade: {cliente.idade}')
    print(f'Cidade: {cliente.cidade} \n')

print('Produtos: \n')
for id_produto, produto in lista_produtos.items():
    print(f'Nome: {produto.nome}')
    print(f'Qtd em estoque: {produto.qtd}')
    print(f'Preço: {produto.preco} \n')