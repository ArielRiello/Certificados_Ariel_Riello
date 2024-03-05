# Ordenação de Relíquias com Insertion Sort

Nivel: Intermediário / Carga Horária: 1h

---

## Descrição

Na Fortaleza dos CodeMiners, o processo de mineração de dados, eventualmente, coleta relíquias místicas que possuem poderes incríveis. Essas relíquias são numeradas de acordo com sua raridade e os estudiosos desejam organizá-las em ordem crescente para facilitar a pesquisa e o estudo. Sua missão é criar um algoritmo em C que implemente o Insertion Sort¹ para ordenar as relíquias. Com esse algoritmo, os estudiosos poderão manter suas relíquias organizadas e acessíveis, permitindo um estudo mais eficiente das propriedades místicas.

¹ Um passo à frente do Bubble Sort, o Insertion Sort é outro algoritmo simples de entender e implementar. Ele funciona construindo uma sublista ordenada, inserindo elementos um a um em suas posições corretas. Apesar de ainda não ser o mais eficiente, é uma evolução natural no aprendizado após o Bubble Sort.

---

## Entrada

* 1ª Linha: Número inteiro N (1 <= N <= 1000), representando a quantidade de relíquias.

* 2ª Linha: Lista com N números inteiros NÃO ORDENADOS e separados por espaços, representando a raridade de cada relíquia.

---

## Saída

Imprima a lista de relíquias em ORDEM CRESCENTE, com cada número separado por um espaço.

---

## Exemplos

A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada:

5

5 3 4 1 2

Saída:

1 2 3 4 5

---

*Código Base:*

~~~c
#include <stdio.h>
#include <stdlib.h>

void insertionSort(int reliquias[], int quantidade) {
  // TODO: Implemente o algoritmo de ordenação "Insertion Sort".
}

int main() {
  // Lê os nossos dados de entrada:
  int quantidade;
  scanf("%d", &quantidade);
  int  reliquias[quantidade];
  for (int i = 0; i < quantidade; i++) {
    scanf("%d", & reliquias[i]);
  }

  // Executa o algoritmo "insertionSort" para ordenar os "reliquias".
  insertionSort(reliquias, quantidade);

  // Imprime as "reliquias" ordenados
  for (int i = 0; i < quantidade; i++) {
    printf("%d ",  reliquias[i]);
  }
  return 0;
}
~~~
---