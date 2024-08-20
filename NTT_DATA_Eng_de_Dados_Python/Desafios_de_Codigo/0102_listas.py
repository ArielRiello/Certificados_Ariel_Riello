def produto_mais_vendido(produtos):
    contagem = {}
    
    for produto in produtos:
        if produto in contagem:
            contagem[produto] += 1
        else:
            contagem[produto] = 1
    
    max_produto = None
    max_count = 0
    
    for produto, count in contagem.items():
        if count > max_count:
            max_count = count
            max_produto = produto
    
    return max_produto

def obter_entrada_produtos():
    entrada = input()
    produtos = [produto.strip() for produto in entrada.split(',')]
    return produtos

produtos = obter_entrada_produtos()
produto_mais_frequente = produto_mais_vendido(produtos)
print(produto_mais_frequente)