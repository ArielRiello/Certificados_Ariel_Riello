# Ordenação de Poções com Bubble Sort

Nivel: Intermediário / Carga Horária: 1h

---

## Descrição

Na Fortaleza dos CodeMiners, há uma área especializada em alquimia, onde os aprendizes criam poções mágicas (extraídas dos óleos essenciais dos cogumelos da Grande Montanha) para aprimorar suas habilidades. As poções são armazenadas em frascos numerados e os aprendizes precisam organizá-las em ordem crescente de acordo com a numeração. Sua missão é criar um algoritmo em C que implemente o Bubble Sort¹ para ordenar os frascos de poção. Este algoritmo ajudará os aprendizes a manterem a área de alquimia organizada e eficiente.

¹ É um dos algoritmos de ordenação mais simples e é fácil de entender. Ele compara pares de elementos adjacentes e troca-os se estiverem fora de ordem, repetindo esse processo até que toda a lista esteja ordenada. Apesar de não ser eficiente, é um bom ponto de partida para o estudo de algoritmos de ordenação.

---

## Entrada

* 1ª Linha: Número inteiro N (1 <= N <= 1000), representando a quantidade de frascos de poção.

* 2ª Linha: Lista com N números inteiros NÃO ORDENADOS e separados por espaços, representando a numeração de cada frasco de poção.

---

## Saída

A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

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
#include<stdio.h>
#include<stdlib.h>

void trocar(int *a, int *b){ 
    int temp = *a; 
    *a = *b; 
    *b = temp; 
}

void bubbleSort(int array[], int quantidade){ 
  // TODO: Implemente o algoritmo "Bubble Sort".
  // Dica: O método "trocar" pode ser útil ;)
}

int main() {
  // Lê os nossos dados de entrada:
  int quantidade;
  scanf("%d", &quantidade);
  int frascos[quantidade];
  for (int i = 0; i < quantidade; i++) {
      scanf("%d", &frascos[i]);
  }
  
  // Executa o algoritmo "bubbleSort" para ordenar os "frascos".
  bubbleSort(frascos, quantidade);
  
  // Imprime os "frascos" ordenados.
  for (int i = 0; i < quantidade; i++) {
      printf("%d ", frascos[i]);
  }
  
  return 0;
}
~~~
---