
## Criando Container MYSQL

Para criar um container MySQL, você geralmente irá usar a imagem oficial do MySQL disponível no Docker Hub. Aqui estão os passos para criar um container MySQL:

Puxe a Imagem do MySQL:

Primeiro, você precisa ter a imagem do MySQL. Você pode puxar a imagem mais recente usando o comando docker pull:

~~~bash
docker pull mysql
~~~

Você também pode especificar uma versão particular do MySQL adicionando uma tag após o nome da imagem:

~~~bash
docker pull mysql:5.7
~~~

Execute o Container MySQL:

Para executar o container MySQL, você usará o comando docker run, passando várias opções necessárias para configurar o MySQL:

* -e MYSQL_ROOT_PASSWORD: Define a senha do usuário root.
    
* -e MYSQL_DATABASE: (Opcional) Cria um banco de dados com o nome especificado ao iniciar o container.
    
* -e MYSQL_USER e -e MYSQL_PASSWORD: (Opcional) Cria um usuário e define a senha para esse usuário.
    
* --name: Dá um nome ao seu container.
    
* -p: Mapeia uma porta do host para uma porta do container.
    
* -d: Executa o container em modo de fundo (detached).

Aqui está um exemplo de comando que cria um container MySQL:

~~~bash
docker run --name meu-mysql -e MYSQL_ROOT_PASSWORD=minhasenha -p 3306:3306 -d mysql:5.7
~~~

Este comando cria um container chamado meu-mysql com uma senha de root minhasenha, mapeia a porta padrão do MySQL (3306) do container para a mesma porta no host, e utiliza a versão 5.7 da imagem do MySQL.

Verificar o Container:

Você pode verificar se o container está rodando corretamente com o comando docker ps e também pode ver os logs com docker logs meu-mysql para assegurar que o servidor MySQL dentro do container está funcionando como esperado.

Conectar-se ao MySQL:

Após o container ser iniciado, você pode se conectar ao servidor MySQL usando qualquer cliente MySQL. Se você estiver conectando-se localmente de sua máquina host, você pode usar localhost e a porta que mapeou (neste caso, 3306):

~~~bash
mysql -u root -p -h 127.0.0.1
~~~

Será solicitado que você insira a senha que você definiu com MYSQL_ROOT_PASSWORD.

Gerenciamento de Persistência de Dados:

Se você planeja manter os dados mesmo após o container ser excluído, você deve montar um volume. Isso pode ser feito com a opção -v ao executar o container:

~~~bash
docker run --name meu-mysql -v meu-volume-local:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=minhasenha -p 3306:3306 -d mysql
~~~

O comando acima montará um volume da sua máquina host (meu-volume-local) para o diretório de dados do MySQL (/var/lib/mysql) dentro do container, garantindo que os dados persistam entre as reinicializações e exclusões do container.

Lembre-se de substituir minhasenha pela senha que você quer usar para o usuário root do MySQL e meu-volume-local pelo caminho do diretório que você deseja usar para armazenar os dados do MySQL na sua máquina host.

---