valores = input().split()

horas, velocidade_media = valores

horas = int(horas)
velocidade_media = int(velocidade_media)

distancia = horas * velocidade_media

consumo = distancia / 12

print("{:.3f}".format(consumo))