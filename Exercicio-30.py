def soma_digitos(numero):
    soma = 0
    while numero > 0:
        soma += numero % 10
        numero //= 10
    return soma

numero = int(input("Digite um número: "))
print(f"A soma dos dígitos de {numero} é {soma_digitos(numero)}")
