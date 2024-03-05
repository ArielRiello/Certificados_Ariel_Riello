let arr = gets().split(', ');

const list = {
  Reflorestamento: gets(),
  EsgotoTratado: gets(),
  EmissaoDeCarbono: gets(),
  EnergiaSustentavel: gets(),
};

const findItem = (object, index) => Object.keys(object).filter(item => item.toString() == index);

for (const atividade of arr) {
  const valor = list[atividade];
  
  if (valor === "Feito") {
    print("Não multar");
  } else if (valor === "Em progresso") {
    print("Avaliação de progresso");
  } else {
    print("Multa");
  }
}