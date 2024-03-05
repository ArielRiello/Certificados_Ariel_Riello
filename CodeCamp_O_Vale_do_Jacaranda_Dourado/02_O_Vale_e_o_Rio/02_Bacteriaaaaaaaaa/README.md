# Desafio: Bactériaaaaaaaa

<img src="https://hermes.dio.me/code_challenge/badge/3a2780f6-89da-4eea-92e1-a0cf0dc8bed4.png" width="200">

Nivel: Básico - Duração: 1h

---

🌱 Sobre o Desafio

Por conta do extrativismo e a presença humana na região, o rio Jacará-Mirim está com níveis altíssimos de plástico em todas as suas formas, em sua maioria originados de descartes irregulares da Oil Corp. Para isso, a coordenadora da expedição Camila (uma ecologista engajada e expert em Java), criou uma ecobarreira com sua equipe. Essa ecobarreira, como a palavra já diz, barra o plástico e o mantém acumulado em uma porção do rio para que depois ele seja coletado e retirado da água.

Felizmente, CleanCoders do Japão descobriram uma bactéria conhecida como Ideonella sakaiensis. Eles confirmaram que essa bactéria possui uma enzima capaz de decompor o plástico: a PETase. Essa enzima é muito eficaz e acaba com o plástico em muito menos tempo em comparação com a decomposição na natureza, que pode levar séculos.

Nesse contexto, o plástico é degradado sempre pela metade a cada dia. Então se temos 1000kg em um dia, no próximo teremos 500kg, no seguinte 250kg e assim por diante. Crie um código que, dependendo da quantidade de plástico, nos diga em quantos dias teremos 1kg ou menos de plástico (viabilizando a coleta manual).

Nota: mais sobre essa bactéria pode ser encontrado nessa matéria da Super Interessante de Dezembro/2022: https://super.abril.com.br/ciencia/o-futuro-do-plastico/

🌅 Entradas e Saídas

A entrada será a quantidade de plástico em quilogramas. A saída deverá ser a quantidade de dias que levará para que essa quantidade de plástico chegue a 1kg ou menos.

🌳 Exemplo

|Entrada|Saída|
|-|-|
|10|Serão necessários 4 dias|
|50|Serão necessários 6 dias|
|78|Serão necessários 7 dias|

---

*Código Base:*

~~~JS
//Desafios JavaScript na DIO têm funções "gets" e "print" acessíveis globalmente:
//- "gets" : lê UMA linha com dado(s) de entrada (inputs) do usuário;
//- "print": imprime um texto de saída (output), pulando linha.

let plastico = parseInt(gets());
let diasNecessarios = 0;

//TODO: Print no console a quantidade de dias que levará para que o plástico chegue
//a 1kg ou menos
~~~

---