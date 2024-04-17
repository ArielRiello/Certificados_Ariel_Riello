import re

def validar_numero():
    numero = input()
    padrao = r"\(\d{2}\) 9\d{4}-\d{4}"
    if re.match(padrao, numero):
        return "Número de telefone válido."
    else:
        return "Número de telefone inválido."

print(validar_numero())