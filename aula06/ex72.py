from math import floor


manha = []
lotacao = 0

tarde = []

noite = []

fileiras = int(input('Quantas fileiras terá a sessão da manhã? '))

while(fileiras < 0):
    fileiras = int(input('Quantidade de linhas inválida. Digite novamente quantas fileiras terá a sessão da manhã: '))

poltronas = int(input('Quantas poltronas terá a sessão da manhã? '))
while(poltronas < 0):
    poltronas = int(input('Quantidade de poltronas inválida. Digite novamente quantas poltronas terá a sessão da manhã: '))

for i in range (0, fileiras, 1):
    manha.append([])

for l in range (0, fileiras, 1):
    for c in range (0, poltronas, 1):
        manha[l].append("Poltrona livre")

opcao = 'S'

while(opcao == 'S'):
    nome = (input('Digite o nome do cliente (com até 5 letras): '))
    fileira = int(input(f'Digite a fileira que você deseja sentar (1 a {fileiras}): ')) - 1
    poltrona = int(input(f'Digite a poltrona que você deseja sentar (1 a {poltronas}): ')) - 1

    while(manha[fileira][poltrona] != 'Poltrona livre'):
        print("Esse assento já está reservado.")
        fileira = int(input('Digite a fileira que você deseja sentar (1 a 10): ')) - 1
        poltrona = int(input('Digite a poltrona que você deseja sentar (1 a 4): ')) - 1

    manha[fileira][poltrona] = nome
    print('Reserva realizada com sucesso!')
    lotacao += 1

    total = fileiras * poltronas

    capacidade = (total / 5) * 4
    
    print(lotacao, floor(capacidade), total)

    if(lotacao != floor(capacidade)):
        opcao = input("Mais alguém deseja reservar? (S/N) ").upper()
    else:
        print('O show chegou em sua capacidade máxima! Sinto muito :(')
        break;

print('Mapa do show do CBJR: ')
for i in range (0, fileira, 1):
    print(manha[i])