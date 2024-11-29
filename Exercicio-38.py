from collections import deque

def fila_banco():
    fila = deque()
    while True:
        acao = input("Digite 'chegada' para adicionar cliente ou 'atender' para atender cliente (ou 'sair' para finalizar): ")
        if acao.lower() == 'chegada':
            nome = input("Digite o nome do cliente: ")
            fila.append(nome)
            print(f"{nome} entrou na fila.")
        elif acao.lower() == 'atender':
            if fila:
                cliente_atendido = fila.popleft()
                print(f"Atendendo {cliente_atendido}.")
            else:
                print("Não há clientes na fila.")
        elif acao.lower() == 'sair':
            break
        else:
            print("Ação inválida.")

fila_banco()
