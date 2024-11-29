def calcular_termo_n(a1, r, n):
    return a1 + (n - 1) * r

def calcular_soma_sequencia(a1, r, n):
    return (n / 2) * (2 * a1 + (n - 1) * r)

a1 = float(input("Digite o primeiro termo (a1) da sequência: "))
r = float(input("Digite a razão (r) da sequência: "))
n = int(input("Digite o número de termos (n) da sequência: "))

an = calcular_termo_n(a1, r, n)
soma = calcular_soma_sequencia(a1, r, n)

print(f"O {n}-ésimo termo da sequência é: {an}")
print(f"A soma dos {n} primeiros termos da sequência é: {soma}")
