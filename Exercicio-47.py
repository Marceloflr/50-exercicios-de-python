class CaixaEletronico:
    def __init__(self, saldo=0):
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor:.2f} realizado com sucesso.")

    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente.")
        else:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")

    def consultar_saldo(self):
        print(f"Seu saldo é: R${self.saldo:.2f}")

caixa = CaixaEletronico()
caixa.depositar(int(input("Digite o valor que voce ira depositar na sua conta: ")))
caixa.sacar(int(input("Digite o valor que voce ira sacar na sua conta: ")))
caixa.consultar_saldo()
