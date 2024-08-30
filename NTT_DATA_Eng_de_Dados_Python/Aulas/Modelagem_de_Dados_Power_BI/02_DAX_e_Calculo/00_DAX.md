
## DAX

DAX, ou Data Analysis Expressions, é uma linguagem de fórmulas usada no Power BI, Power Pivot e Analysis Services do SQL Server. É projetada para cálculos e análise de dados, permitindo a criação de medidas, colunas calculadas e tabelas calculadas que podem ser usadas para aprofundar a análise dos dados. Aqui estão os principais pontos sobre o DAX:

#### Objetivo do DAX

- Cálculos Avançados: DAX é usada para realizar cálculos complexos que vão além das capacidades das funções básicas do Power BI. Ela permite criar medidas que podem calcular totais, médias ponderadas, percentuais, variações ano a ano, e muito mais.
    
- Expressões e Fórmulas: Semelhante ao Excel, o DAX permite criar expressões que combinam diferentes funções para realizar cálculos dinâmicos e contextuais.

### Componentes do DAX

- Medidas: São fórmulas dinâmicas que realizam cálculos com base nos dados contidos em suas tabelas e são recalculadas automaticamente conforme o contexto de filtro é alterado. Exemplo: SUM(Sales[Amount]) calcula a soma dos valores na coluna "Amount" da tabela "Sales".
    
- Colunas Calculadas: São colunas adicionadas a uma tabela, onde o valor é calculado linha a linha usando uma fórmula DAX. Exemplo: Sales[Total] = Sales[Quantity] * Sales[Price].
    
- Tabelas Calculadas: Permitem criar novas tabelas derivadas dos dados existentes usando fórmulas DAX. Exemplo: SUMMARIZE(Sales, Sales[Year], "Total Sales", SUM(Sales[Amount])) cria uma nova tabela que resume as vendas por ano.

### Principais Funções do DAX

- Agregação: Funções como SUM, AVERAGE, MIN, MAX, COUNT, etc., que calculam valores agregados.
    
- Inteligência Temporal: Funções como DATESYTD, TOTALYTD, PREVIOUSYEAR, SAMEPERIODLASTYEAR, que facilitam cálculos de análises temporais, como ano até a data (YTD) e comparações de períodos.
    
- Manipulação de Texto: Funções como CONCATENATE, LEFT, RIGHT, SEARCH, que permitem manipular e combinar strings de texto.
    
- Lógica: Funções como IF, SWITCH, AND, OR, que permitem a criação de cálculos condicionais.
    Relacionamento: Funções como RELATED, RELATEDTABLE, LOOKUPVALUE, que permitem acessar e utilizar dados de tabelas relacionadas.

### Contexto no DAX

- Contexto de Linha: Refere-se ao valor individual de uma linha em uma coluna calculada. Ele avalia expressões linha por linha.
    
- Contexto de Filtro: Refere-se ao subconjunto de dados que está sendo considerado em uma medida ou cálculo, determinado pelos filtros aplicados na visualização ou no relatório.

### Diferenças entre DAX e Excel

- Contexto de Cálculo: Diferente do Excel, onde as fórmulas operam no nível da célula, DAX opera no nível do conjunto de dados, levando em consideração o contexto dos dados.
    
- Relatórios Dinâmicos: No DAX, as medidas são recalculadas automaticamente com base nos filtros e seleções feitas no relatório, tornando os resultados dinâmicos e dependentes do contexto.

### Aplicações Práticas

- Análise de Negócios: DAX é fundamental para criar relatórios e dashboards no Power BI que permitem aos usuários analisar dados com profundidade, como comparações de desempenho, análise de tendências e projeções futuras.
    
- Modelagem de Dados: É usado para criar cálculos que complementam a modelagem de dados no Power BI, agregando camadas de inteligência e automação aos dados.

---

DAX é uma ferramenta poderosa no Power BI que permite a realização de análises avançadas e detalhadas dos dados, sendo essencial para criar relatórios dinâmicos e altamente personalizáveis.

---