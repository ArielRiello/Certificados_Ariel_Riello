
## Granularidade de Dados

A granularidade de dados refere-se ao nível de detalhe ou precisão dos dados armazenados em uma tabela fato em um data warehouse ou sistema de Business Intelligence (BI).

### Principais Aspectos da Granularidade:

- Nível de Detalhe:
    - A granularidade define o quão detalhados são os dados armazenados. Por exemplo, em uma tabela fato de vendas, a granularidade pode ser definida ao nível de transação individual, ao nível diário, ou até mesmo ao nível mensal.

- Decisão de Granularidade:
    - A escolha da granularidade depende das necessidades de análise. Dados mais granulados (maior nível de detalhe) permitem análises mais precisas, mas podem levar a um maior volume de dados e complexidade. Dados menos granulados (menor nível de detalhe) são mais fáceis de gerenciar e podem melhorar o desempenho de consultas, mas oferecem menos flexibilidade analítica.

- Impacto na Modelagem:
    - A granularidade afeta a estrutura do modelo dimensional, a definição das tabelas fato, e o tipo de agregações necessárias. Por exemplo, se a granularidade for diária, a tabela fato armazenará dados agregados por dia, o que simplifica as consultas diárias, mas limita a análise ao nível individual das transações.

### Exemplo:

- Alta Granularidade: Se a tabela fato armazena cada venda individualmente, incluindo data e hora específicas, cliente, produto, etc., a granularidade é alta.
    
- Baixa Granularidade: Se a tabela fato armazena as vendas agregadas por dia ou por mês, sem detalhes de cada transação, a granularidade é baixa.

Escolher a granularidade correta é essencial para equilibrar a necessidade de detalhamento analítico com o desempenho do sistema e o volume de dados.

---