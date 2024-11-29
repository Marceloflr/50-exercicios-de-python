def segundo_menor(lista):
    if len(lista) < 2:
        return "A lista precisa ter pelo menos dois elementos."
    lista_ordenada = sorted(set(lista))
    return lista_ordenada[1]

numeros = [10, 20, 10, 30, 40, 20]
print(f"O segundo menor valor é: {segundo_menor(numeros)}")
