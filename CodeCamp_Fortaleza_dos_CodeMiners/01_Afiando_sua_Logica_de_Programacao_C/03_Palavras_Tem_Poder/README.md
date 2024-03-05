# Armazenamento de Dados é Vida!

Nivel: Básico / Carga Horária: 1h

---

## Descrição

Com o avanço inédito às profundezas da Grande Montanha, os CodeMiners encontraram um pergaminho antigo com códigos secretos em um local que exala uma energia divina. Eles precisam decifrar o código, que consiste em um conjunto simples de palavras. Escreva um programa em C que inverta a ordem das letras para revelar as palavras secretas.

---

## Entrada

Um texto com uma palavra misteriosa (com no máximo 100 caracteres) sem espaços.

---

## Saída

O texto invertido.

---

## Exemplos

A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

| Entrada | Saida |
|---|---|
| tumahaB | Bahamut |
| droK | Kord |
| sihtarE | Erathis |

---

*Código Base:*

~~~c
#include <stdio.h>
#include <string.h>

// Função que recebe uma string e inverte a ordem das letras.
void inverter(char palavra[]) {
  // TODO: Implemente a lógica para inverter a "palavra".
}

int main() {
  char palavra[100];

  // Lê a palavra a ser invertida do usuário.
  scanf("%s", palavra);

  // Chama a função que inverte a palavra.
  inverter(palavra);

  // Imprime a palavra invertida na tela.
  printf("%s", palavra);

  return 0;
}
~~~
---