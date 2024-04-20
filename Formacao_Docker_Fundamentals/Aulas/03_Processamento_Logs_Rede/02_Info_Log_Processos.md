
## Informações, logs e processos

Para gerenciar contêineres Docker eficientemente, é essencial conhecer comandos que permitam acessar informações sobre os contêineres, visualizar logs e monitorar processos internos. Aqui está uma visão geral de alguns comandos úteis para essas tarefas:

1. Comandos para Informações dos Contêineres

### docker ps

Lista todos os contêineres que estão atualmente em execução. Para ver todos os contêineres, incluindo os que estão parados, use docker ps -a.

~~~bash
docker ps
~~~

### docker inspect

Fornece informações detalhadas sobre um contêiner, incluindo configuração de rede, volumes montados, limites de recursos e muito mais. Você precisa especificar o ID ou nome do contêiner.

~~~bash
docker inspect nome_do_contêiner
~~~

### docker stats

Mostra um fluxo ao vivo de uso de recursos por contêiner, como CPU, uso de memória, rede, e mais.

~~~bash
docker stats
~~~

2. Comandos para Logs

### docker logs

Permite visualizar os logs de um contêiner. Isso é particularmente útil para depurar problemas ou monitorar a atividade de um contêiner. Você pode seguir os logs em tempo real com a opção -f.

~~~bash
docker logs nome_do_contêiner
docker logs -f nome_do_contêiner  # Para seguir os logs em tempo real
~~~

3. Comandos para Processos Internos

### docker top

Mostra os processos em execução dentro de um contêiner. É útil para obter uma visão rápida do que está acontecendo dentro do contêiner.

~~~bash
docker top nome_do_contêiner
~~~

### docker exec

Executa um comando dentro de um contêiner que está rodando. Este comando é extremamente útil para interagir diretamente com os processos dentro do contêiner. Por exemplo, para iniciar um shell bash dentro de um contêiner, você usaria:

~~~bash
docker exec -it nome_do_contêiner bash
~~~

Exemplo de Uso Combinado

Você pode combinar esses comandos para gerenciar e diagnosticar eficazmente seus contêineres. Por exemplo, se você quiser verificar a utilização de recursos de um contêiner, seguido por seus logs e então acessar um shell dentro dele para investigação adicional, poderia usar:

* docker stats nome_do_contêiner para ver a utilização de recursos.

* docker logs -f nome_do_contêiner para acompanhar os logs recentes.

* docker exec -it nome_do_contêiner bash para iniciar um shell e investigar mais a fundo.

Esses comandos ajudam a garantir que você pode monitorar e responder a problemas em seus contêineres de forma eficaz, mantendo suas aplicações rodando suavemente.

---