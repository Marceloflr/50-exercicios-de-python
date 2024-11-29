def maior_menor(n1, n2, n3):
    maior = max(n1, n2, n3)
    menor = min(n1, n2, n3)
    return maior, menor

numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))
numero3 = int(input("Digite o terceiro numero: "))

maior, menor = maior_menor(numero1, numero2, numero3)
print(f"O maior número é {maior} e o menor número é {menor}")
