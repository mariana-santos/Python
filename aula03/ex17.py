# Exercício 17 -> Entrar com o peso, o sexo e a altura de uma determinada pessoa. Após a digitação, exibir se esta pessoa está ou não com seu peso ideal. Fórmula: peso/altura².

peso = float(input("Insira seu peso: "))
altura = float(input("Insira sua altura: "))
sexo = str(input("Insira seu sexo: ")).upper()

imc = peso / (altura * altura)

# Caso seja mulher
if sexo == 'F' :
    if imc < 19:
        print("Abaixo do peso")
    elif imc < 24:
        print("Peso ideal")
    else:
        print("Acima do peso")
        
# Caso seja homem
else:
    if imc < 20:
        print("Abaixo do peso")
    elif imc < 25:
        print("Peso ideal")
    else:
        print("Acima do peso")