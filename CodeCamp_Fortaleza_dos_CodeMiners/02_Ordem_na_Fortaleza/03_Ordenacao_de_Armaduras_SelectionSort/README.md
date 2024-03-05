# Ordenação de Armaduras com Selection Sort

Nivel: Intermediário / Carga Horária: 1h

---

## Descrição

Os guerreiros da Fortaleza dos CodeMiners precisam manter suas armaduras em ordem, para facilitar a escolha do equipamento certo antes das batalhas. As armaduras são numeradas de acordo com seu nível de proteção, e os guerreiros desejam organizá-las em ordem decrescente. Sua missão é criar um algoritmo em C que implemente o Selection Sort¹ para ordenar as armaduras. Com esse algoritmo, os guerreiros poderão encontrar a armadura mais adequada rapidamente, o que pode ser crucial em uma situação de combate.

¹Este algoritmo é um pouco mais avançado que os anteriores. Ele divide a lista em duas partes: a parte ordenada e a parte não ordenada. A cada iteração, o algoritmo seleciona o menor (ou maior) elemento da parte não ordenada e o move para o final da parte ordenada. Isso ajuda a entender melhor a divisão do trabalho em algoritmos de ordenação. 

---

## Entrada

* 1ª Linha: Número inteiro N (1 <= N <= 1000), representando a quantidade de armaduras.

* 2ª Linha: Lista com N números inteiros NÃO ORDENADOS e separados por espaços, representando o nível de proteção de cada armadura.

---

## Saída

Imprima a lista de armaduras em ORDEM DECRESCENTE, com cada número separado por um espaço.

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

void trocar(int *a, int *b) {
  int temp = *a;
  *a = *b;
  *b = temp;
}

void selectionSort(int array[], int quantidade){ 
  // TODO: Implemente o algoritmo "Selection Sort" para ordenação DECRESCENTE.
  // Dica: O método "trocar" pode ser útil ;)
}

int main() {
  // Lê os nossos dados de entrada:
  int quantidade;
  scanf("%d", &quantidade);
  int armaduras[quantidade];
  for (int i = 0; i < quantidade; i++) {
      scanf("%d", &armaduras[i]);
  }
  
  // Executa o algoritmo "selectionSort" para deixar as "armaduras" em ordem DECRESCENTE.
  selectionSort(armaduras, quantidade);
  
  // Imprime as "armaduras" ordenados.
  for (int i = 0; i < quantidade; i++) {
      printf("%d ", armaduras[i]);
  }
  
  return 0;
}
~~~

---