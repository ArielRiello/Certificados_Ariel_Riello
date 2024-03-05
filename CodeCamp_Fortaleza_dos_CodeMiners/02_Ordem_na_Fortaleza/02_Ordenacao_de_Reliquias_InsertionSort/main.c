#include <stdio.h>
#include <stdlib.h>

void insertionSort(int reliquias[], int quantidade) {
  int i, j, temp;
  for (i = 1; i < quantidade; i++) {
    temp = reliquias[i];
    j = i - 1;
    while (j >= 0 && reliquias[j] > temp) {
      reliquias[j + 1] = reliquias[j];
      j--;
    }
    reliquias[j + 1] = temp;
  }
}

int main() {

  int quantidade;
  scanf("%d", &quantidade);
  int reliquias[quantidade];
  for (int i = 0; i < quantidade; i++) {
    scanf("%d", &reliquias[i]);
  }

  insertionSort(reliquias, quantidade);

  for (int i = 0; i < quantidade; i++) {
    printf("%d ", reliquias[i]);
  }
  return 0;
}
