
## Fix the Implicit 'Any' Error
### Corrija o Erro Implícito de 'Any'

### Tradução

tutorial-iniciantes-typescript/src/01-number.solution.ts

*'a' tem implicitamente um tipo 'any'.*

Este erro ocorre porque o TypeScript não possui informações suficientes para inferir um tipo, então o define como 'any' por padrão.

A solução é adicionar anotações de tipo aos argumentos da função.

Neste caso, tanto a quanto b devem ser tipados como número:

~~~typescript
export const addTwoNumbers = (a: number, b: number) => {
return a + b;
};
~~~

As Anotações de Tipo são Cruciais para Entender o TypeScript

O TypeScript depende de anotações de tipo para entender os contratos que a função deve cumprir. As anotações de tipo são cruciais para entender o TypeScript.

Sempre que você criar uma função, é necessário especificar os tipos de cada argumento!

Para ajudá-lo a lembrar desta regra fundamental, recomendo habilitar o modo estrito para todos os projetos TypeScript.

Quando o modo estrito está habilitado, você receberá o erro 'implicitamente tem tipo 'any'' sempre que deixar de fora as anotações de tipo.

Mas por que o TypeScript não pode simplesmente olhar para o + e saber que a e b são números?

Experimente com Diferentes Tipos

Tente definir os tipos de a e b como string.

Ao executar o teste novamente, o TypeScript lhe daria um erro:

~~~typescript
Argument of type 'number' is not assignable to parameter of type 'string'
~~~

Atualizar o código de teste para passar strings para addTwoNumbers acaba resultando em erros de tempo de execução.

Mudar um tipo para um Boolean não funcionará porque você não pode adicionar um booleano a um número.

Uma string pode ter um número anexado a ela com +, mas o teste falharia.

---

Transcrição

A solução, então, é adicionar algumas anotações de tipo aos argumentos da função. Agora, A é tipado como número e B é tipado como número. Podemos mudar isso, se quisermos. Podemos mudar isso para string e string aqui, mas então começamos a receber erros mais adiante, em addTwoNumbers.

Diz, "O argumento do tipo 'number' não é atribuível ao parâmetro do tipo 'string'". Teríamos que passar algumas strings aqui. Então, é claro, as coisas vão falhar durante a execução.

Essa ideia de que você precisa anotar e fazer o TypeScript entender os contratos que suas funções devem cumprir, as coisas que você deve passar para suas funções, é fundamental para entender o TypeScript.

Poderíamos mudar isso para um booleano também, se quisermos. Na verdade, os booleanos não podem ser adicionados aqui. "O operador '+' não pode ser aplicado aos tipos 'boolean' e 'number'". Você não pode adicionar um booleano a um número.

De forma estranha, você pode adicionar uma string a um número aqui, mas o que aconteceria é que ela seria anexada. Teríamos um dois aqui. Está esperando que seja um número seis, mas na verdade acaba sendo 24 aqui porque está adicionando o quatro, concatenando-o com o dois.

Você pode estar se perguntando por que o TypeScript não entende isso? Ele vê que há um sinal de mais entre as duas coisas aqui. Por que ele não pode entender que A é um número e B é um número sem que precisemos adicionar isso?

Bem, é porque o TypeScript, na origem de suas funções, como sempre que você cria uma função, precisa fazer esse contrato para que o TypeScript entenda exatamente o que você pode passar para a função. Essa é uma das regras fundamentais do TypeScript, que em toda função que você cria, você sempre deve especificar os tipos de cada argumento.

Se você não o fizer, vai receber esse erro bastante confuso, mas é exatamente isso que esse erro significa. No tsconfig, habilitamos o modo estrito. O modo estrito significa que se você não especificar essas coisas, você vai receber um erro.

Recomendo habilitar o modo estrito para todos os projetos TypeScript. Esta é sua primeira solução. Parabéns.

---

### Solução do exercicio anterior:

~~~typescript
export const addTwoNumbers = (a: number, b: number) => {
  return a + b;
};

it("Should add the two numbers together", () => {
  expect(addTwoNumbers(2, 4)).toEqual(6);
  expect(addTwoNumbers(10, 10)).toEqual(20);
});
~~~

---