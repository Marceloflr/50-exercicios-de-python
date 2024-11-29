def calcular_mmc(a, b):
    def mdc(x, y):
        while y:
            x, y = y, x % y
        return x

    return abs(a * b) // mdc(a, b)

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
print(f"O MMC de {numero1} e {numero2} é: {calcular_mmc(numero1, numero2)}")
