
# Working with Object Params
## Trabalhando com Parâmetros de Objeto

Tutorial TypeScript para iniciantes

/src/02-object-param.problem.ts

Aqui está uma implementação diferente da função addTwoNumbers:

~~~Typescript
export const addTwoNumbers = (params) => {
return params.first + params.second;
};
~~~

Desta vez, a função aceita um objeto de parâmetros com propriedades first e second.

~~~Typescript
{
first: 2,
second: 4,
}
~~~

Da mesma forma que da última vez, estamos recebendo o erro "implicitamente tem um tipo 'any'".

### Desafio

Descubra como tipar os parâmetros como um objeto com uma chave first que é um número e uma chave second que também é um número.

Codigo do Desafio:

~~~Typescript
import { expect, it } from "vitest";

export const addTwoNumbers = (params) => {
  return params.first + params.second;
};

it("Should add the two numbers together", () => {
  expect(
    addTwoNumbers({
      first: 2,
      second: 4,
    }),
  ).toEqual(6);

  expect(
    addTwoNumbers({
      first: 10,
      second: 20,
    }),
  ).toEqual(30);
});
~~~

---

#### Transcrição

Estamos enfrentando um problema semelhante ao que tivemos da última vez. Temos um argumento de função que está nos dando "O parâmetro 'params' possui implicitamente um tipo 'any'", exceto que é um pouco diferente porque ainda temos nossa função addTwoNumbers, mas estamos passando-os como um objeto para nossa função.

De alguma forma, precisamos descobrir como tipar esses parâmetros como um tipo de objeto com uma chave 'first', que é um número, e uma chave 'second', que também é um número. Esse é o seu desafio.

---