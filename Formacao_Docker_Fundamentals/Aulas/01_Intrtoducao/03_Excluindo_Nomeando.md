
## Excluindo e Nomeando Containers

### Excluindo

Para excluir um container no Docker, você deve primeiro garantir que o container não esteja em execução. Se estiver, você precisará pará-lo. Aqui estão os comandos para fazer isso:

Para parar um container:

~~~bash
docker stop <container_name_or_id>
~~~

*Substitua <container_name_or_id> pelo nome ou ID do container que você deseja parar.*

### Para excluir um container:

Depois de parar o container, você pode excluí-lo com o seguinte comando:

~~~bash
docker rm <container_name_or_id>
~~~

*Assim como antes, substitua <container_name_or_id> pelo nome ou ID do container que você deseja remover.*

Se você deseja forçar a remoção de um container em execução (não recomendado a menos que necessário), você pode adicionar a opção -f:

~~~bash
docker rm -f <container_name_or_id>
~~~

---

### Nomeando

Para nomear um container, você usa a opção --name quando cria (ou executa) o container. Isso é útil para quando você quer se referir a um container por um nome fácil de lembrar, em vez de usar o ID do container.

Para nomear um container ao criá-lo:

~~~bash
docker run --name meu_container_nome <outras_opções> <imagem>
~~~

*Substitua meu_container_nome pelo nome que você deseja atribuir ao seu container, e <imagem> pela imagem Docker que você está usando para criar o container.*

Por exemplo, para executar um container do Ubuntu e nomeá-lo "meu-ubuntu":

~~~bash
docker run -it --name meu-ubuntu ubuntu bash
~~~

Isso iniciará um novo container a partir da imagem do Ubuntu com um shell interativo e você poderá se referir a ele com o nome "meu-ubuntu" ao usar outros comandos do Docker.

---