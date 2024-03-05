const arr = gets().split(', ');

let qualFiltro = "Filtro Normal";

for (const molécula of arr) {
  if (molécula.length > 10) {
    qualFiltro = "Filtro Duplo Específico";
    break;
  } else if (molécula.length > 5) {
    qualFiltro = "Filtro Específico";
  }
}

print(`O filtro deve ser: ${qualFiltro}`);