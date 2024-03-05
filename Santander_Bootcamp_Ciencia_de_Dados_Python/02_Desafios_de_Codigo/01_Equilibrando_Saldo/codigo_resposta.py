saldo_atual = float(input())
valor_deposito = float(input())
valor_retirada = float(input())

#TODO: Calcular o saldo atualizado de acordo com a descrição deste desafio.
saldo_final = (saldo_atual + valor_deposito) - valor_retirada

saida = "Saldo atualizado na conta: {:.1f}".format(saldo_final)

#TODO: Imprimir o a saída de conforme a tabela de exemplos (uma casa decimal).
print(saida)