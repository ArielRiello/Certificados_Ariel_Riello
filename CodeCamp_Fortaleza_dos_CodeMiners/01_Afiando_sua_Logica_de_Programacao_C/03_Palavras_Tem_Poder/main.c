#include <stdio.h>
#include <string.h>


void inverter(char palavra[]) {
    int i, j;
    char temp;

    j = strlen(palavra) - 1;

    for (i = 0; i < j; i++, j--) {
        temp = palavra[i];
        palavra[i] = palavra[j];
        palavra[j] = temp;
    }
}

int main() {
  char palavra[100];

  scanf("%s", palavra);

  inverter(palavra);

  printf("%s", palavra);

  return 0;
}
