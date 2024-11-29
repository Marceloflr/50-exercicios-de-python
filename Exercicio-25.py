def remover_espacos(texto):
    return texto.replace(" ", "")


texto = input("Digite uma frase: ")
texto_sem_espacos = remover_espacos(texto)
print("Texto sem espaços:", texto_sem_espacos)
