
## Colunas Personalizadas

No Power BI, Colunas Personalizadas referem-se a colunas que você cria manualmente em uma tabela para adicionar novos dados ou transformar dados existentes de maneira personalizada. Assim como as colunas calculadas, as colunas personalizadas são criadas usando expressões DAX, mas a terminologia "colunas personalizadas" é frequentemente usada no contexto de transformação de dados na Power Query Editor, a ferramenta de preparação de dados do Power BI.

### Criação de Colunas Personalizadas:

- Fórmula M: Diferente das colunas calculadas no modelo de dados, que usam DAX, as colunas personalizadas no Power Query são criadas usando a linguagem de fórmulas "M". Isso permite que você realize transformações complexas de dados diretamente na etapa de importação.
    
- Interface de Usuário: Você pode criar uma coluna personalizada através da interface do Power Query Editor, que fornece uma caixa de diálogo onde você pode inserir a fórmula M para definir a lógica da nova coluna.

### Processo para Criar Colunas Personalizadas:

- Acessando o Power Query Editor: No Power BI Desktop, vá até a guia "Transformar Dados" para abrir o Power Query Editor.
    
- Adicionar Coluna Personalizada: Clique em "Adicionar Coluna" > "Coluna Personalizada". Isso abrirá uma janela onde você pode inserir uma fórmula para calcular a nova coluna.

- Escrever Fórmula: Na janela de coluna personalizada, você pode escrever fórmulas que combinam, transformam, ou criam novos dados com base nas colunas existentes. Por exemplo:

~~~M
= [Quantidade] * [Preço]
~~~

*Essa fórmula cria uma nova coluna personalizada que multiplica as colunas Quantidade e Preço.*

### Exemplos de Uso:

- Concatenar Textos:

~~~m
= [Nome] & " " & [Sobrenome]
~~~

*Essa fórmula combina as colunas Nome e Sobrenome em uma nova coluna com o nome completo.*

- Cálculos Condicionais:

~~~m
= if [Vendas] > 1000 then "Alta" else "Baixa"
~~~

*Essa fórmula classifica as vendas como "Alta" ou "Baixa" com base em um valor limite.*

- Transformação de Datas:

~~~m
= Date.ToText([Data], "dd-MM-yyyy")
~~~

*Converte uma data para um formato específico de texto.*

### Vantagens das Colunas Personalizadas:

- Transformação de Dados Antes da Carga: As colunas personalizadas no Power Query permitem que você transforme e limpe seus dados antes de carregá-los no modelo de dados do Power BI, resultando em um modelo mais eficiente e focado.
    
- Fácil Integração: Após a criação, essas colunas se integram ao restante do modelo de dados, permitindo que você use os dados transformados em visualizações, relatórios e análises.

### Diferenças em Relação às Colunas Calculadas:

- Localização e Momento de Criação: Colunas personalizadas são criadas durante a etapa de transformação de dados no Power Query, antes de os dados serem carregados no modelo. Já as colunas calculadas são criadas no modelo de dados após os dados serem carregados.
    
- Linguagem de Fórmulas: Colunas personalizadas usam a linguagem M, enquanto as colunas calculadas usam DAX.
    
- Impacto no Modelo: Como colunas personalizadas são calculadas e aplicadas antes do carregamento dos dados, elas não afetam o desempenho do modelo de dados tanto quanto as colunas calculadas.

### Quando Usar Colunas Personalizadas:

- Pré-processamento: Quando você precisa limpar, transformar ou criar dados antes de carregá-los no modelo de dados.

- Transformações Complexas: Para realizar cálculos ou manipulações de dados que são mais adequadamente tratados durante o processo de ETL.

---

As colunas personalizadas no Power Query são uma ferramenta poderosa para preparar e transformar seus dados, garantindo que eles estejam no formato necessário para análises e relatórios eficazes no Power BI.

---