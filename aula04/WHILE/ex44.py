# 44. Entrar via teclado com dez valores positivos. Consistir a digitação e enviar mensagem de erro, se necessário. Após a digitação, exibir:
# a) O maior valor;
# b) A soma dos valores;
# c) A média aritmética dos valores;

soma = 0
maior = 0
i = 1

while (i <= 10):
    n = int(input(f"Digite o {i}° número: "))

    while(n < 0):
        n = int(input(f"Números negativos não são aceitos. Digite o {i}° número novamente: "))

    soma += n

    if(n > maior):
        maior = n

    i+= 1

print(f"a) O maior valor: {maior}")
print(f"b) A soma dos valores: {soma}")
print(f"c) A média aritmética dos valores: {soma / 10}")