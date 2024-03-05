# Desafio: Isso Não Está Cheirando Bem... Bora Filtrar!

<img src="https://hermes.dio.me/code_challenge/badge/2304c91a-4da9-405f-b692-eede4ed35f82.png" width="200">

Nivel: Intermediário - Duração: 1h

---

🌱 Sobre o Desafio

A Oil Corp abriu o jogo e entregou para vocês uma lista contendo vários gases que eles liberam durante a extração de óleo. Alguns desses gases são extremamente prejudiciais para a camada de ozônio e para a natureza local como: NO2, SO2, CO e FHO.

Durante a extração os gases saem misturados. Crie um código que, de acordo com a lista, verifique se há pelo menos UM desses gases. Se não houver, imprima que deverá passar por um Filtro Simples. Se houver, imprima no console que deverá passar por um Filtro Especial e especifique qual gás.

🏭 Entradas e Saídas 

A entrada será uma lista de listas com as moléculas que devem ser analisadas. A saída deve ser qual filtro deve ser utilizado para filtrar. Caso tenha uma dessas moléculas prejudiciais, a saída deve ser um filtro específico para a molécula X.

Nesse nosso desafio se houver a molécula prejudicial na entrada será apenas UMA.

🌳 Exemplo 

**Entrada:**

CO2, OH
Br2, NH3
HCl, HCN, O2

**Saída:**

Filtro Simples

---

**Entrada:**

CO2, CO
NH3, Cl2

**Saída:**

Filtro Específico para a Molécula CO

---

*Código Base:*

~~~JS
//Desafios JavaScript na DIO têm funções "gets" e "print" acessíveis globalmente:
//- "gets" : lê UMA linha com dado(s) de entrada (inputs) do usuário;
//- "print": imprime um texto de saída (output), pulando linha.

let lista1 = gets().split(', ');
let lista2 = gets().split(', ');
let lista3 = gets().split(', ')

let arr = [lista1, lista2, lista3]

let qualFiltro = false;
let qualMolecula;

//TODO: Print no console qual filtro deve ser utilizado de acordo com as moléculas prejudiciais
//avaliadas no teste.
~~~

---