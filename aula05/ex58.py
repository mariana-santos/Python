nome = []
idade = []
sexo = []

for i in range(0, 5, 1):
    nome_str = str(input('Qual seu nome? '))
    nome.append(nome_str)

    idade_int = int(input('Qual sua idade? '))

    while(idade_int < 0):
        idade_int = int(input('Idade digitada inválida. Qual sua idade? '))

    idade.append(idade_int)

    sexo_str = str(input('Qual seu sexo (F/M)? ')).upper()

    while(sexo_str != 'M' and sexo_str != 'F'):
        sexo_str = str(input('Sexo digitado inválido. Qual seu sexo (F/M)? ')).upper()

    sexo.append(sexo_str)

maiores = 0

for i in range(0, 5, 1):
    if(idade[i] > 18):
        maiores += 1
        print(f'{nome[i]}: {idade[i]} ano(s) - sexo {sexo[i]}')

print(f'{maiores} maiores de idade')