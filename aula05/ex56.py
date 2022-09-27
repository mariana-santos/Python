nome = []
idade = []

for i in range(0, 5, 1):
    nome_str = str(input('Qual seu nome? '))
    nome.append(nome_str)

    idade_int = int(input('Qual sua idade? '))
    idade.append(idade_int)

for i in range(0, 5, 1):
    print(f'{nome[i]}: {idade[i]} ano(s)')