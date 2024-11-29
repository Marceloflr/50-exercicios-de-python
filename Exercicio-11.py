def menor_valor(lista):
    if not lista:
        return None  # Retorna None se a lista estiver vazia
    menor = lista[0]
    for valor in lista:
        if valor < menor:
            menor = valor
    return menor

lista = [21, 5, 3, 8, 11]
print("O menor valor é:", menor_valor(lista))
