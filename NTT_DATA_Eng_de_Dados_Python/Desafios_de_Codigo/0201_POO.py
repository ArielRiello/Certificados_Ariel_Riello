class Venda:
    def __init__(self, produto, quantidade, valor):
        self.produto = produto
        self.quantidade = quantidade
        self.valor = valor

class Relatorio:
    def __init__(self):
        self.vendas = []

    def adicionar_venda(self, venda):
        if isinstance(venda, Venda):
            self.vendas.append(venda)

    def calcular_total_vendas(self):
        total = 0
        for venda in self.vendas:
            total += venda.quantidade * venda.valor
        return total

def main():
    relatorio = Relatorio()
    
    for i in range(3):
        produto = input().strip()
        quantidade = int(input().strip())
        valor = float(input().strip())
        venda = Venda(produto, quantidade, valor)
        relatorio.adicionar_venda(venda)
    
    total_vendas = relatorio.calcular_total_vendas()
    print(f"Total de Vendas: {total_vendas}")

main()