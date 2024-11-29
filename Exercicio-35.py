import math

def area_circulo(raio):
    return math.pi * (raio ** 2)

raio = float(input("Digite o raio do círculo: "))
print(f"A área do círculo é: {area_circulo(raio):.2f}")
