# Linguagem de programação R

R é uma linguagem de programação e ambiente de software livre amplamente utilizado para análise estatística, visualização de dados e computação científica. Desenvolvida inicialmente por Ross Ihaka e Robert Gentleman na Universidade de Auckland, na Nova Zelândia, a linguagem R tornou-se uma ferramenta indispensável para estatísticos, cientistas de dados e pesquisadores devido à sua expressividade, flexibilidade e abrangente ecossistema de pacotes.

* Estruturas de Dados: 
    * R suporta várias estruturas de dados fundamentais, incluindo vetores (arrays unidimensionais), matrizes (arrays multidimensionais), data frames (tabelas para armazenar dados de tipos variados), e listas (coleções ordenadas de objetos que podem ter diferentes tipos).

* Funções e Pacotes:
    * R é conhecida pela sua vasta coleção de funções internas que facilitam a manipulação de dados, cálculos estatísticos e a criação de gráficos. Além disso, a linguagem é extensível através de pacotes, que são conjuntos de funções, dados e código compilado que expandem as capacidades do R para áreas específicas. O Comprehensive R Archive Network (CRAN) hospeda milhares desses pacotes, cobrindo uma ampla gama de funcionalidades.

* Ambiente de Desenvolvimento: 
    * Embora R possa ser utilizado em diversos ambientes de desenvolvimento, o RStudio é um dos mais populares IDEs (Ambiente de Desenvolvimento Integrado) para R, oferecendo uma interface amigável que facilita a escrita de código, execução de análises e visualização de dados.

* Gráficos e Visualização: 
    * R possui poderosas capacidades de visualização de dados, com sistemas de gráficos base e avançados (como o ggplot2) permitindo a criação de representações visuais sofisticadas e personalizadas de dados estatísticos.

* Análise Estatística e Modelagem: 
    * No coração do R está sua capacidade de realizar análises estatísticas complexas. Isso inclui desde procedimentos estatísticos básicos, como testes de hipóteses e análises exploratórias, até modelagem estatística avançada, como regressão, análise de séries temporais e aprendizado de máquina.

* Comunidade e Suporte: 
    * R beneficia-se de uma comunidade global ativa e engajada, que contribui para o desenvolvimento contínuo da linguagem, oferece suporte através de fóruns e promove eventos educacionais, como workshops e conferências.


## Interpretada

Ser uma linguagem interpretada significa que o código escrito em R é executado diretamente, linha por linha, por um interpretador. Diferentemente das linguagens compiladas, onde o código fonte é primeiramente transformado em um formato de máquina específico antes de ser executado, as linguagens interpretadas permitem uma abordagem mais dinâmica e interativa à programação. Esta característica traz várias vantagens para o R:

* Interatividade: 
    * R suporta um estilo de desenvolvimento interativo, onde os usuários podem digitar comandos e receber feedback imediato. Isso é particularmente útil para análise exploratória de dados e pesquisa científica, onde a capacidade de experimentar rapidamente com diferentes métodos é valiosa.
    
* Flexibilidade: 
    * A natureza interpretada do R facilita a experimentação e a prototipagem rápida. Os usuários podem testar novas ideias ou ajustar suas análises sem a necessidade de um ciclo de compilação.
    
* Portabilidade: 
    * Códigos em R podem ser executados em diferentes plataformas sem modificações. Isso contrasta com linguagens compiladas, que podem exigir compilação específica para cada plataforma.

## Case-Sensitive

Ser "case-sensitive" significa que o R diferencia letras maiúsculas de minúsculas. Portanto, identificadores como variáveis, nomes de funções e outros símbolos no código devem ser usados com a exata combinação de maiúsculas e minúsculas com que foram definidos. Por exemplo, resultado, Resultado e RESULTADO seriam considerados três identificadores distintos em R. Essa característica tem implicações importantes:

* Precisão na Codificação: 
    * Os usuários devem ser precisos ao referenciar objetos ou funções existentes para evitar erros de "objeto não encontrado".
    
* Convenções de Nomenclatura: 
    * Embora o R seja case-sensitive, a comunidade adota convenções de nomenclatura para ajudar a manter o código legível e consistente, como usar nomes de variáveis em minúsculas e funções em camelCase ou underscore_separated.
    
* Atenção aos Detalhes: 
    * Programadores devem estar atentos à capitalização para garantir que o código seja interpretado corretamente pelo R.


## Tudo é um Objeto

Em R, tudo é tratado como um objeto. Isso inclui não apenas estruturas de dados como vetores, matrizes e data frames, mas também funções e até mesmo expressões de controle de fluxo. Essa abordagem orientada a objetos permite uma manipulação consistente e flexível de estruturas de dados e operações, facilitando a programação e a análise de dados complexa.


## O Operador "<-"

O operador <- é usado em R para atribuição, significando que o valor à direita do operador é atribuído ao objeto à esquerda. Embora o sinal de igual (=) também possa ser usado para atribuição, o <- é preferencial no estilo de codificação R por sua clareza visual e tradição. Por exemplo, x <- 10 atribui o valor 10 à variável x.

Datasets Embutidos

R possui uma variedade de datasets embutidos, que são extremamente úteis para testar algoritmos, realizar análises exploratórias e ensinar conceitos de estatística e ciência de dados. Alguns desses conjuntos de dados incluem:

* mtcars: 
    * Dados de consumo de combustível do Motor Trend US magazine, contendo informações de diversos modelos de carros.
    
* iris: 
    * O famoso dataset Iris, que contém medidas das variáveis de comprimento e largura da sépala e da pétala de 150 amostras de íris de três espécies diferentes.
    
* airquality: 
    * Dados diários sobre a qualidade do ar de Nova Iorque, maio a setembro de 1973.

## Constantes Matemáticas e Estatísticas

Além do valor de pi, R inclui outras constantes úteis:

* Inf:
    * Representa o infinito positivo. Útil em contextos matemáticos onde é necessário representar um valor maior do que qualquer número real.

* -Inf:
    * Representa o infinito negativo.

* NaN: 
    * Significa "Not a Number". É um valor utilizado para representar um resultado indefinido ou que não pode ser expresso como um número real.

* NA:
    * Representa um valor "Não Disponível" ou "Missing". É usado em R para indicar a ausência de um valor em um vetor ou outro objeto.

## Funções Matemáticas e Estatísticas Básicas

R também oferece uma ampla gama de funções matemáticas e estatísticas básicas pré-definidas, tais como:

* mean(): Calcula a média aritmética.

* median(): Determina a mediana.

* sd(): Calcula o desvio padrão.

* var(): Calcula a variância.

* sum(): Soma os elementos.

* min() e max(): Determinam o valor mínimo e máximo de um conjunto de dados, respectivamente.

## Funções de Geração de Dados

R inclui funções que permitem gerar dados de acordo com distribuições específicas, o que é especialmente útil para simulações e análises estatísticas. Algumas dessas funções são:

* rnorm(): Gera números aleatórios de uma distribuição normal.

* runif(): Gera números aleatórios de uma distribuição uniforme.

* rbinom(): Gera números aleatórios de uma distribuição binomial.

Estes são apenas alguns exemplos dos muitos objetos e funções pré-definidos disponíveis em R, demonstrando a riqueza e a versatilidade da linguagem para facilitar o trabalho com análise de dados e estatística.