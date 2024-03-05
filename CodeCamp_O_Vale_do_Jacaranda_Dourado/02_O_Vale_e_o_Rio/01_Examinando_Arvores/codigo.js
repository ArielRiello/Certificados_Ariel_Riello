const input = gets();
const amostras = input.split(',').map(Number);

for (const amostra of amostras) {
  if (amostra >= 75) {
    print('Descartar da lista');
  } else if (amostra >= 50) {
    print('Manter sob observação');
  } else if (amostra < 50) {
    print('Isolar e iniciar protocolo de cuidados');
  }
}