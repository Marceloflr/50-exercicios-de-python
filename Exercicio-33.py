def intersecao_listas(lista1, lista2):
    return list(set(lista1) & set(lista2))

lista1 = [1, 2, 3, 44, 5]
lista2 = [44, 5, 6, 7, 8]
print("Interseção entre as listas:", intersecao_listas(lista1, lista2))