
## Funções X

As Funções X no Power BI são um conjunto de funções iterativas do DAX que permitem aplicar um cálculo a cada linha de uma tabela ou a cada elemento de uma coleção e, em seguida, agregam os resultados. Essas funções são extremamente poderosas para cálculos complexos, pois permitem personalizar operações linha a linha em um conjunto de dados.

### Principais Funções X

Aqui estão algumas das funções X mais usadas e seus usos:

- **SUMX**:
    - **Descrição**: 
        ~~~
        Calcula a soma de uma expressão avaliada para cada linha de uma tabela.
        ~~~

    - **Sintaxe**:
        ~~~DAX
        SUMX(tabela, expressão)
        ~~~

    - **Exemplo**:
        ~~~DAX
        Total Vendas = SUMX(Sales, Sales[Quantidade] * Sales[Preço])
        ~~~
        *Esse exemplo multiplica a Quantidade pelo Preço para cada linha da tabela Sales e, em seguida, soma esses valores.*

- **AVERAGEX**:
    - **Descrição**: 
        ~~~
        Calcula a média de uma expressão avaliada para cada linha de uma tabela.
        ~~~

    - **Sintaxe**:
        ~~~DAX
        AVERAGEX(tabela, expressão)
        ~~~

    - **Exemplo**:
        ~~~DAX
        Média de Vendas = AVERAGEX(Sales, Sales[Quantidade] * Sales[Preço])
        ~~~
        *Calcula a média do total de vendas por linha.*

- **MINX**:
    - **Descrição**: 
        ~~~
        Retorna o menor valor de uma expressão avaliada para cada linha de uma tabela.
        ~~~

    - **Sintaxe**:
        ~~~DAX
        MINX(tabela, expressão)
        ~~~

    - **Exemplo**:
        ~~~DAX
        Menor Preço = MINX(Products, Products[Preço])
        ~~~
        *Encontra o menor preço na tabela Products.*

- **MAXX**:
    - **Descrição**: 
        ~~~
        Retorna o maior valor de uma expressão avaliada para cada linha de uma tabela.
        ~~~

    - **Sintaxe**:
        ~~~DAX
        MAXX(tabela, expressão)
        ~~~

    - **Exemplo**:
        ~~~DAX
        Maior Preço = MAXX(Products, Products[Preço])
        ~~~
        *Encontra o maior preço na tabela Products.*

- **COUNTX**:
    - **Descrição**: 
        ~~~
        Conta o número de valores não nulos retornados por uma expressão para cada linha de uma tabela.
        ~~~

    - **Sintaxe**:
        ~~~DAX
        COUNTX(tabela, expressão)
        ~~~

    - **Exemplo**:
        ~~~DAX
        Contagem de Produtos Vendidos = COUNTX(Sales, Sales[ProdutoID])
        ~~~
        *Conta o número de produtos vendidos (considerando IDs de produtos não nulos).*

- **RANKX**:
    - **Descrição**: 
        ~~~
        Retorna a classificação de um valor em uma tabela, aplicando uma expressão a cada linha da tabela e classificando os resultados.
        ~~~

    - **Sintaxe**:
        ~~~DAX
        RANKX(tabela, expressão, [valor], [ordem])
        ~~~

    - **Exemplo**:
        ~~~DAX
        Classificação de Vendas = RANKX(ALL(Sales), Sales[Total Vendas], , DESC)
        ~~~
        *Classifica os totais de vendas em ordem decrescente.*

### Diferença entre Funções X e Funções Tradicionais

- **Iteração**: 
    - As funções X iteram sobre cada linha ou elemento de uma tabela, aplicando uma expressão. As funções tradicionais (como SUM, AVERAGE, etc.) simplesmente agregam os valores diretamente, sem considerar cada linha individualmente.

- **Contexto de Linha**:
    - As funções X podem acessar o contexto de cada linha da tabela, permitindo cálculos mais dinâmicos e detalhados. Isso é essencial quando você precisa realizar cálculos complexos, como multiplicar valores em colunas diferentes e, em seguida, somá-los.

- **Flexibilidade**:
    - As funções X oferecem uma grande flexibilidade porque permitem a execução de cálculos personalizados em cada linha antes de agregá-los. Isso as torna ideais para situações onde a agregação direta não é suficiente.

### Quando Usar Funções X

- **Cálculos Personalizados**:
    - Quando você precisa aplicar um cálculo específico a cada linha de uma tabela e depois agregá-lo.

- **Agregações Condicionais**:
    - Quando os cálculos dependem de condições específicas para cada linha.

- **Modelagem Complexa de Dados**:
    - Em cenários onde o cálculo deve levar em consideração múltiplas colunas ou critérios para cada linha de dados.

---

As Funções X são ferramentas essenciais para realizar cálculos mais complexos e detalhados no Power BI, permitindo análises mais refinadas e precisas.

---