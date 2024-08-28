
## Chave Artificial

Uma chave artificial (também conhecida como chave substituta ou surrogate key) é um identificador único gerado artificialmente para uma linha (registro) em uma tabela de banco de dados. Ela é usada como a chave primária para identificar de forma exclusiva cada registro dentro da tabela.

### Características da Chave Artificial:

- Gerada Artificialmente:
    - Diferente de uma chave natural (que é derivada dos dados existentes, como um CPF ou número de documento), uma chave artificial não tem nenhum significado no mundo real e é criada apenas para uso interno no banco de dados.

- Valores Únicos:
    - A chave artificial é projetada para ser única em toda a tabela, garantindo que cada registro possa ser identificado de maneira distinta.

- Exemplos Comuns:
    - Números sequenciais (como um autoincremento), identificadores UUID, ou outras sequências geradas pelo sistema.

- Vantagens:
    - Simplicidade: Facilita a manutenção do banco de dados, pois não depende dos dados reais, que podem mudar. Por exemplo, se uma chave natural fosse um nome de usuário, uma mudança no nome do usuário exigiria a atualização da chave em todas as tabelas relacionadas.
        
    - Independência: É independente dos dados de negócio, o que significa que mudanças nos atributos do negócio não afetam a chave.
        Consistência: Permite manter a consistência ao longo do tempo e entre diferentes sistemas, já que o identificador não está sujeito a alterações no mundo real.

- Desvantagens:
    - Sem Significado: Como a chave artificial não tem significado no mundo real, ela não pode ser usada para qualquer interpretação dos dados sem uma referência cruzada.

### Exemplo:

- Tabela de Clientes:
    - Chave Artificial: id_cliente (número sequencial gerado automaticamente, como 1, 2, 3...)
    
    - Chave Natural (alternativa): CPF do cliente.

Neste exemplo, id_cliente é a chave artificial que identifica unicamente cada cliente na tabela, enquanto o CPF poderia ser uma chave natural, mas não é usada como tal devido a possíveis mudanças ou inconsistências.

Em sistemas de data warehouse e modelagem dimensional, é comum usar chaves artificiais para garantir a integridade e a flexibilidade dos dados.

---