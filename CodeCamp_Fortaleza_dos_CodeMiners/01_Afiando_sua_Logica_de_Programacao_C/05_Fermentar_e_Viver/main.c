#include <stdio.h>

int main() {
  int temperatura;
  scanf("%d", &temperatura);

  if (temperatura < 18) {
    printf("Baixa");
  }
  if (temperatura > 18 && temperatura < 24) {
    printf("Ideal");
  }
  if (temperatura > 24) {
    printf("Alta");
  }

  return 0;
}
