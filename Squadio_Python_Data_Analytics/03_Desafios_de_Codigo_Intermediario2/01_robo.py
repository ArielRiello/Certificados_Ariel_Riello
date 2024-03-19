def classificar_numero(numero):
    if numero > 0:
        return "positivo!"
    elif numero < 0:
        return "negativo!"

def main():
    positivos = 0
    negativos = 0
    
    while True:
        numero = int(input())
        
        if numero == 0:
            break
        
        classificacao = classificar_numero(numero)
        print(classificacao)
        
        if classificacao == "positivo!":
            positivos += 1
        elif classificacao == "negativo!":
            negativos += 1
    
    print(f"{positivos} números positivos, {negativos} números negativos")

if __name__ == "__main__":
    main()