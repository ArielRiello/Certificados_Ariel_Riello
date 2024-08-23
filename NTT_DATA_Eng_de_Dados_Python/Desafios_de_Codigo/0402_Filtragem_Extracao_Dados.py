def extrair_anos(datas):
    lista_datas = datas.split(", ")
    anos = [data.split("-")[0] for data in lista_datas]
    return ", ".join(anos)

entrada = input()
saida = extrair_anos(entrada)
print(saida)