entrada = input().split()

distancia = int(entrada[0])
diametro1 = int(entrada[1])
diametro2 = int(entrada[2])

if 0 < distancia < 10000 and 0 < diametro1 < 100 and 0 < diametro2 < 100:
    def ICM(distancia, diametro1, diametro2):
        soma = diametro1 + diametro2
        calculo_ICM = distancia / soma
        return "{:.2f}".format(calculo_ICM)

    resultado_ICM = ICM(distancia, diametro1, diametro2)
    print(resultado_ICM)