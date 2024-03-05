valor_inicial = float(input())
taxa_juros = float(input())
periodo = int(input())

valor_final = valor_inicial

contador = periodo
while contador > 0:
    valor_juros = (valor_final * taxa_juros)
    valor_final += valor_juros
    contador -= 1

print("Valor final do investimento: R$ {:.2f}".format(valor_final))