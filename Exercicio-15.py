idades = []

for i in range(10):
    idade = int(input(f"Digite a idade da pessoa {i+1}: "))
    idades.append(idade)

media = sum(idades) / len(idades)

print(f"A média das idades é: {media:.2f}")
