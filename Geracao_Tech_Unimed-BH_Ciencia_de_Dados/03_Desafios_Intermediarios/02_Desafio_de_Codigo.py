while True: 
    try:
        entrada = input().upper()

        if entrada == "ESQUERDA":
            print("ingles")
        elif entrada == "DIREITA":
            print("frances")
        elif entrada == "NENHUMA":
            print("portugues")
        else:
            print("caiu")
            break
    except EOFError: 
        break

# Solução Otimizada:
    
# respostas = {
#     "ESQUERDA": "ingles",
#     "DIREITA": "frances",
#     "NENHUMA": "portugues"
# }

# while True:
#     try:
#         entrada = input().upper()
#         print(respostas.get(entrada, "caiu"))
#     except EOFError:
#         break