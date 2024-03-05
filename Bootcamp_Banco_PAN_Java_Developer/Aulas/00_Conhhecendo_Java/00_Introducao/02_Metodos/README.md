## Java Sintaxe - Métodos

*Todas as ações das aplicações são consideradas métodos.*

*Uma classe é definida por atributos e métodos. Já vimos que atributos são, em sua grande maioria, variáveis de diferentes tipos e valores. Os métodos por sua vez, correspondem a **funções** ou **sub-rotinas** disponíveis dentro de nossas classes*

##### Critérios de nomeação de Métodos

*Esses critérios não são obrigatórios, mas é recomendável que sejam seguidos, pois essas convenções facilitam a vida dos programadores ao trabalharem em códigos de forma colaborativa.*

* *Deve ser nomeado como verbo*
* *Segui o padrão camelCase (Todas as letras minúsculas com a exceção da primeira letra da segunda palavra)*

##### Exemplos:

~~~java
somar (int n1, int n2){}

abriConexao(){}

concluirProcessamento() {}

findById (int id){}

calcularImprimir(){} 
// há algo de errado neste método, confito de responsabilidades, ou calcular ou imprimir
~~~

*Abaixo temos um exemplo de uma classe com dois métodos e suas respectivas considerações:*

~~~java
public class MyClass {
    
    public double somar(int num1, int num2){
        // LOGICA - FINALIDADE DO MÉTODO
        return ... ;
    }
    public void imprimir(String texto){
        // LOGICA - FINALIDADE DO MÉTODO
        // AQUI NÃO PRECISA DO RETURN
        // POIS NÃO SERÁ RETORNADO NENHUM RESULTADO
    }
    // throws Exception : indica que o método ao ser utilizado poderá gerar uma exceção
    public double dividir(int dividendo, int divisor) throws Exception{}
    
    // Este método não pode ser visto por outras classes
    private void metodoPrivado(){}
}
~~~

