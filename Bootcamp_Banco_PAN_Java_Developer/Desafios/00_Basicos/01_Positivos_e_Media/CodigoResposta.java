import java.io.IOException;
import java.util.Scanner;

public class CodigoResposta {
	
    public static void main(String[] args) throws IOException {
        Scanner leitor = new Scanner(System.in);
        int cont = 0;
        double media = 0;
        double soma = 0;

        for (int i = 0; i < 6; i++) {
            double nEntrada = leitor.nextDouble();

            if(nEntrada > 0){
                cont++;
                soma += nEntrada;
            }
        }

        media = (soma / cont);
        System.out.println(cont + " valores positivos");
        System.out.println(String.format("%.1f", media));
    }
}