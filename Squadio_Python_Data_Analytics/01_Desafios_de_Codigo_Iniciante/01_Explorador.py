quantidade_passos = int(input())

if quantidade_passos <= 0:
    print("Nenhum passo dado na floresta.")
    

for passos in range(1, quantidade_passos + 1):

    mensagem = f"Explorador: {passos} passos"

    if passos == 1:
        mensagem = "Explorador: 1 passo"

    print(mensagem)