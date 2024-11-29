def contar_palavras(frase):
    return len(frase.split())

frase = input("Digite uma frase: ")
print(f"Número de palavras: {contar_palavras(frase)}")
