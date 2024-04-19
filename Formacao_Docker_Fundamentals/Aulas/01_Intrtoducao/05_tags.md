
## Tags

Tags em Docker são utilizadas para identificar diferentes versões de uma imagem Docker. Elas funcionam como rótulos legíveis que apontam para uma versão específica de uma imagem dentro de um repositório. Cada imagem em um repositório pode ter múltiplas tags associadas a ela, e cada tag é única dentro do contexto de um repositório.

---

### Como funcionam as Tags

1. Identificação de Versão: Frequentemente, tags são usadas para indicar diferentes versões de uma aplicação ou diferentes estágios de desenvolvimento, como 2.1, 2.2, latest, stable, development, feature-xyz, etc.

2. Imutabilidade: Uma vez que uma imagem é marcada com uma tag específica e é enviada para um registro (por exemplo, Docker Hub), essa tag deveria ser imutável; ou seja, não deveria ser reutilizada para outra imagem. Se uma nova versão de uma imagem é construída, ela deve ser marcada com uma nova tag.

3. Tag latest: A tag latest é uma tag padrão que é dada a uma imagem quando uma tag não é especificada. Entretanto, latest pode ser enganoso; não significa necessariamente que a imagem é a versão mais recente, mas sim que é a versão mais recentemente marcada como latest.

4. Referenciando Imagens: Quando você executa um comando como docker pull ou docker run e não especifica uma tag, o Docker assume que você está se referindo à tag latest. Por exemplo, docker pull ubuntu é o mesmo que docker pull ubuntu:latest.

---

### Como Usar Tags

Para marcar uma imagem local com uma nova tag, você usa o comando docker tag:

~~~bash
docker tag <imagem_existente>:<tag_existente> <imagem_existente>:<nova_tag>
~~~

Por exemplo, se você tem uma imagem minha_imagem com a tag 1.0 e quer adicionar uma nova tag stable, você faria:

~~~bash
docker tag minha_imagem:1.0 minha_imagem:stable
~~~

Quando você constrói uma imagem com um Dockerfile, você pode especificar a tag diretamente no comando docker build:

~~~bash
docker build -t <meu_usuario>/<nome_da_imagem>:<tag> .
~~~

Aqui está um exemplo de como construir e marcar uma imagem:

~~~bash
docker build -t meu_usuario/minha_app:2.0 .
~~~

Isso cria uma imagem de minha_app com a tag 2.0.

Lembre-se de que é uma boa prática usar tags específicas para controle de versão para garantir que o mesmo código seja usado em todos os ambientes de implantação, reduzindo inconsistências e facilitando o rollback para versões anteriores, se necessário.

---