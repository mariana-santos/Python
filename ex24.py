nome = str(input('Digite seu nome: '))
sexo = str(input('Digite seu sexo (F/M): ')).upper()
civil = str(input('Digite seu estado civil: ')).upper()

if(sexo == 'F' and civil == 'CASADA'):
    tempo = int(input('Quantos anos de casada? '))