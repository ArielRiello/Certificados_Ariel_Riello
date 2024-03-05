# Desafio: Network É Tudo!

<img src="https://hermes.dio.me/code_challenge/badge/2304c91a-4da9-405f-b692-eede4ed35f82.png" width="200">

Nivel: Intermediário - Duração: 1h

---

🌱 Sobre o Desafio

Vocês decidem que vão enviar projetos e ideias para a Oil Corp seguir sendo mais sustentável. Uma pessoa do seu grupo diz que vocês receberam um JSON com diversos funcionários da Oil Corp, e seus emails, e que vocês deveriam tentar enviar as ideias para esses endereços. Porém, vocês devem poupar esforços e enviar esses emails somente para cargos de liderança e diretoria.

Crie um código que, faça a analise do JSON procurando por cargos e emails válidos, e print no console o nome, o cargo e seu email válido.

Caso não o algoritmo não encontre nenhum cargo e emprego válido, print no console "Não existem registros encontrados".

OBS: Emails válidos são aqueles que possuem @oilcorp.com.br completo.

🏭 Entradas e Saídas 
As entradas serão: o offset e o limit respectivamente e sempre serão números inteiros positivos. A saída deverá ser todos os nomes, cargos e emails válidos de acordo com os critérios descritos no desafio.

🌳 Exemplo 

**Entrada:**

0 1

**Saída:**

Não existem registros encontrados

---

**Entrada:**

2 4

**Saída:**

Nome: Lenite Longo, Cargo: Diretoria, Email: lenite@oilcorp.com.br

---

*Código Base:*

~~~JS
//Desafios JavaScript na DIO têm funções "gets" e "print" acessíveis globalmente:
//- "gets" : lê UMA linha com dado(s) de entrada (inputs) do usuário;
//- "print": imprime um texto de saída (output), pulando linha.

let offset = parseInt(gets());
let limit = parseInt(gets());
let personFind = false;

const info = [
    {
        nome: "Caique Andrade", 
        idade: 23, 
        cargo: "Trainee", 
        email: "caiqueandrade@hotmail.com", 
        tempoDeEmpresa: "3 meses"
    },
    {
        nome: "Júlio Cesar", 
        idade: 65, 
        cargo: "Diretoria", 
        email: "julio.cesar@oilcorp.com.br", 
        tempoDeEmpresa: "44 anos"
    },
    {
        nome: "Enzo Gaben", 
        idade: 25, 
        cargo: "Auxiliar Administrativo", 
        email: "enzogaben@oilcorp.com", 
        tempoDeEmpresa: "1 ano"
    },
    {
        nome: "Lenite Longo", 
        idade: 70, 
        cargo: "Diretoria", 
        email: "lenite@oilcorp.com.br", 
        tempoDeEmpresa: "50 anos"
    },
    {
        nome: "Renan Oliveira", 
        idade: 35, 
        cargo: "Liderança", 
        email: "renan@oilcorp.com", 
        tempoDeEmpresa: "10 anos"
    },
    {
        nome: "Renato Linhares", 
        idade: 32, 
        cargo: "Liderança", 
        email: "renatolinhares@oilcorp.com.br", 
        tempoDeEmpresa: "5 anos"
    },
    {
        nome: "Emerson Junior", 
        idade: 22, 
        cargo: "Tech lead", 
        email: "emersonjunior@oilcorp.com.br", 
        tempoDeEmpresa: "5 anos"
    },
    {
        nome: "Igor Alves", 
        idade: 26, 
        cargo: "DBA", 
        email: "igor.alves@hotmail.com", 
        tempoDeEmpresa: "Terceirizado"
    },
    {
        nome: "Marcela Kawakame", 
        idade: 28, 
        cargo: "Liderança", 
        email: "marcela@oilcorp.com.br", 
        tempoDeEmpresa: "6 anos"
    },
    {
        nome: "Eric Velloso", 
        idade: 29, 
        cargo: "Diretoria", 
        email: "e.velloso@oilcorp.com.br", 
        tempoDeEmpresa: "11 anos"
    }
];

//TODO: Crie as condições para printar no console o nome, o cargo e o email de cada
//funcionário que se encaixa nas condições do desafio
~~~

---