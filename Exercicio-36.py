def media_turma():
    notas = []
    while True:
        nota = input("Digite a nota do aluno (ou 'finalizar' para calcular a média): ")
        if nota.lower() == 'finalizar':
            break
        notas.append(float(nota))
    media = sum(notas) / len(notas)
    return media

print(f"A média da turma é: {media_turma():.2f}")
