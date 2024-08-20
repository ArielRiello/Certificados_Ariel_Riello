def entrada():
    entrada = input()

    lista_valores = list(map(int, entrada.split(',')))

    return lista_valores

def calculo(valores):
    total = sum(valores)

    media = total / len(valores)

    return total, "{:.2f}".format(media)

if __name__ == "__main__":
    valores = entrada()
    total, media = calculo(valores)
    print(f"{total}, {media}")