def maior_valor():
    numeros = []
    for i in range(5):
        numero = float(input(f"Digite o {i+1}º número: "))
        numeros.append(numero)
    maior = max(numeros)
    print(f"O maior valor é: {maior}")

maior_valor()
