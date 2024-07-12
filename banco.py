# Autor: André Luiz Barbosa
# Data: 11/07/2022

import datetime

# Classe bancária usuário

class Usuario:
    def __init__(self):
        self.saldo = 0
        self.extrato = []
        self.saques_diarios = 0
        self.data_ultimo_saque = datetime.date.today()

    def depositar(self, valor):
        self.saldo += valor
        self.extrato.append({"tipo": "Deposito", "valor": valor, "data": datetime.date.today()})

    def sacar(self, valor):
        if self.data_ultimo_saque != datetime.date.today():
            self.saques_diarios = 0
        if self.saques_diarios == 2 and valor <= 500 and self.saldo >= valor:
            print("Aviso: este é seu último saque permitido para hoje.")
            self.saldo -= valor
            self.saques_diarios += 1
            self.data_ultimo_saque = datetime.date.today()
            self.extrato.append({"tipo": "Saque", "valor": valor, "data": datetime.date.today()})
        else:
            print("Saque não permitido.")
        
    def ve_extrato(self):
        for transacao in self.extrato:
            print(f"{transacao['data']}: {transacao['tipo']} de R$ {transacao['valor']:, .2f}")
        print(f"Saldo atual: R$ {self.saldo:, .2f}")

def main():
    usuario = Usuario()

    while True:
        print("1. Depositar")
        print("2. Sacar")
        print("3. Ver extrato")
        print("4. Sair")
        opcao = int(input("Escolha uma opção: "))
        if opcao == 1:
            valor = float(input("Digite o valor para depósito: "))
            usuario.depositar(valor)
        elif opcao == 2:
            valor = float(input("Digite o valor a sacar: "))
            usuario.sacar(valor)
        elif opcao == 3:
            usuario.ve_extrato()
        elif opcao == 4:
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()