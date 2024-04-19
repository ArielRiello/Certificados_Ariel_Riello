
## Comandos Básicos Docker

### Verificar a Versão do Docker:

~~~bash
docker --version
~~~

ou

~~~bash
docker version
~~~

---

### Listar Todas as Imagens do Docker:

~~~bash
docker images
~~~

---

### Baixar uma Imagem do Docker (pull):

~~~bash
docker pull [nome_da_imagem]
~~~

*Substitua [nome_da_imagem] pelo nome da imagem que deseja baixar, por exemplo, ubuntu.*

---

### Executar um Container (run):

~~~bash
docker run [opções] [nome_da_imagem] [comando]
~~~

Por exemplo, para executar um container Ubuntu interativamente:

~~~bash
docker run -it ubuntu bash
~~~

---

### Listar Containers Ativos:

~~~bash
docker ps
~~~

---

### Listar Todos os Containers (ativos e inativos):

~~~bash
docker ps -a
~~~

---

### Parar um Container:

~~~bash
docker stop [container_id_ou_nome]
~~~

---

### Remover um Container:

~~~bash
docker rm [container_id_ou_nome]
~~~

Para remover containers inativos de uma vez só:

~~~bash
docker container prune
~~~

---

### Remover uma Imagem:

~~~bash
docker rmi [nome_da_imagem]
~~~

---

### Ver Logs de um Container:

~~~bash
docker logs [container_id_ou_nome]
~~~

---

### Executar Comandos em um Container Ativo (exec):

~~~bash
docker exec [opções] [container_id_ou_nome] [comando]
~~~

Por exemplo, para abrir um shell em um container ativo:

~~~bash
docker exec -it [container_id_ou_nome] bash
~~~

---

### Construir uma Imagem a partir de um Dockerfile (build):

~~~bash
docker build -t [nome_da_imagem]:[tag] [caminho_para_dockerfile]
~~~

*Substitua [nome_da_imagem]:[tag] pelo nome e tag que deseja dar à sua imagem e [caminho_para_dockerfile] pelo diretório onde o Dockerfile está localizado.*

---

### Verificar Uso de Recursos por Containers:

~~~bash
docker stats
~~~

---