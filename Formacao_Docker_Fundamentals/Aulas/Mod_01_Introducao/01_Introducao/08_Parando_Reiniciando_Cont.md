
## Parando e reiniciando um container

Parar e reiniciar um container Docker são operações comuns que podem ser feitas facilmente usando a linha de comando. Aqui está como você pode fazer isso:
Parar um Container

Para parar um container que está em execução, você usa o comando docker stop. Este comando sinaliza o processo principal dentro do container para encerrar graciosamente, permitindo que ele termine suas operações e libere recursos de forma limpa.

Comando:

~~~bash
docker stop <container_name_or_id>
~~~

Substitua <container_name_or_id> pelo nome ou ID do container que você deseja parar.

Exemplo:

~~~bash
docker stop meu_container
~~~

O Docker aguardará um tempo padrão (10 segundos) para que o container pare graciosamente antes de forçar a parada. Se você precisar de mais tempo para que o processo do container encerre corretamente, você pode especificar um tempo de espera usando a opção -t:

~~~bash
docker stop -t 30 meu_container
~~~

Este comando dá ao container 30 segundos para encerrar antes de forçá-lo a parar.
Reiniciar um Container

Para reiniciar um container que já está em execução ou parado, você pode usar o comando docker restart. Este comando irá parar o container se ele estiver em execução e então iniciá-lo novamente.

Comando:

~~~bash
docker restart <container_name_or_id>
~~~

Substitua <container_name_or_id> pelo nome ou ID do container que você deseja reiniciar.

Exemplo:

~~~bash
docker restart meu_container
~~~

Assim como com o comando stop, você pode especificar um tempo de espera para o encerramento do container antes que ele seja reiniciado:

~~~bash
docker restart -t 30 meu_container
~~~

Dicas Adicionais

* Verificar Status: Após parar ou reiniciar, você pode verificar o status do container com docker ps para containers ativos ou docker ps -a para ver todos os containers (ativos e inativos).
    
* Logs: Se você estiver tendo problemas para entender por que um container não está se comportando como esperado ao parar ou reiniciar, você pode verificar os logs do container usando docker logs <container_name_or_id>.

Esses comandos são essenciais para o gerenciamento diário de containers no Docker e são muito úteis em cenários de desenvolvimento, testes, e produção.

---