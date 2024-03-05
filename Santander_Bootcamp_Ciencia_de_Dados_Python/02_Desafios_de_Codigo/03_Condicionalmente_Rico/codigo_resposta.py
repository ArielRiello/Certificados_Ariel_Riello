def saque(saldo_total, valor_saque):
    if valor_saque > saldo_total:
        print("Saldo insuficiente. Saque nao realizado!")
    else:
        novo_saldo = saldo_total - valor_saque
        print(f"Saque realizado com sucesso. Novo saldo: {novo_saldo}")

saldo_total = int(input())
valor_saque = int(input())

saque(saldo_total, valor_saque)