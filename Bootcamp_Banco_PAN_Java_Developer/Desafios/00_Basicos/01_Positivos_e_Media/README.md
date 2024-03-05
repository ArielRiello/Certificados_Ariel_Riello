## DESAFIO: Fábrica de Carros

### Desafio: 
Leia 6 valores. Em seguida, mostre quantos destes valores digitados foram positivos. Na próxima linha, deve-se mostrar a média de todos os valores positivos digitados, com um dígito após o ponto decimal.

### Entrada:
A entrada contém 6 números que podem ser valores inteiros ( int ) ou de ponto flutuante ( float ou double ). Pelo menos um destes números será positivo.

### Saida:
O primeiro valor de saída é a quantidade de valores positivos. A próxima linha deve mostrar a média dos valores positivos digitados.

#### **Exemplo**

~~~
Entrada     |     Saida
   7                4 valores positivos
  -5                7.4
   6
  -3.4
   4.6
  12
~~~

#### Código do Desafio

~~~java
// Para ler e escrever dados em Java, aqui na DIO padronizamos da seguinte forma: 
// - new Scanner(System.in): cria um leitor de Entradas, com métodos úteis com prefixo "next";
// - System.out.println:.imprime um texto de Saída (Output) e pulando uma linha.  


import java.io.IOException;
import java.util.Scanner;

public class DIO {
	
  public static void main(String[] args) throws IOException {
     Scanner leitor = new Scanner(System.in);
     int cont = 0;
     double media = 0;
     double x;

     //TODO: Implemente as condições adequadas para obter a quantidade 
    //de valores positivos e a média dos valores positivos:
        for () {
        	

        	}
        }
        
        media = ;
        System.out.println(cont + " valores positivos");
        System.out.println(String.format("%.1f", media));
    }
	
}
~~~