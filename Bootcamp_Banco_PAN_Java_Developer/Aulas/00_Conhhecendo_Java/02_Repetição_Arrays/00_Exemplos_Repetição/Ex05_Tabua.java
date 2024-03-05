// Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer numero
// inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja a tabuada.
// A saida deve ser conforme o exemplo a baixo:

/*      Tabuada do 5
 *      5 x 1 = 5
 *      5 x 2 = 10
 *      ...
 *      5 x 10 = 50
 */     

import java.util.Scanner;

public class Ex05_Tabua {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        System.out.println("Escolha a tabuada: ");
        int tabuada = scan.nextInt();

        System.out.println("Tabuada do "+ tabuada);

        for(int i = 1; i <= 10; i++){
            System.out.println(tabuada + " x " + i + " = " + (tabuada*i));
        }
    }
}