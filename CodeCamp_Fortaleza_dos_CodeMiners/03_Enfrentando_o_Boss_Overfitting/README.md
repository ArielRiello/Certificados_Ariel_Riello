# Batalha Final: Enfrentando o Boss Overfitting

Nivel: Avançado / Carga Horária: 1h

---

## Descrição

Após uma noite de gala no lançamento do livro de Hella na CodeMiners I/O, os trabalhos de mineração de dados voltaram a todo vapor. Com novas técnicas e boas práticas exploradas na conferência, a eficiência na mineração aumentou consideravelmente. Foi então que, finalmente, os CodeMiners localizaram a lendária masmorra do temido Boss Overfitting.

Overfitting é um Boss astuto, conhecido por sua capacidade de se adaptar excessivamente às estratégias de seus adversários, tornando-se imprevisível e difícil de ser derrotado. Os CodeMiners, durante séculos de mineração de dados, documentaram suas descobertas e identificaram as fraquezas do Boss Overfitting. Essas informações são valiosas, pois indicam quais equipamentos devem ser usados pelos CodeMiners para derrotá-lo.

O desafio consiste em criar um programa em C++ que utilize Orientação a Objetos e algoritmos de busca (busca linear, binária ou outros mais eficientes) para determinar se os CodeMiners têm em seu arsenal os equipamentos necessários para derrotar o Boss Overfitting. Para isso, teremos em nosso template de código as classes FortalezaCodeMiner e Boss com atributos relacionados às nossas entradas, além do método possui_equipamento preparado para implementação de seu algoritmo de busca escolhido.

---

## Entrada

* O programa receberá duas linhas:

* A primeira contendo os pontos fracos do Boss (inteiros separados por espaços);

* A segunda com os equipamentos disponíveis no Arsenal dos CodeMiners (inteiros separados por espaços).

---

## Saída

O objetivo é verificar se a lista de equipamentos possui TODOS os itens necessários para eliminar os pontos fracos do Boss. Se sim, o programa deve imprimir "Vencemos!". Caso contrário, deve imprimir "Perdemos!".

---

## Exemplos

A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada:

1 2 3 5

1 2 3 4 5 6 7 8 9 10

Saída:

Vencemos!

Entrada: 

1 3 5 7

1 2 4 6 8 9 10

Saida:

Perdemos!

---

*Código Base:*

~~~c
#include <iostream>
#include <vector>
#include <string>

using namespace std;

class FortalezaCodeMiner {
public:
  FortalezaCodeMiner(const vector<int>& equipamentos) : equipamentos_(equipamentos) {}

  bool possui_equipamento(int equipamento) {
    // TODO: Implementar um algoritmo de busca eficiente para encontrar o equipamento.
    return false;
  }

private:
  vector<int> equipamentos_;
};

class Overfitting {
public:
  Overfitting(const vector<int>& pontos_fracos) : pontos_fracos_(pontos_fracos) {}

  const vector<int>& pontos_fracos() const {
    return pontos_fracos_;
  }

private:
  vector<int> pontos_fracos_;
};

int main() {
  vector<int> pontos_fracos_chefao;
  vector<int> equipamentos_fortaleza;

  int n;

  // Lê os pontos fracos do Chefão Overfitting.
  cin >> n;
  for (int i = 0; i < n; i++) {
    int ponto_fraco;
    cin >> ponto_fraco;
    pontos_fracos_chefao.push_back(ponto_fraco);
  }

  // Lê os equipamentos da Fortaleza dos CodeMiners.
  cin >> n;
  for (int i = 0; i < n; i++) {
    int equipamento;
    cin >> equipamento;
    equipamentos_fortaleza.push_back(equipamento);
  }

  // Cria objetos dos tipos Overfitting e FortalezaCodeMiner
  Overfitting chefao(pontos_fracos_chefao);
  FortalezaCodeMiner fortaleza(equipamentos_fortaleza);

  // Verifica se todos os pontos fracos do Chefão possuem equipamentos na Fortaleza
  bool vitoria = true;
  for (int ponto_fraco : chefao.pontos_fracos()) {
    if (!fortaleza.possui_equipamento(ponto_fraco)) {
      vitoria = false;
      break;
    }
  }

  // Imprimir resultado da batalha
  cout << (vitoria ? "Vencemos!" : "Perdemos!") << endl;

  return 0;
}
~~~

---