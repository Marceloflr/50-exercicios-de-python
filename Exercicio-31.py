import random

def adivinhar_numero():
    numero_secreto = random.randint(1, 1000)
    tentativas = 0
    while True:
        chute = int(input("Adivinhe o número (entre 1 e 1000): "))
        tentativas += 1
        if chute < numero_secreto:
            print("Mais alto...")
        elif chute > numero_secreto:
            print("Mais baixo...")
        else:
            print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.")
            break

adivinhar_numero()
