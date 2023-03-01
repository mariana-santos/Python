opcao = 'S'
clientes = []

while(opcao == 'S'):
    nome = input('Por favor, digite o nome: ')
    email = input('Por favor, digite o e-mail: ')
    idade = int(input('Por favor, digite a idade: '))

    contas = []

    possui_conta = input('Possui conta bancária? (S/N) ').upper()

    while(possui_conta == 'S'):
        ag = input('Digite a agência da conta bancária: ')
        num = int(input('Digite o número da conta bancária: '))
        saldo = float(input('Digite o saldo da conta bancária: '))

        contas.append({"ag": ag, "conta": num, "saldo": saldo})

        possui_conta = input('Deseja cadastrar outra conta? (S/N) ').upper()

    clientes.append({"nome": nome, "email": email, "idade": idade, "contas": contas})

    opcao = input('Deseja cadastrar outro cliente? (S/N) ').upper()

print('\nLista de clientes: \n')

for cliente in clientes:
    print(cliente['nome'])
    print(cliente['email'])
    print(f'{cliente["idade"]} anos ')

    if(len(cliente['contas']) <= 0):
        print(f'Cliente não possui conta bancária.\n')
    else: 
        print('\nLista de contas bancárias cadastradas: ')

    for conta in cliente['contas']:
        print(f'ag.: {conta["ag"]}')
        print(f'c/c: {conta["conta"]}')
        print(f'saldo: {conta["saldo"]}\n')