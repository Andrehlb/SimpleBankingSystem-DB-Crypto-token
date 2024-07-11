# Autor: André Luiz Barbosa
# Data: 11/07/2022

import datetime

# Classe bancária usuário
def __init__(self):
    self.saldo = 0
    self.extrato = []
    self_saques_diarios = 0
    self.data_último_saque = datetime.date.today()

def depositar(self, valor):
    self.saldo += valor
    self.extrato.append({"tipo": "Deposito", "valor": valor, "data": datetime.date.today()})

def sacar(self, valor):
    if self.saques.diario < 3 and valor <= 500 and self.saldo >= valor:
        self.saldo -= valor
        self.saques_diarios += 1
        self.data_ultimo_saque = datetime.date.today()
        self.extrato.append({"tipo": "Saque", "valor": valor, "data": datetime.date.today()})
    else
        print("Saque não permitido.")


