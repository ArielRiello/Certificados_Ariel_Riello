
## Tipos de modelos dimensionais: Start Schema, Snowflake e Constellation

1. Star Schema (Esquema em Estrela)

    - Estrutura: O Star Schema é o modelo dimensional mais simples e mais amplamente usado. Ele consiste em uma única tabela fato central, que armazena as métricas principais (como vendas, transações, etc.), rodeada por tabelas dimensão que descrevem os atributos do fato (como produto, cliente, tempo, localização).
    
    - Vantagens: É fácil de entender e eficiente para consultas de BI (Business Intelligence). As consultas são rápidas, pois as tabelas dimensão são diretamente relacionadas à tabela fato.
    
    - Desvantagens: Pode haver redundância de dados nas tabelas dimensão, o que pode aumentar o tamanho do armazenamento.

2. Snowflake Schema (Esquema em Floco de Neve)

    - Estrutura: O Snowflake Schema é uma extensão do Star Schema, onde as tabelas dimensão são normalizadas (divididas em tabelas menores). Isso resulta em uma estrutura onde as tabelas dimensão podem estar conectadas a outras tabelas menores, criando uma estrutura em forma de floco de neve.
    
    - Vantagens: Reduz a redundância de dados, pois as dimensões são normalizadas. Pode economizar espaço de armazenamento.
    
    - Desvantagens: As consultas podem ser mais complexas e menos eficientes, pois exigem mais junções (joins) entre tabelas.

3. Constellation Schema (Esquema de Constelação)

    - Estrutura: O Constellation Schema, também conhecido como Galaxy Schema, é uma combinação de vários Star Schemas que compartilham tabelas dimensão comuns. Esse modelo é utilizado em cenários onde há múltiplas tabelas fato, cada uma representando um processo diferente, mas que compartilham dimensões semelhantes.
    
    - Vantagens: Permite análise de diferentes processos de negócio em uma única estrutura, sendo mais flexível para cenários complexos.
    
    - Desvantagens: A complexidade do esquema aumenta, tornando a manutenção e as consultas mais desafiadoras.

Cada um desses modelos é adequado para diferentes cenários, dependendo das necessidades específicas de análise e dos requisitos de desempenho do sistema.

---