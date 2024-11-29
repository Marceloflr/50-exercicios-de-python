def contar_nao_letras(string):
    nao_letras = [c for c in string if not c.isalpha()]
    return len(nao_letras)

texto = "Guilherme o numero 1 em programaçao!"
print(f"Número de caracteres que não são letras: {contar_nao_letras(texto)}")
