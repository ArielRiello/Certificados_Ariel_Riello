# Fermentar é Viver

Nivel: Básico / Carga Horária: 1h

---

## Descrição

Com o estoque de cogumelos nas alturas, os CodeMiners estão produzindo sua famosa cerveja artesanal e agora precisam monitorar sua temperatura constantemente. A temperatura é um fator crítico para garantir a qualidade da cerveja, e um desvio dos valores ideais pode afetar negativamente seu sabor e aroma. Para solucionar esse problema, será criado um programa em C que será embarcado na cervejeira e fornecerá leituras em tempo real da temperatura, permitindo que os CodeMiners monitorem a cerveja durante todo o processo de produção.

---

## Entrada

Um número inteiro representando a temperatura atual.

---

## Saída

Uma string: "Ideal" se a temperatura estiver no intervalo ideal, "Baixa" se estiver abaixo de 18 graus e "Alta" se estiver acima de 24 graus.

---

## Exemplos

A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

| Entrada | Saida |
|---|---|
| 20 | Ideal |
| 15 | Baixa |
| 26 | Alta |

---

*Código Base:*

~~~c
#include <stdio.h>

int main() {
  int temperatura;
  scanf("%d", &temperatura);
  
  // TODO: Crie as condições de acordo com as saídas deste desafio.
  
  return 0;
}
~~~
---