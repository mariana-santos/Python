pedidos = []

def cadastrarProuto():
    nomeProd = input("Digite o nome do produto: ")
    while(nomeProd == ''):
        nomeProd = input("Nome do produto é um campo obrigatório! Por favor, digite novamente ")

    qtdProd = int(input("Digite a quantidade de produtos desejada: "))
    while qtdProd <= 0:
        qtdProd = int(input("Quantidade inválida. Por favor, digite novamente: "))

    preco = float(input("Digite o preço do produto: "))
    while preco <= 0:
        preco = int(input("Preço inválido. Por favor, digite novamente: "))

    produto = {"nome": nomeProd, "qtd": qtdProd, "preco": preco}
    return produto


def cadastrarPedido(nome, qtd):
    produtos = []
    for i in range(qtd):
        print(f"---Dados do {(i + 1)}° produto---")
        
        produtos.append(cadastrarProuto())
       
        pedido = {"nome": nome, "produtos": produtos}

        pedidos.append(pedido)       

def inserirPedidosArquivo():
    arquivo = open("C:\\Users\\logonrmlocal\\Desktop\\pedidos.txt", 'w')

    string = ''

    for pedido in pedidos:
        string += (pedido["nome"] + "\n")
        produtos = pedido["produtos"]

        for prod in produtos:
            string += (prod["nome"] + ',')
            string += (str(prod["qtd"]) + ',')
            string += (str(prod['preco']) + "\n")

        string += '\n'
    arquivo.write(string)

def inserirTotalArquivo():
    path_pedidos = open("C:\\Users\\logonrmlocal\\Desktop\\pedidos.txt", 'r')
    path_total = open("C:\\Users\\logonrmlocal\\Desktop\\total_pedidos.txt", 'a')

    string = ''
    linhas = path_pedidos.readlines()
    novas_linhas = [linha.rstrip('\n') for linha in linhas]

    print(novas_linhas)

    for linha in novas_linhas:
        if(linha != ''):
            dados = linha.split(',')

            if(len(dados) > 1):
                qtd = float(dados[1])
                preco = float(dados[2])
                total = qtd * preco
                string += ("R$" + str(total) + "\n")
            else:
                string += linha + " - "
        
    path_total.write(string)

novoPedido = 'S'
while(novoPedido == 'S'):
    nome = input("Para começar, qual o seu nome? ")
    while(nome == ''):
        nome = input("Nome é um campo obrigatório! Por favor, digite novamente ")

    qtd = int(input("Quantos produtos deseja comprar? "))
    while qtd <= 0:
        qtd = int(input("Quantidade inválida. Por favor, digite novamente: "))

    cadastrarPedido(nome, qtd)
    novoPedido = input("Deseja fazer um novo pedido? ").upper()

inserirPedidosArquivo()
inserirTotalArquivo()