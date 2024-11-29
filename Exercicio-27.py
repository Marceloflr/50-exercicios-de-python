def estatisticas_lista(lista):
    media = sum(lista) / len(lista)
    maior = max(lista)
    menor = min(lista)
    return media, maior, menor

numeros = [20, 30, 91, 7, 76, 44]
media, maior, menor = estatisticas_lista(numeros)
print(f"Média: {media}, Maior: {maior}, Menor: {menor}")
