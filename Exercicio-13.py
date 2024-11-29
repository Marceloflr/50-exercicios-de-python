def soma_impares(lista):
    soma = 0
    for numero in lista:
        if numero % 2 != 0:
            soma += numero
    return soma

lista = [11, 222, 37, 4, 5]
print("A soma dos números ímpares é:", soma_impares(lista))
