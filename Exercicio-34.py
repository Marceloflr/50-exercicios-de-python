def contar_repetidos(lista):
    contagem = {}
    for elemento in lista:
        if elemento in contagem:
            contagem[elemento] += 1
        else:
            contagem[elemento] = 1
    repetidos = {k: v for k, v in contagem.items() if v > 1}
    return repetidos

lista_exemplo = [1, 2, 2, 3, 3, 3, 4]
print("Elementos repetidos:", contar_repetidos(lista_exemplo))
