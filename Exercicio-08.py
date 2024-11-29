def calcular_media(numeros):
    if len(numeros) == 0:
        return 0
    return sum(numeros) / len(numeros)

entrada = input("Digite uma lista de números separados por espaço: ")

numeros = [float(num) for num in entrada.split()]

media = calcular_media(numeros)

print("A média dos números é:", media)
