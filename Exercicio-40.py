def substituir_vogais(string):
    vogais = "aeiouAEIOU"
    nova_string = ''.join(['*' if c in vogais else c for c in string])
    return nova_string

texto = "Guilherme programador"
print("Texto com vogais substituídas:", substituir_vogais(texto))
