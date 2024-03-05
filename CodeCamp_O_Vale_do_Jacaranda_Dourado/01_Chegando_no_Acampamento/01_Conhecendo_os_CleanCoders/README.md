# Desafio: Conhecendo os CleanCoders

🌱 Sobre o Desafio 
Buscando planejar as ações para conter a Oil Corp, um acampamento foi criado e muitos CleanCoders (inclusive novos adeptos da causa) estão chegando. Com isso, para faciliar a comunicação e interação, precisamos imprimir cartões de identificação para todas as pessoas.

Crie um código que com três entradas (NOME, SOBRENOME e ID) que imprima essas informações no seguinte padrão: "Nome: NOME SOBRENOME ID: ID"

Venilton, um CleanCoder experiente, compartilhou uma dica bem útil. Ele disse que é possível utilizar o conceito de interpolação de strings para facilitar a impressão de textos concatenados à variáveis. Para utilizar basta fazer assim:

print(`String e ${variavel}`);
⛺ Entradas e Saídas
As entradas serão: o nome, o sobrenome e o ID de cada CleanCoder. A saída deverá ser essas três variáveis concatenadas em uma única String.

🌳 Exemplo

~~~
Entrada 

Kawan
Anthony
22       	

Saída

Nome: Kawan Anthony ID: 22      
~~~

~~~
Entrada

Renan
Oliveira
98       	

Saída

Nome: Renan Oliveira ID: 98
~~~

~~~
Entrada

Marjory
 Santos
204                    	

Saída

Nome: Marjory Santos ID: 204
~~~

---

*Código Base*

~~~js
//Desafios JavaScript na DIO têm funções "gets" e "print" acessíveis globalmente:
//- "gets" : lê UMA linha com dado(s) de entrada (inputs) do usuário;
//- "print": imprime um texto de saída (output), pulando linha.

let nome = gets()
let sobrenome = gets();
let id = parseInt(gets());

//TODO: Print no console as três variáveis de acordo com a saída esperada
~~~

---