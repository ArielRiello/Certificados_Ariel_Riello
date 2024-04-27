
# The Implicit ‘Any’ Type Error
## O Erro de Tipo Implícito 'Any'

### Tradução

tutorial-iniciantes-typescript/src/01-number.problem.ts

Considere esta função addTwoNumbers:

~~~typescript
export const addTwoNumbers = (a, b) => {
return a + b;
};
~~~

Esta função recebe a e b e os adiciona juntos.

Parece ser JavaScript perfeitamente válido.

Ao executar npm run exercise 01 no terminal, podemos ver que nossos testes passam.

Mas mesmo que pareça válido e os testes passem, o TypeScript não está feliz.

O terminal exibe os seguintes erros juntamente com a linha de código onde ocorrem:

~~~typescript
O parâmetro 'a' tem implicitamente um tipo 'any'.
O parâmetro 'b' tem implicitamente um tipo 'any'.
~~~

Desafio

Leia nosso explicador sobre 'any' implícito e veja se consegue encontrar como corrigir esses erros do TypeScript.

[Explicação sobre o erro](https://www.totaltypescript.com/concepts/parameter-x-implicitly-has-an-any-type)

---

### Transcrição do Video

Temos aqui algum código que parece ser JavaScript perfeitamente válido, mas o TypeScript está nos advertindo. Temos uma função chamada "add two numbers", que recebe a e b e os adiciona juntos. Podemos ver no nosso terminal, nos testes que estão sendo analisados aqui.

Podemos bagunçar isso. Se quisermos, podemos dizer a-b e isso começará a falhar nossos testes. Podemos ver que na verdade está funcionando durante a execução, mas o TypeScript não está feliz. Sua tarefa aqui é descobrir por que ele não está feliz. Para decodificar essas mensagens de erro, o parâmetro a implicitamente tem um tipo 'any'.

O que diabos isso poderia significar? O parâmetro b implicitamente tem um tipo 'any'. Dê uma olhada na documentação e veja se consegue encontrar alguma pista sobre o que pode corrigir esses erros do TypeScript.

---

### Agora é sua vez! Tente resolver este exercício.

Codigo do exercicio: 

~~~typescript
import { expect, it } from "vitest";

export const addTwoNumbers = (a, b) => {
  return a + b;
};

it("Should add the two numbers together", () => {
  expect(addTwoNumbers(2, 4)).toEqual(6);
  expect(addTwoNumbers(10, 10)).toEqual(20);
});
~~~

---