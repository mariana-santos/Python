sala = []
retornar = 'S'
lotacao = 0

for i in range (0, 5, 1):
    sala.append([])

for l in range (0, 5, 1):
    for c in range (0, 8, 1):
        sala[l].append("-----")

while retornar == 'S':
    nome = (input('Digite o nome do aluno (com até 5 letras): '))

    # MANIPULANDO A STRING NOME PRA TER EXATAMENTE 5 CARCACTERES E FICAR PADRONIZADA
    if(len(nome) > 5):
        nome = nome[0:5]

    elif(len(nome) < 5):

        charFaltam = 5 - len(nome)
        espacos = ''
        for i in range(0, charFaltam, 1):
            espacos = espacos + ' '

        nome = nome[0:len(nome)] + espacos


    fileira = int(input('Digite a fileira que você deseja sentar (1 a 5): ')) - 1
    carteira = int(input('Digite a carteira em que você deseja sentar (1 a 8): ')) - 1

    while(sala[fileira][carteira] != '-----'):
        print("Essa carteira já está ocupada! Por favor, escolha outro lugar")
        fileira = int(input('Digite a fileira que você deseja sentar (1 a 10): ')) - 1
        carteira = int(input('Digite a carteira que você deseja sentar (1 a 4): ')) - 1

    sala[fileira][carteira] = nome
    print('Reserva da carteira realizada com sucesso!')
    lotacao += 1
    
    if(lotacao != 40):
        retornar = input("Deseja realizar uma nova reserva? (S/N) ").upper()
    else:
        print('Todas as carteiras foram preenchidas! Sinto muito :(')
        break

print('Mapa de sala da turma: ')
for i in range (0, 5, 1):
    print(sala[i])