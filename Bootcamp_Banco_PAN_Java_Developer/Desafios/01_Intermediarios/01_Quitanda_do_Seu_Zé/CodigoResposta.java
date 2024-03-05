import java.util.*;

public class CodigoResposta {

    public static void main(String[] args) {
    
        Scanner input = new Scanner(System.in);
        int morangos = input.nextInt();
        int macas = input.nextInt();
    
        double valorMorango = 2.5;
        double valorMacas = 1.8;
        double valorCompra;

        double totalMorango = 0.0;
        double totalMacas = 0.0;
        double totalCompra;
        int totalKg;

        totalKg = morangos + macas;
        
        if (morangos > 5) {
            valorMorango = 2.20;
            totalMorango = morangos * valorMorango;
        } else {
            totalMorango = morangos * valorMorango;
        }

        if (macas > 5) {
            valorMacas = 1.5;
            totalMacas = macas * valorMacas;
        } else {
            totalMacas = macas * valorMacas;
        }

        valorCompra = totalMorango + totalMacas;

        if (valorCompra >= 25 || totalKg >= 8) {
            totalCompra = valorCompra - (valorCompra * 0.1);
            System.out.println(totalCompra);
        } else {
            System.out.println(valorCompra);
        }
    }
}