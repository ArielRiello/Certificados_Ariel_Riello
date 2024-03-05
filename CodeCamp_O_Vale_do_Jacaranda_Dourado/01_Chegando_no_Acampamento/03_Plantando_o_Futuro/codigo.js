let id = parseInt(gets());

if (id === 10) {
  print('Plantar!');
} else if (id < 10) {
  let calculo = 10 - id;
  print(`O buraco deve avançar ${calculo} metros`);
} else if (id > 10) {
  let calculo = id - 10;
  print(`O buraco deve retroceder ${calculo} metros`);
}
