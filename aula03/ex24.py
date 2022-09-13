# 24. Faça um algoritmo que leia o nome, o sexo e o estado civil de uma pessoa. Caso sexo seja “F” e estado civil seja “CASADA”, solicitar o tempo de casada (anos).

nome = str(input('Digite seu nome: '))
sexo = str(input('Digite seu sexo (F/M): ')).upper()
civil = str(input('Digite seu estado civil: ')).upper()

if(sexo == 'F' and civil == 'CASADA'):
    tempo = int(input('Quantos anos de casada? '))