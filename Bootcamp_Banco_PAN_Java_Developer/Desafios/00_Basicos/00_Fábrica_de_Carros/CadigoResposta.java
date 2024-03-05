import java.util.*;

public class CadigoResposta {

    public static void main(String[] args) {

	    Scanner scan = new Scanner(System.in);
      int custoFabrica = scan.nextInt();
	    int porcentagemDistribuidor = scan.nextInt();
	    int PercentualImpostos = scan.nextInt();

            int custoConsumidor;
     
            int Distribuidor;
            int ValorImpostos;

        ValorImpostos = (custoFabrica * PercentualImpostos) / 100;
 
        Distribuidor = (custoFabrica * porcentagemDistribuidor) / 100;
      
        custoConsumidor = (custoFabrica + Distribuidor + ValorImpostos);
 
        System.out.println(custoConsumidor);
	}
}