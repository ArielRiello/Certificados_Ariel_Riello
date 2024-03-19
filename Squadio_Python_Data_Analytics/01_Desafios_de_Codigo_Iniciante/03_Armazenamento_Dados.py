capacidade_atual, aumento_percentual = map(int, input().split())

aumento = (aumento_percentual * capacidade_atual) / 100

capacidade_final = capacidade_atual + aumento

print(round(capacidade_final))