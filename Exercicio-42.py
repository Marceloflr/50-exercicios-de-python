def eh_perfeito(numero):
    soma_divisores = sum([i for i in range(1, numero) if numero % i == 0])
    return soma_divisores == numero

numero = int(input("Escreva um numero para determinar se ele é perfeito: "))
print(f"O número {numero} é perfeito? {eh_perfeito(numero)}")
