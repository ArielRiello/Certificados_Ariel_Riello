
# Decoradores

### Objetos de Primeira Classe

Em Python, "objetos de primeira classe" refere-se a uma propriedade da linguagem que trata funções como objetos de dados normais. Isso significa que você pode passar funções como argumentos para outras funções, retorná-las como valores de outras funções e armazená-las em estruturas de dados, como listas e dicionários.

1. Passando funções como argumentos para outras funções:

~~~py
def funcao_superior(funcao):
    return funcao(5)

def funcao_inferior(x):
    return x * 2

resultado = funcao_superior(funcao_inferior)
print(resultado)  # Saída: 10
~~~

2. Retornando funções de outras funções:

~~~py
def criador_de_funcao(multiplicador):
    def funcao(x):
        return x * multiplicador
    return funcao

funcao_por_5 = criador_de_funcao(5)
print(funcao_por_5(2))  # Saída: 10
~~~

3. Armazenando funções em estruturas de dados:

~~~py
funcoes = [funcao_inferior, funcao_por_5]
print(funcoes )  # Saída: 6
print(funcoes )  # Saída: 15
~~~

Essa característica flexível é muito poderosa e é uma das razões pelas quais Python é tão popular para programação funcional e paradigmas orientados a objetos.

---

### Inner Functions

Inner functions, ou funções internas, em Python, referem-se a funções definidas dentro de outras funções. Em outras palavras, são funções aninhadas dentro do escopo de outra função. Essas funções internas podem acessar variáveis locais e argumentos da função externa (função envolvente), além de variáveis globais.

Aqui está um exemplo simples de uma função interna em Python:

~~~py
def externa():
    def interna():
        return "Esta é uma função interna"
    return interna()

print(externa())  # Saída: Esta é uma função interna
~~~

Neste exemplo, a **função interna()** é definida dentro da função **externa()**. A função **externa()** retorna o resultado da chamada da **função interna()**, permitindo que você chame diretamente **externa()** para obter o resultado da função interna.

As funções internas podem ser úteis para encapsular funcionalidades relacionadas em um escopo específico, evitando poluição do namespace global e aumentando a modularidade do código. Elas são frequentemente usadas em Python para implementar closures, que são funções que capturam e mantêm o ambiente léxico onde foram definidas.

---

### Retornando Funções de Funções

Python permite que funções retornem outras funções. Isso é uma parte fundamental da natureza de Python ser uma linguagem que trata funções como objetos de primeira classe.

Aqui está um exemplo de uma função que retorna outra função em Python:

~~~py
def criar_funcao(multiplicador):
    def funcao_interna(x):
        return x * multiplicador
    return funcao_interna

funcao_por_5 = criar_funcao(5)
print(funcao_por_5(2))  # Saída: 10
~~~

Neste exemplo, **criar_funcao** é uma função que aceita um argumento **multiplicador** e retorna uma função interna **funcao_interna**. A função interna **funcao_interna** multiplica seu argumento x pelo multiplicador fornecido quando a função externa foi chamada. Então, ao chamar **criar_funcao**(5), você recebe uma função que multiplica seu argumento por 5.

Essa capacidade de retornar funções de outras funções é útil para criar funções especializadas ou geradoras de funções de uma maneira mais dinâmica e flexível.

---

### Decorador Simples

Em Python, decoradores são uma característica poderosa da linguagem que permitem modificar ou estender o comportamento de funções ou métodos de forma declarativa. Eles são usados para adicionar funcionalidades extras a funções existentes sem modificá-las explicitamente. Decoradores são geralmente funções que aceitam outra função como argumento e retornam uma nova função. Eles são amplamente utilizados em situações como logging, medição de tempo, validação de entrada, caching, entre outros.

Por exemplo, aqui está um decorador simples que imprime uma mensagem antes e depois de chamar a função decorada:

~~~py
def decorador(func):
    def wrapper():
        print("Antes da chamada da função")
        func()
        print("Depois da chamada da função")
    return wrapper

@decorador
def minha_funcao():
    print("Minha função está sendo chamada")

minha_funcao()
~~~

Neste exemplo, **decorador** é o **decorador** que envolve a função **minha_funcao**. Quando **minha_funcao()** é chamada, o **decorador** é aplicado automaticamente, resultando na impressão das mensagens antes e depois da chamada da função.

Os decoradores são uma ferramenta poderosa para tornar o código mais limpo, modular e reutilizável, facilitando a adição e remoção de funcionalidades em funções existentes.

---

### Açucar Sintático

Açúcar sintático em Python refere-se a uma sintaxe mais concisa ou conveniente que é fornecida pela linguagem para expressar operações ou padrões comuns de forma mais legível e compacta. Embora a funcionalidade subjacente seja a mesma, o açúcar sintático torna o código mais claro e expressivo, facilitando a leitura e a escrita.

Alguns exemplos de açúcar sintático em Python incluem:

1. Compreensão de listas: Em vez de escrever loops for para criar listas, você pode usar compreensões de listas, que são mais concisas e expressivas.

~~~py
# Usando loop for
squares = []
for x in range(10):
    squares.append(x ** 2)

# Usando compreensão de lista
squares = [x ** 2 for x in range(10)]
~~~

2. Uso de if ternário: Em vez de escrever um bloco if completo para atribuir valores com base em uma condição, você pode usar o operador ternário para uma sintaxe mais compacta.

~~~py
# Usando bloco if
x = 10
if x > 5:
    y = "maior que 5"
else:
    y = "menor ou igual a 5"

# Usando operador ternário
y = "maior que 5" if x > 5 else "menor ou igual a 5"
~~~

3. Decoradores: O uso de @decorator é um exemplo de açúcar sintático que torna a aplicação de decoradores mais legível e conveniente.

~~~py
@decorator
def minha_funcao():
    pass
~~~

4. Métodos mágicos: Python fornece uma série de métodos mágicos (ou dunder methods) que permitem definir comportamentos especiais para objetos. Eles começam e terminam com dois underscores (__). Isso inclui métodos como __init__, __str__, __len__, entre outros. Eles fornecem uma maneira mais intuitiva de interagir com objetos em Python.

~~~py
class MinhaClasse:
    def __init__(self, valor):
        self.valor = valor

    def __str__(self):
        return f"Valor: {self.valor}"

objeto = MinhaClasse(42)
print(objeto)  # Isso chama automaticamente o método __str__
~~~

Esses são apenas alguns exemplos de açúcar sintático em Python. Eles ajudam a tornar o código mais limpo, legível e expressivo, o que é uma das razões pelas quais Python é considerado uma linguagem fácil de aprender e usar.

---