import java.io.IOException;
import java.util.Scanner;

public class CodigoResposta{
    
    public static void main(String[] args) throws IOException {
        Scanner leitor = new Scanner(System.in);
        double A = leitor.nextDouble();
        double B = leitor.nextDouble();
        double C = leitor.nextDouble();
        double maior;
        double soma;
        boolean triangulo;
        
        if (A < B + C && B < A + C && C < A + B) {
            triangulo = true;
            soma = A + B + C;
            System.out.println("Perimetro = " + String.format("%.1f", soma));
        } else {
            triangulo = false;
            double trapezio = ((A + B) * C) / 2;
            System.out.println("Area = " + String.format("%.1f", trapezio));
        }
    }
}
