def contar_vogais(palavra):
    vogais = input("Digite uma vogal: ")
    contador = 0
    for letra in palavra:
        if letra in vogais:
            contador += 1
    return contador

palavra = "exemplo"
print("Número de vogais:", contar_vogais(palavra))
