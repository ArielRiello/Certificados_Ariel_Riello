#include <stdio.h>

int main() {
  int capacidadeAtual, aumentoPercentual, capacidadeNova;

  scanf("%d %d", &capacidadeAtual, &aumentoPercentual);

  capacidadeNova = ((capacidadeAtual * aumentoPercentual) / 100) + capacidadeAtual;

  printf("%.d", capacidadeNova);

  return 0;
}
