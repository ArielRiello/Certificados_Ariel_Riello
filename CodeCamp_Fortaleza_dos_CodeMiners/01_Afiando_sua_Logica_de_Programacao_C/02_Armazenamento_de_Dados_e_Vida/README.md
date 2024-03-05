# Armazenamento de Dados é Vida!

Nivel: Básico / Carga Horária: 1h

---

## Descrição

Com as máquinas pesadas agrupadas estrategicamente, graças ao seu algoritmo de cálculo energético, agora a mineração está muito mais eficiente! Com isso, os CodeMiners logo terão que aumentar a capacidade de armazenamento de dados em seus discos de Mithril. Atualmente, cada máquina tem uma capacidade em teraflops e todas terão um upgrade! Escreva um programa em C que calcule a nova capacidade total de todas as máquinas após um aumento percentual específico.

---

## Entrada

Dois valores inteiros positivos, representando a capacidade atual total em teraflops e o aumento percentual, separados por espaço.

---

## Saída

A nova capacidade total em teraflops.

---

## Exemplos

A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

| Entrada | Saida |
|---|---|
| 100 20 | 120 |
| 50 10 | 55 |
| 200 50 | 300 |

---

*Código Base:*

~~~c
#include <stdio.h>

int main() {
  int capacidadeAtual, aumentoPercentual;
  
  // Lê as entradas do usuário
  scanf("%d %d", &capacidadeAtual, &aumentoPercentual);

  // TODO: Declare e calcule a nova capacidade do disco de Mithril.
  
  // TODO: Imprima a nova capacidade.

  return 0;
}
~~~
---