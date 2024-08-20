from datetime import datetime, timedelta

class Transacao:
    def __init__(self, tipo, valor):
        self.tipo = tipo
        self.valor = valor
        self.data = datetime.now()

class ContaBancaria:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial
        self.transacoes = []

    def depositar(self, valor):
        if self._verificar_limite_diario():
            self.saldo += valor
            self.transacoes.append(Transacao('Depósito', valor))
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso. Saldo atual: R$ {self.saldo:.2f}")
        else:
            print("Limite de transações diárias atingido.")

    def sacar(self, valor):
        if self._verificar_limite_diario():
            if valor <= self.saldo:
                self.saldo -= valor
                self.transacoes.append(Transacao('Saque', valor))
                print(f"Saque de R$ {valor:.2f} realizado com sucesso. Saldo atual: R$ {self.saldo:.2f}")
            else:
                print("Saldo insuficiente.")
        else:
            print("Limite de transações diárias atingido.")

    def _verificar_limite_diario(self):
        hoje = datetime.now().date()
        transacoes_hoje = [t for t in self.transacoes if t.data.date() == hoje]
        return len(transacoes_hoje) < 10

    def exibir_transacoes(self):
        for transacao in self.transacoes:
            print(f"{transacao.data} - {transacao.tipo}: R$ {transacao.valor:.2f}")

# Exemplo de uso
conta = ContaBancaria(saldo_inicial=1000)

conta.depositar(200)
conta.sacar(100)

# Tentar mais de 10 transações em um dia para testar o limitador
for _ in range(10):
    conta.depositar(50)

conta.exibir_transacoes()