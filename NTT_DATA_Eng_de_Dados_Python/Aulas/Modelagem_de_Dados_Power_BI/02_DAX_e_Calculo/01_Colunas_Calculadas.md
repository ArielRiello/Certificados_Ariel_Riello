
## Colunas Calculadas

Colunas Calculadas no Power BI são colunas que você cria manualmente em uma tabela, utilizando expressões DAX (Data Analysis Expressions). Elas são adicionadas ao modelo de dados e os valores dessas colunas são calculados linha por linha, com base em outras colunas da tabela ou em expressões DAX.
Características Principais das Colunas Calculadas:

### Cálculo Linha por Linha:

- Diferente das medidas, que calculam valores com base no contexto de filtros e agregação de dados, as colunas calculadas realizam cálculos em cada linha da tabela. O valor da coluna calculada é armazenado para cada linha, e não é alterado pelo contexto de filtro.

### Utilização de DAX:
- As colunas calculadas são definidas usando fórmulas DAX. Essas fórmulas podem incluir funções matemáticas, de texto, lógicas, entre outras, para criar novos dados derivados das colunas existentes.

### Armazenamento no Modelo:
- Os valores das colunas calculadas são armazenados fisicamente no modelo de dados do Power BI. Isso pode aumentar o tamanho do arquivo do modelo, especialmente se a tabela for grande.

### Exemplo de Uso:

Se você tiver uma tabela de vendas com colunas para Quantidade e Preço, você pode criar uma coluna calculada chamada Total de Vendas que multiplica essas duas colunas:

~~~DAX
Total de Vendas = Sales[Quantidade] * Sales[Preço]
~~~

Agora, essa coluna estará disponível em toda a tabela e pode ser usada em visualizações ou para cálculos adicionais.

### Diferença em Relação às Medidas:

- Colunas Calculadas: Avaliam expressões para cada linha da tabela e o valor é fixo, a menos que os dados subjacentes mudem.

- Medidas: Calculam resultados com base no contexto de agregação e filtragem, e os valores podem mudar dependendo dos filtros aplicados no relatório.

### Uso Comum:
- Derivação de Dados: Criar novos campos que combinam ou transformam dados de outras colunas.
        
- Segmentação e Agrupamento: Criar categorias ou grupos com base em condições (por exemplo, uma coluna calculada que classifica as vendas como "Baixa", "Média" ou "Alta").
        
- Preparação de Dados: Ajustar e formatar dados para facilitar a análise e a visualização.

### Quando Usar Colunas Calculadas:

- Pré-processamento de Dados: Quando você precisa de um valor derivado que deve ser armazenado no modelo e usado em diferentes visualizações, independentemente do contexto de filtros.

- Cálculos Linha a Linha: Quando o cálculo depende diretamente dos valores de outras colunas na mesma linha.

### Considerações:

- Performance: Como os valores das colunas calculadas são armazenados no modelo, usar muitas colunas calculadas pode aumentar o tamanho do modelo e impactar a performance, especialmente em tabelas grandes.
    
- Necessidade de Atualização: As colunas calculadas são recalculadas apenas quando os dados subjacentes são atualizados, ao contrário das medidas, que são recalculadas dinamicamente.

---

Em resumo, as colunas calculadas são uma poderosa ferramenta no Power BI para enriquecer seu modelo de dados com novas informações derivadas, permitindo análises mais detalhadas e específicas.

---