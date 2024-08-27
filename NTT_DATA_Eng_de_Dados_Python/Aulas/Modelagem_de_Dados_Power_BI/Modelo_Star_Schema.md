
## Esquema em Estrela

A modelagem com Star Schema (Esquema em Estrela) é uma abordagem comum em projetos de Data Warehousing. Essa técnica é usada principalmente para organizar dados de forma que seja fácil realizar consultas analíticas eficientes, como as que ocorrem em sistemas de Business Intelligence (BI). Vou explicar os principais componentes e como criar um esquema em estrela.

### Estrutura do Star Schema

- Tabela Fato (Fact Table):
    - Descrição: A tabela fato armazena as métricas ou fatos numéricos que você deseja analisar. Cada linha na tabela fato corresponde a um evento ou transação específica, como uma venda, uma visita a um site, ou uma transação bancária.
        
    - Chaves Estrangeiras: A tabela fato contém chaves estrangeiras que fazem referência às tabelas dimensão, permitindo associar cada fato aos detalhes descritivos.
    
    - Exemplo de Métricas: Quantidade vendida, valor da venda, número de visitas, etc.

- Tabelas Dimensão (Dimension Tables):
    - Descrição: As tabelas dimensão armazenam os atributos descritivos relacionados aos fatos. Esses atributos fornecem contexto aos fatos e podem ser usados para criar filtros ou agrupar os dados.
        
    - Exemplo de Atributos: Nome do produto, categoria, data da venda, localização, cliente, etc.
        
    - Características: Geralmente, essas tabelas têm um número menor de registros, mas cada registro é bastante descritivo.

### Como Criar um Star Schema

- Identifique o Fato Central:
    - Determine o que será medido ou analisado (ex.: vendas, acessos, transações). Este será o centro do seu esquema em estrela.

- Defina as Dimensões:
    - Identifique as dimensões que fornecerão contexto ao fato central. Pergunte-se: "Quais informações precisamos para analisar esse fato?" Por exemplo, para uma venda, você pode precisar de dimensões como tempo, produto, localização e cliente.

- Crie a Tabela Fato:
    - A tabela fato deve conter as métricas principais e as chaves estrangeiras que referenciam as dimensões.

- Crie as Tabelas Dimensão:
    - Para cada dimensão identificada, crie uma tabela que armazene todos os atributos relacionados a essa dimensão.

- Relacionamentos:
    - Defina os relacionamentos entre a tabela fato e as tabelas dimensão. Esses relacionamentos geralmente são muitos-para-um, com a tabela fato tendo múltiplos registros relacionados a um único registro em uma tabela dimensão.

### Exemplo

Imagine que você esteja modelando dados de vendas de um e-commerce:

- Tabela Fato:
    - fato_vendas
        - id_venda
        - id_tempo (Chave Estrangeira)
        - id_produto (Chave Estrangeira)
        - id_cliente (Chave Estrangeira)
        - id_localizacao (Chave Estrangeira)
        - quantidade_vendida
        - valor_total

- Tabelas Dimensão:
    - dim_tempo
        - id_tempo
        - data
        - mês
        - ano
    - dim_produto
        - id_produto
        - nome_produto
        - categoria_produto
    - dim_cliente
        - id_cliente
        - nome_cliente
        - email_cliente
    - dim_localizacao
        - id_localizacao
        - cidade
        - estado
        - país

Esse é um exemplo básico de como a estrutura ficaria em um Star Schema. Com essa estrutura, você pode facilmente consultar os dados para responder perguntas como: "Qual foi o total de vendas por mês?" ou "Qual cliente comprou mais no último ano?"

---