ativos = []

quantidadeAtivos = int(input())

for _ in range(quantidadeAtivos):
    codigoAtivo = input()
    ativos.append(codigoAtivo)

ativos_ordenados = sorted(ativos)

for i in range(len(ativos_ordenados)):
    print(f"{ativos_ordenados[i]}")