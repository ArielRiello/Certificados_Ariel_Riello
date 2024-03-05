#include <stdio.h>
#include <stdlib.h>

void trocar(int *a, int *b) {
  int temp = *a;
  *a = *b;
  *b = temp;
}

int particionar(int array[], int inicio, int fim) {
  int pivo = array[fim];
  int i = inicio - 1;

  for (int j = inicio; j < fim; j++) {
    if (array[j] < pivo) {
      i++;
      trocar(&array[i], &array[j]);
    }
  }

  trocar(&array[i+1], &array[fim]);
  return i+1;
}

void quickSort(int array[], int inicio, int fim) {
  if (inicio < fim) {
    int indice_pivo = particionar(array, inicio, fim);
    quickSort(array, inicio, indice_pivo-1);
    quickSort(array, indice_pivo+1, fim);
  }
}

int main() {

  int quantidade;
  scanf("%d", &quantidade);
  int joias[quantidade];
  for (int i = 0; i < quantidade; i++) {
      scanf("%d", &joias[i]);
  }

  int inicio = 0;
  int fim = quantidade - 1;

  quickSort(joias, inicio, fim);


  for (int i = 0; i < quantidade; i++) {
      printf("%d ", joias[i]);
  }

  return 0;
}
