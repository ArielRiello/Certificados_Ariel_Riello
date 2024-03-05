#include <stdio.h>

void trocar(int *a, int *b) {
  int temp = *a;
  *a = *b;
  *b = temp;
}

void selectionSort(int array[], int quantidade){
  int i, j, posicao_min;
  for (i = 0; i < quantidade - 1; i++) {
    posicao_min = i;
    for (j = i + 1; j < quantidade; j++) {
      if (array[j] > array[posicao_min]) {
        posicao_min = j;
      }
    }
    if (posicao_min != i) {
      trocar(&array[i], &array[posicao_min]);
    }
  }
}

int main() {

  int quantidade;
  scanf("%d", &quantidade);
  int armaduras[quantidade];
  for (int i = 0; i < quantidade; i++) {
    scanf("%d", &armaduras[i]);
  }

  selectionSort(armaduras, quantidade);

  for (int i = 0; i < quantidade; i++) {
    printf("%d ", armaduras[i]);
  }

  return 0;
}
