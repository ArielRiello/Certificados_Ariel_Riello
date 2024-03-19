def prever_fruta(peso, textura, cor):
    if peso >= 130 and textura == "rough" and cor == "red":
        return "A fruta é uma maçã!"
    elif peso >= 120 and textura == "smooth" and cor == "orange":
        return "A fruta é uma laranja!"
    elif peso >= 150 and textura == "smooth" and cor == "red":
        return "A fruta é um morango!"
    elif peso >= 150 and textura == "rough" and cor == "yellow":
        return "A fruta é uma banana!"
    else:
        return "Não foi possível classificar a fruta."

peso_fruta = float(input())
textura_fruta = input()
cor_fruta = input()

resultado = prever_fruta(peso_fruta, textura_fruta, cor_fruta)

print(resultado)