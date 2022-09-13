# 33. Entrar via teclado com o sexo de determinado usuário, aceitar somente “F” ou “M” como respostas válidas.

sexo = str(input('Digite o seu sexo F/M: '))

# While
while(sexo != 'F' and sexo != 'M'):
    print(f'Sexo {sexo} inválido. Digite outro valor válido')
    sexo = str(input('Digite o seu sexo F/M: '))

print(f'Sexo {sexo}. Fim')