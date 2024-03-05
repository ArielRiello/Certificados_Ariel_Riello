#include <stdio.h>

int main() {
  int consumo1, consumo2, consumo3;
  float media;

  scanf("%d %d %d", &consumo1, &consumo2, &consumo3);

  media = (float)(consumo1 + consumo2 + consumo3) / 3;

  printf("%.2f", media);

  return 0;
}
