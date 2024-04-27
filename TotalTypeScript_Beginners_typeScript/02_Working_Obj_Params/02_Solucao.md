
## Adicionar Tipos aos Parâmetros de Objeto

Tutorial TypeScript para Iniciantes

/src/02-object-param.solution.1.ts

Existem várias soluções para este problema.

### Solução 1: Passar um Tipo de Objeto Diretamente

Talvez a solução mais simples seja passar um tipo de objeto diretamente para o argumento params.

Use chaves para representar o objeto e, em seguida, crie o tipo inline:

~~~Typescript
export const addTwoNumbers = (params: { first: number; second: number }) => {
...
~~~

Note que o TypeScript entenderá se você usar uma vírgula entre os tipos first e second desta forma:

~~~Typescript
params: {first: number, second: number}
~~~

No entanto, o Prettier corrigirá para usar ponto e vírgula em vez disso.

### Solução 2: Criar um Tipo Nomeado

Uma técnica útil é criar um tipo nomeado. Use a palavra-chave type e forneça um nome e um objeto semelhante à solução anterior.

Neste caso, nomearemos o tipo como AddTwoNumbersArgs e tiparemos first e second como número:

~~~Typescript
type AddTwoNumbersArgs = {
first: number;
second: number;
};
~~~

Agora podemos definir os params como tipados como AddTwoNumbersArgs:

~~~Typescript
export const addTwoNumbers = (params: AddTwoNumbersArgs) => {
return params.first + params.second;
};
~~~

### Solução 3: Criar uma Interface

Interfaces podem ser usadas para representar objetos (elas podem fazer outras coisas, mas estamos preocupados apenas com objetos por enquanto).

Usar interface é semelhante ao uso de type.

~~~Typescript
interface AddTwoNumbersArgs {
first: number;
second: number;
};

export const addTwoNumbers = (params: AddTwoNumbersArgs) => {
return params.first + params.second;
};
~~~

Escolhendo entre Inline, Tipo e Interface

A técnica inline usada na primeira solução fornecerá um erro detalhado que inclui o tipo completo do objeto:
O argumento do tipo 'number' não é atribuível a um parâmetro do tipo '{first: number; second: number;}'

Mas, em geral, você deve usar aliases em vez de ir inline.

Então, quando você deve escolher type e quando deve escolher interface?

Isso se resume à sintaxe que você prefere.

Tecnicamente, type pode representar qualquer coisa. Pode ser um número, ou uma string, ou um booleano.

O TypeScript dará um erro se você tentar usar uma string com interface:

~~~Typescript
// this won't work!

interface AddTwoNumbersArgs = string
~~~

Quando você está começando, não importa muito se você escolhe type ou interface.

Apenas seja consistente!

---

### Transcrição

Existem várias soluções para este problema. A primeira, e talvez uma das mais simples de entender, é você pode passar um tipo de objeto diretamente para o argumento params. Use estas chaves para representar um objeto, e então você cria o tipo inline ali.

Note que o TypeScript entenderá se você usar uma vírgula nesta situação, mas geralmente, e o Prettier corrigirá isso, então você usa ponto e vírgula, em vez disso.

Esta é a primeira solução. A segunda solução é criando um tipo aqui. Criamos um tipo nomeado, damos um nome ao tipo, o que é bastante útil. Criamos isso com este sinal de igual aqui. Dizemos... basicamente passamos a mesma coisa que tínhamos antes, só que dentro de um tipo ali.

Se eu quisesse converter isso para um tipo, apenas criaria um novo tipo aqui e diria NovoTipo e diria type NovoTipo = e apenas colaria o que copiei ali.

A terceira solução é usar uma interface. Uma interface é bastante semelhante a um tipo, mas as interfaces só podem ser usadas para representar objetos e algumas outras coisas, mas principalmente objetos neste curso básico.

Você pode estar se perguntando por que escolheria tipo em vez de interface? Tecnicamente, tipo pode representar qualquer coisa. Tipo pode ser um número. Pode ser uma string. Pode ser booleano. Pode ser absolutamente qualquer coisa, enquanto uma interface, se você tentar dizer interface = string, ela vai reclamar com você. Ela não vai deixar. Não é muito divertido.

Por que você usaria interface em vez de tipo? Costumava haver muita confusão sobre isso. É uma pergunta que me fazem muito.

Para ser honesto, qualquer sintaxe que você preferir, você deve escolher e apenas se manter consistente. Qualquer uma delas vai te dar...

Você também notará, se... Nesta primeira solução, se eu refatorar isso de volta para como era, na verdade vou obter uma mensagem de erro mais detalhada se fizer isso ao invés do outro caminho. Se eu errar isso, e se eu disser... Vamos dizer que eu remova um destes e apenas adicione um número aleatório no lugar.

Então, ele vai dizer "O argumento do tipo 'number' não é atribuível ao parâmetro do tipo..." e ele dá o valor literal aqui, então está escrito.

Enquanto se eu fizer isso neste, onde tem um alias de tipo atribuído a ele e eu disser blah, blah, blah, blah, blah, então vai dizer, "O argumento do tipo 'number' não é atribuível ao tipo 'AddTwoNumbers Args'", o que é melhor e um pouco mais legível, um pouco mais compreensível.

Em geral, você deve extrair esses para seus próprios aliases, mas não importa muito se você usa tipo ou interface, especialmente quando está começando.

---