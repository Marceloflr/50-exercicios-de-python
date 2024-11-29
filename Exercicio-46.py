def matriz_identidade(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]

n = 3
print("Matriz identidade:")
for linha in matriz_identidade(n):
    print(linha)
