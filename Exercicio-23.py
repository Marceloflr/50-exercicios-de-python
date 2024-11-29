def fibonacci_ate_valor(limite):
    sequencia = [0, 1]
    while sequencia[-1] + sequencia[-2] <= limite:
        sequencia.append(sequencia[-1] + sequencia[-2])
    return sequencia

valor_limite = int(input("Digite o valor limite: "))
sequencia_fibonacci = fibonacci_ate_valor(valor_limite)
print(f"Sequência de Fibonacci até {valor_limite}:", sequencia_fibonacci)
