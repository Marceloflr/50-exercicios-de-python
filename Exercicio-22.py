def segundo_maior(lista):
    if len(lista) < 2:
        return "A lista precisa ter pelo menos dois elementos."
    primeiro, segundo = float('-inf'), float('-inf')
    for num in lista:
        if num > primeiro:
            segundo = primeiro
            primeiro = num
        elif primeiro > num > segundo:
            segundo = num
    return segundo

lista_exemplo = [2, 4, 42, 22, 6, 7]
print("O segundo maior valor da lista é:", segundo_maior(lista_exemplo))
