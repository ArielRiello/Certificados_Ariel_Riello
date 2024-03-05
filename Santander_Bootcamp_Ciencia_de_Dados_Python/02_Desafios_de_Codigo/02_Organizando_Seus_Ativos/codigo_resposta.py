ativos = []

# Entrada da quantidade de ativos
quantidadeAtivos = int(input())

# Entrada dos códigos dos ativos
for _ in range(quantidadeAtivos):
    codigoAtivo = input()
    ativos.append(codigoAtivo)

# TODO: Ordenar os ativos em ordem alfabética.
ativos_ordenados = sorted(ativos)

# TODO: Imprimir a lista de ativos ordenada, conforme a tabela de exemplos.
for i in range(len(ativos_ordenados)):
    print(f"{ativos_ordenados[i]}")