import re

def verificar_forca_senha(senha):
    comprimento_minimo = 8
    tem_letra_maiuscula = re.search("[A-Z]", senha) is not None
    tem_letra_minuscula = re.search("[a-z]", senha) is not None
    tem_numero = re.search("[0-9]", senha) is not None
    tem_caractere_especial = re.search("[!@#$%^&*(),.?\":{}|<>]", senha) is not None

    if len(senha) < comprimento_minimo:
        return "Sua senha e muito curta. Recomenda-se no minimo 8 caracteres."
    
    if not tem_letra_maiuscula:
        return "Sua senha nao contem letra maiuscula. Inclua pelo menos uma letra maiuscula."
    
    if not tem_letra_minuscula:
        return "Sua senha nao contém letra minuscula. Inclua pelo menos uma letra minuscula."
    
    if not tem_numero:
        return "Sua senha nao contem numero. Inclua pelo menos um numero."
    
    if not tem_caractere_especial:
        return "Sua senha nao atende aos requisitos de seguranca."

    return "Sua senha atende aos requisitos de seguranca. Parabens!"

senha = input().strip()
resultado = verificar_forca_senha(senha)
print(resultado)