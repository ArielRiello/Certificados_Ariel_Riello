const quantidadePlastico = parseInt(gets()); 

let dias = 0;
let quantidadeAtual = quantidadePlastico;

while (quantidadeAtual > 1) {
  quantidadeAtual /= 2;
  dias++;
}

print(`Serão necessários ${dias} dias`);