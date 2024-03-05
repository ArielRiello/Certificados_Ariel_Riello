#include<stdio.h>
#include<stdlib.h>

void trocar(int *a, int *b){
    int temp = *a;
    *a = *b;
    *b = temp;
}

void bubbleSort(int array[], int quantidade){
  int i, j;

  for (i = 0; i < quantidade - 1; i++) {
    for (j = 0; j < quantidade - i - 1; j++) {
      if (array[j] > array[j+1]) {
        trocar(&array[j], &array[j+1]);
      }
    }
  }
}

int main() {
  int quantidade;
  scanf("%d", &quantidade);
  int frascos[quantidade];
  for (int i = 0; i < quantidade; i++) {
      scanf("%d", &frascos[i]);
  }

  bubbleSort(frascos, quantidade);

  for (int i = 0; i < quantidade; i++) {
      printf("%d ", frascos[i]);
  }

  return 0;
}
