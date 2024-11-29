def verificar_par_impar(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Ímpar"

numero = int(input("Digite um numero e veja se é par ou impar: "))
resultado = verificar_par_impar(numero)
print(resultado)
