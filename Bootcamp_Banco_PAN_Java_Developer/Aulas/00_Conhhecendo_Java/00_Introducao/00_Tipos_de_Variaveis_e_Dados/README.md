## Tipos de Variáveis / Dados

#### Primitivos: 

*Não são considerados objetos, e portanto representam valores brutos.*

*Eles são armazenados diretamente na pilha de memória. **Memory Stack***

Podemos dividir os tipos em dois grupos:

* Numérico
* Boolean
  * Que é um tipo primitivo propriamente dito.

O tipo **boolean** só recebe dois valores:

* **True**
* **False**

Os tipos **numéricos**, temos duas subdivisões:

* **Integrais**
* **Ponto flutuante**

Os tipos **numéricos integrais** são compostos por:

* **byte**
* **short**
* **int**
* **long**
* **char**

Apesar de uma variável do tipo **char** receber um caractere, essa variável pode receber valores:

* **Literais do tipo int** (por isso o tipo numérico integral)
* **Unicode**



#### Tipos Primitivos e seus valores de memória

* **int (memória: 4 bytes) **

* **byte (memória: 1 byte)**

* **short (memória: 2 bytes)**

* **long (memória: 8 bytes) **



#### Tipos primitivos que podem conter partes fracionárias:

* **float** (memória: 4 bytes) 

* **double** (memória: 8 bytes)



#### Estrutura padrão para se declarar uma variável:

**<Tipo> <nomeVariavel> <atribuicaoDeValorOpcional>**



##### Exemplos:

~~~java
byte idade = 123;
short ano = 2021;
int cep = 21070333;
long cpf = 98765432109L;
float pi = 3.14F;
double salario = 1275.33;
~~~

Variáveis podem ter valores alterados:

~~~java
int numero = 1;
numero = 2;
System.out.println(numero);

// resultado: 2
~~~

Para se definir uma constante em Java (Variável que não pode alterar valor).

Usasse o "final" e se escreve em letras maiúsculas.

~~~java
final double VALOR_DE_PI = 3.14;
~~~

