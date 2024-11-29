import random

def gerar_lista_aleatoria(tamanho, limite_inferior, limite_superior):
    lista = [random.randint(limite_inferior, limite_superior) for _ in range(tamanho)]
    return lista

def encontrar_maior_menor(lista):
    maior = max(lista)
    menor = min(lista)
    return maior, menor

tamanho_lista = int(input("Digite o numero do 'tamanho_lista': "))
limite_inferior = int(input("Digite o numero do 'limite_inferior': "))
limite_superior = int(input("Digite o numero do 'limite_superior': "))

lista = gerar_lista_aleatoria(tamanho_lista, limite_inferior, limite_superior)
maior_valor, menor_valor = encontrar_maior_menor(lista)

print("Lista gerada:", lista)
print("Maior valor:", maior_valor)
print("Menor valor:", menor_valor)
