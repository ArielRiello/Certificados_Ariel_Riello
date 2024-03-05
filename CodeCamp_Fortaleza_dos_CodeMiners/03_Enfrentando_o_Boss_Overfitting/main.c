#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class FortalezaCodeMiner {
public:
  FortalezaCodeMiner(const vector<int>& equipamentos) : equipamentos_(equipamentos) {
    sort(equipamentos_.begin(), equipamentos_.end()); 
  }

  bool possui_equipamento(int equipamento) {

    int inicio = 0;
    int fim = equipamentos_.size() - 1;

    while (inicio <= fim) {
      int meio = inicio + (fim - inicio) / 2;

      if (equipamentos_[meio] == equipamento) {
        return true;
      } else if (equipamentos_[meio] < equipamento) {
        inicio = meio + 1;
      } else {
        fim = meio - 1;
      }
    }

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

  cin >> n;
  for (int i = 0; i < n; i++) {
    int ponto_fraco;
    cin >> ponto_fraco;
    pontos_fracos_chefao.push_back(ponto_fraco);
  }

  cin >> n;
  for (int i = 0; i < n; i++) {
    int equipamento;
    cin >> equipamento;
    equipamentos_fortaleza.push_back(equipamento);
  }

  Overfitting chefao(pontos_fracos_chefao);
  FortalezaCodeMiner fortaleza(equipamentos_fortaleza);

  bool vitoria = true;
  for (int ponto_fraco : chefao.pontos_fracos()) {
    if (!fortaleza.possui_equipamento(ponto_fraco)) {
      vitoria = false;
      break;
    }
  }

  cout << (vitoria ? "Vencemos!" : "Perdemos!") << endl;

  return 0;
}
