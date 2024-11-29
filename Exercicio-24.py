import random

def lancar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    soma = dado1 + dado2
    return dado1, dado2, soma

dado1, dado2, soma = lancar_dados()
print(f"Resultado do dado 1: {dado1}")
print(f"Resultado do dado 2: {dado2}")
print(f"Soma dos resultados: {soma}")
