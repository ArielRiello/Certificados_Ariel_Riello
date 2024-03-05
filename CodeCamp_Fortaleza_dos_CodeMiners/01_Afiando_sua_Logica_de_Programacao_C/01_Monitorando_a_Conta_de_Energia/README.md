# Monitorando a Conta de Energia

Nivel: Básico / Carga Horária: 1h

---

## Descrição

As máquinas pesadas da Fortaleza dos CodeMiners precisam de ajustes em seus parâmetros. Proativamente, você sugere uma solução que calcule a média do consumo energético de três máquinas, já que essa é a configuração mais utilizada por eles. Desta forma, será possível analisar e planejar a estratégia de escavação mais eficiente, pois diferentes combinações de máquinas poderão ser avaliadas por meio do mesmo algoritmo.

---

## Entrada

Três valores inteiros positivos, representando o consumo de energia de cada máquina, separados por espaços.

---

## Saída

A média de consumo das três máquinas, formatada com duas casas decimais.

---

## Exemplos

A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

| Entrada | Saida |
|---|---|
10 20 30 | 20.00
15 20 30 | 25.00
 5 10 20 | 11.67

---

### Código Base

~~~c
#include <stdio.h>

int main() {
  int consumo1, consumo2, consumo3;
  float media;

  // Lendo os valores de consumo das três máquinas
  scanf("%d %d %d", &consumo1, &consumo2, &consumo3);

  //TODO: Calcule a média de consumo e a imprima com duas casas decimais.

  return 0;
}
~~~

---