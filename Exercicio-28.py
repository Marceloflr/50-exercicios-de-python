def para_binario(numero):
    return bin(numero)[2:]

numero = int(input("Escreva um numero para se tornar uma representação binaria: "))
print(f"A representação binária de {numero} é {para_binario(numero)}")
