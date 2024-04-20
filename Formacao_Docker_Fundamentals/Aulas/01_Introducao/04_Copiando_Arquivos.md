
## Copiando arquivos para dentro de um container

Para copiar um arquivo ou diretório da máquina host para dentro de um container, você pode usar o comando docker cp seguindo esta sintaxe:

~~~bash
docker cp <caminho_no_host> <container_id_or_name>:<caminho_no_container>
~~~

Por exemplo, se você quiser copiar um arquivo chamado example.txt do seu host para um container chamado meu_container no diretório /app:

~~~bash
docker cp example.txt meu_container:/app/example.txt
~~~

---

## Copiando arquivos de um container para a máquina host:

Para copiar um arquivo ou diretório de um container para a máquina host, simplesmente inverta a ordem dos parâmetros no comando docker cp:

~~~bash
docker cp <container_id_or_name>:<caminho_no_container> <caminho_no_host>
~~~

Por exemplo, para copiar o arquivo example.txt de dentro do container meu_container para o diretório atual na máquina host:

~~~bash
docker cp meu_container:/app/example.txt .
~~~

*O ponto . no final do comando representa o diretório atual no host.*

Lembre-se de que para usar o comando docker cp, o container não precisa estar em execução se você estiver copiando arquivos para fora dele. No entanto, para copiar arquivos para dentro de um container, ele precisa estar em execução ou pelo menos criado (existe como um container, mesmo que parado).

Esses comandos são muito úteis para mover arquivos entre o host e o container sem a necessidade de configurar volumes compartilhados ou usar serviços de transferência de arquivos.

---