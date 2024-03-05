import string

letra = input() 

letra = letra.upper()

alfabeto_maiusculas = list(string.ascii_uppercase)

posicao = alfabeto_maiusculas.index(letra)

print(posicao + 1)