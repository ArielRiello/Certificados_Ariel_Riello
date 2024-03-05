let lista1 = gets().split(', ');
let lista2 = gets().split(', ');
let lista3 = gets().split(', ');

let arr = [lista1, lista2, lista3];

let qualFiltro = "Filtro Simples";
let qualMolecula = "";

const moleculasPrejudiciais = ["NO2", "SO2", "CO", "FHO"];

for (const lista of arr) {
  for (const molécula of lista) {
    if (moleculasPrejudiciais.includes(molécula)) {
      qualFiltro = "Filtro Específico para a Molécula";
      qualMolecula = molécula;
      break;
    }
  }
}

if (qualFiltro === "Filtro Específico para a Molécula") {
  print(`${qualFiltro} ${qualMolecula}`);
} else {
  print(qualFiltro);
}