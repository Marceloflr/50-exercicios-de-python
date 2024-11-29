def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

peso = float(input("Digite o seu peso (kg): "))
altura = float(input("Digite a sua altura (m): "))
print(f"Seu IMC é: {calcular_imc(peso, altura):.2f}")
