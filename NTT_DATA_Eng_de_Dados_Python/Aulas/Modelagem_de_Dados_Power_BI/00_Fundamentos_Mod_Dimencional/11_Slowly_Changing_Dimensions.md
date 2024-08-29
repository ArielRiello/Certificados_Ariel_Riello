
## Slowly Changing Dimensions (SCD)

Slowly Changing Dimensions (SCD) ou Dimensões de Mudança Lenta referem-se a um conceito de modelagem de dados em data warehouses, onde as informações em tabelas dimensão mudam ao longo do tempo. As SCDs tratam de como essas mudanças são gerenciadas para garantir que os dados históricos sejam precisos e relevantes.

### Tipos de SCD

Existem vários tipos de SCD, cada um com uma abordagem diferente para lidar com as mudanças nos dados de uma dimensão:

- SCD Tipo 1: Substituição Simples
    - Descrição: Quando um valor em uma dimensão muda, o valor antigo é simplesmente substituído pelo novo. Não há histórico mantido das alterações.
    
    - Exemplo: Se o nome de um cliente for alterado, o novo nome substitui o antigo na tabela dimensão.
        Vantagens: Simplicidade e menor espaço de armazenamento.
        Desvantagens: Perde-se o histórico das mudanças.

- SCD Tipo 2: Rastreio de Histórico Completo
    - Descrição: Toda vez que uma mudança ocorre em um atributo da dimensão, uma nova linha é inserida na tabela dimensão com o novo valor. A linha antiga é mantida para preservar o histórico.
        
    - Exemplo: Se o endereço de um cliente mudar, uma nova linha será inserida na tabela com o novo endereço, enquanto a linha antiga permanece para manter o histórico.
        
    - Vantagens: Mantém um histórico completo de mudanças, permitindo análises temporais precisas.
        
    - Desvantagens: Aumenta o tamanho da tabela dimensão e a complexidade das consultas.

- SCD Tipo 3: Atributo Adicional
    - Descrição: Um número limitado de alterações é rastreado. Quando ocorre uma mudança, um novo atributo é adicionado à tabela para armazenar o valor anterior, enquanto o atributo original armazena o valor atual.
    
    - Exemplo: Se um cliente mudar de cidade, a tabela pode ter colunas como cidade_atual e cidade_anterior.
    
    - Vantagens: Permite a visualização do valor anterior e atual sem aumentar muito o tamanho da tabela.
        
    - Desvantagens: Não rastreia mudanças além de um número limitado de versões (geralmente, apenas uma mudança é armazenada).

- Outros Tipos:
    - SCD Tipo 4: Usa uma tabela de histórico separada para armazenar as versões anteriores dos registros.
        
    - SCD Tipo 6: Uma combinação dos tipos 1, 2 e 3, onde as mudanças são rastreadas de maneira mais flexível, geralmente combinando uma substituição simples, histórico completo e um atributo adicional.

### Exemplos de Uso:

- SCD Tipo 1: Ideal quando o histórico das alterações não é relevante e a precisão atual é o único requisito.
    
- SCD Tipo 2: Usado quando é importante preservar o histórico para relatórios e análises ao longo do tempo.
    
- SCD Tipo 3: Útil quando apenas a mudança mais recente precisa ser rastreada junto com o valor atual.

A escolha do tipo de SCD depende dos requisitos específicos de negócio e das necessidades de análise histórica dentro do data warehouse.

---