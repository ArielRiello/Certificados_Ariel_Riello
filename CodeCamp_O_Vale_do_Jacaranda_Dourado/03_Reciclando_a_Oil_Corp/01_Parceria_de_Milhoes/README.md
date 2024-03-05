# Desafio: Parceria de Milhões, Para a Natureza ;)

<img src="https://hermes.dio.me/code_challenge/badge/2304c91a-4da9-405f-b692-eede4ed35f82.png" width="200">

Nivel: Intermediário - Duração: 1h

---

🌱 Sobre o Desafio

Após vocês promoverem diversas atividades a favor da natureza, a liderança e a diretoria da Oil Corp convidaram vocês para os ajudarem a preservar a natureza e a serem uma empresa sustentável. Para isso, eles precisam de ajuda para criar o algoritmo que direciona os resíduos da água para a estação de tratamento correta antes de ser descartada no rio Jacará-Mirim.

Via de regra, as moléculas que possuem até 5 caracteres passam pelo Filtro Normal, as que possuem até 10 caracteres passam pelo Filtro Específico e as que possuem mais que 10 caracteres passam pelo Filtro Duplo Especifico. Essas moléculas estão misturadas nos resíduos, se houver ao menos uma que tenha o número específico de caracteres esse resíduo já deve passar pelo filtro correto.

Crie um código que implemente essas regras e imprima o filtro adequado para cada molécula:

* Se <= 5 - Imprimir "Filtro Normal";
* Se > 5 e <= 10 - Imprimir "Filtro Específico";
* Se > 10 - Imprimir "Filtro Duplo Específico";

🏭 Entradas e Saídas 

As entradas serão listas contendo as moléculas contidas na água analisada. A saída deverá ser se o filtro utilizado deve ser o "Filtro Normal", o "Filtro Específico" ou o "Filtro Duplo Específico".

🌳 Exemplo 
|Entrada|Saída|
|-|-|
|HNO, H3ON, HN3FO|O filtro deve ser: Filtro Normal|
|HNO3FOH, H3O, FOH3|O filtro deve ser: Filtro Específico|

---

*Codigo Base:*

~~~JS
//Desafios JavaScript na DIO têm funções "gets" e "print" acessíveis globalmente:
//- "gets" : lê UMA linha com dado(s) de entrada (inputs) do usuário;
//- "print": imprime um texto de saída (output), pulando linha.

const arr = gets().split(', ')
let qualFiltro = 0;

//TODO: Print no console qual filtro deve ser utilizado de acordo com as moléculas na entrada
~~~

---