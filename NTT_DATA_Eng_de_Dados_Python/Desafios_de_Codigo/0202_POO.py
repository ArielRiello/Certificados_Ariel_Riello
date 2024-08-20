class Venda:
    def __init__(self, produto, quantidade, valor):
        self.produto = produto
        self.quantidade = quantidade
        self.valor = valor

class Categoria:
    def __init__(self, nome):
        self.nome = nome
        self.vendas = []

    def adicionar_venda(self, venda):
        self.vendas.append(venda)

    def total_vendas(self):
        total = 0
        for venda in self.vendas:
            total += venda.quantidade * venda.valor / venda.quantidade
        return total

def main():
    categorias = []

    for i in range(2):
        nome_categoria = input().strip()
        categoria = Categoria(nome_categoria)

        for j in range(2): 
            entrada_venda = input().strip()
            produto, quantidade, valor = entrada_venda.split(',')
            quantidade = int(quantidade.strip())
            valor = float(valor.strip())

            venda = Venda(produto.strip(), quantidade, valor)
            categoria.adicionar_venda(venda)

        categorias.append(categoria)
    
    for categoria in categorias:
        total = categoria.total_vendas()
        print(f"Vendas em {categoria.nome}: {total:.1f}")

if __name__ == "__main__":
    main()