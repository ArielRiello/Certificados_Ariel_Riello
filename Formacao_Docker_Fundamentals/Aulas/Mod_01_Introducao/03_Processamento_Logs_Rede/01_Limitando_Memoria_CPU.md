
## Limitando memória e CPU

Para limitar os recursos de CPU e memória de contêineres Docker, você pode usar opções específicas na linha de comando docker run. Esses controles ajudam a garantir que um contêiner não consuma recursos em excesso do host, permitindo uma melhor gestão dos recursos do sistema. Aqui estão os comandos para configurar limites de CPU e memória:

Limitando Memória

Para limitar a memória que um contêiner pode usar, você pode utilizar a opção --memory (ou -m) seguida do limite desejado. Por exemplo, para limitar um contêiner a usar no máximo 500 MB de memória, você usaria:

~~~bash
docker run -d \
  --memory 500m \
  nome_da_imagem
~~~

Limitando CPU

Para limitar o uso da CPU, você pode usar algumas opções diferentes dependendo de como deseja controlar o acesso ao processador.

1. Limitando a porcentagem de uso da CPU

Você pode usar a opção --cpus para especificar quantos CPUs (ou frações de CPUs) um contêiner pode usar. Por exemplo, se você quiser que o contêiner use no máximo um e meio CPUs, você faria:

~~~bash
docker run -d \
  --cpus 1.5 \
  nome_da_imagem
~~~

2. Limitando o uso de núcleos específicos da CPU

Para atribuir contêineres a núcleos específicos, você pode usar a opção --cpuset-cpus. Esta opção recebe uma lista de CPUs (como índices de CPU) para os quais o contêiner pode ser limitado. Por exemplo, para limitar o contêiner a usar apenas os núcleos 0 e 1, você usaria:

~~~bash
docker run -d \
  --cpuset-cpus 0,1 \
  nome_da_imagem
~~~

Exemplo Completo

Aqui está um exemplo de como você pode limitar tanto a memória quanto a CPU ao iniciar um contêiner:

~~~bash
docker run -d \
  --memory 256m \
  --cpus 0.5 \
  nome_da_imagem
~~~

Este comando executa um contêiner que está limitado a usar no máximo 256 MB de memória e meio CPU.
Verificando as Configurações de Recursos

Para verificar se as configurações de recursos estão sendo aplicadas corretamente, você pode inspecionar o contêiner com:

~~~bash
docker inspect nome_do_contêiner
~~~

Procure pelas seções CpuShares, CpuPeriod, CpuQuota, Memory e outras relacionadas à configuração de recursos para verificar os limites aplicados.

Essas opções de limitação são ferramentas cruciais para a gestão de recursos em ambientes onde múltiplos contêineres são executados no mesmo host, ajudando a evitar que um contêiner monopolize recursos e prejudique a performance dos demais.

---