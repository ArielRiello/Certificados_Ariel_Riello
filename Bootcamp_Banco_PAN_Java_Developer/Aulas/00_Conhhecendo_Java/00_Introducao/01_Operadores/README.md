## Operadores

*Símbolos especiais que tem um significado próprio para a linguagem e estão associados a determinadas operações.*



### Atribuição

 *Representado pelo símbolo de igualdade "="*

 *Utilizado para definir o valor inicial ou sobrescrever o valor de uma variável.*

##### Exemplos:

~~~java
String nome = "Ariel";
int idade = 30;
double peso = 127.5;
char sexo = 'M';
boolean doadorOrgao = false;
Date dataNascimento = new Date();
~~~



### Aritméticos

*Utilizado para realizar operações matemáticas entre valores numéricos, podendo se tornar ou não uma expressão mais complexa.*

* **" + "** (adição)
* **" - "** (subtração)
* **" * " **(multiplicação)
* **" / "** (divisão)

##### Exemplos:

~~~java
double soma = 10.5 + 15.7;
int subtracao = 113 - 25;
int multiplicacao = 20 * 7;
int divisao = 15 / 3;
int modulo = 18 % 3;
double resultado = (10 * 7) + (20 / 4);
~~~

**OBS:** *Operador de adição (+), quando utilizado em variáveis do tipo texto, realizará a "concatenação de textos".*

~~~java
String nomeCompleto = "Ariel" + " " + "Riello";

// resultado Ariel Riello
~~~



### Unários

*Esses operadores são aplicados juntamente com um outro operador aritmético.*

*Eles realizam alguns trabalhos básicos como incrementar, decrementar, inverter valores numéricos e booleanos.*

* **" + " Valor positivo** - números são positivos sem esse operador explicitamente.

* **" - " Valor negativo** - nega um número ou expressão aritmética.

* **" ++ " Incremento de valor** - incrementa o valor em 1 unidade.

* **" -- " Decremento de valor** - decrementa o valor em 1 unidade.

* **" ! " Lógico de negação** - nega o valor de uma expressão booleana.

##### Exemplos:

*Exibe a variável **numero*** com seu valor negativo, mas não altera ele.

~~~java
int numero = 5;
System.out.println(- numero);
~~~



*Altera o valor da variável **numero** para negativo, até outra alteração ser feita.*

~~~java
int numero = 5;
numero = - numero;
~~~



*Não consegue alterar o valor para valor positivo, porque + é uma expressão aritmética*

~~~java
int numero = 5;
numero = + numero;

// Forma utilizada para alterar o valor da variável para positivo
int numero = 5;
numero = numero * -1;
~~~



*Adiciona +1 ao valor de numero.*

~~~java
numero = numero + 1;

// Forma simplificada
numero++;
~~~



### Ternários

*O Operador de Condição Ternária é uma forma resumida para definir uma condição e escolher por um dentre dois valores. Você deve pensar numa condição ternária como se fosse uma condição IF normal, porém de uma forma em que toda a sua estrutura estará escrita numa única linha.*

*Representado pelos símbolos **?** e **:***

**<Expressão Condicional> ? <Caso condição seja true> : <Caso condição seja false>**

##### Exemplo:

~~~java
int a, b;
a = 5;
b = 6;

if (a == b)
	resultado = "Verdadeiro";
else
	resultado = "falso";

// Usando Operadores Ternários:
String resultado = a == b ? "Verdadeiro" : "Falso";
~~~



### Relacionais

*Os operadores relacionais avaliam a relação entre duas variáveis ou expressões. Neste caso, mais precisamente, definem se o operando à esquerda é igual, diferente, menor, menor ou igual, maior, maior ou igual ao da direita, retornando um valor booleano como resultado.*

* **==** Quando desejamos verificar se uma variável é **IGUAL A** outra.*

* **!=** Quando desejamos verificar se uma variável é **DIFERENTE** da outra.*

* **> ** Quando desejamos verificar se uma variável é **MAIOR QUE** a outra.*

* **>=** Quando desejamos verificar se uma variável é **MAIOR OU IGUAL** a outra.*

* **<** Quando desejamos verificar se uma variável é **MENOR QUE** a outra.*

* **<=** Quando desejamos verificar se uma variável é **MENOR OU IGUAL** a outra.*

##### Exemplos:

*Compara se o valor da variável **numero1** é **igual** ao valor da variável **numero2**.*

*Retorna **true** se condição igual a **verdadeira** e **false** se condição igual a **falsa**.*

~~~java
int numero1 = 1;
int numero2 = 2;

boolean simNao numero1 == numero 2;

// resultado false
~~~



*Compara se o valor da variável **numero1** é **diferente** ao valor da variável **numero2**.*

*Retorna **true** se condição igual a **verdadeira** e **false** se condição igual a **falsa**.*

~~~java
int numero1 = 1;
int numero2 = 2;

boolean simNao numero1 != numero 2;

// resultado true
~~~



### Lógicos

*Os operadores lógicos representam o recurso que nos permite criar expressões lógicas maiores a partir da junção de duas ou mais expressões.*

* **&&** Operador Lógico **E**
* **||** Operador Lógico **OU**

##### Exemplo:

~~~java
//Ex 01
boolean condicao1 = true;
boolean condicao2 = true;

if (condicao1 && condicao2) {
    System.out.printn("As duas condições são verdadeiras")
}

if (condicao1 || condicao2) {
    System.out.printn("Uma das duas condições é verdadeiras")
}

// resultado
// As duas condições são verdadeiras
// Uma das duas condições é verdadeiras
~~~

~~~java
//Ex 02
boolean condicao1 = true;
boolean condicao2 = false;

if (condicao1 && condicao2) {
    System.out.printn("As duas condições são verdadeiras")
}

if (condicao1 || condicao2) {
    System.out.printn("Uma das duas condições é verdadeiras")
}

// resultado
// Uma das duas condições é verdadeiras
~~~

