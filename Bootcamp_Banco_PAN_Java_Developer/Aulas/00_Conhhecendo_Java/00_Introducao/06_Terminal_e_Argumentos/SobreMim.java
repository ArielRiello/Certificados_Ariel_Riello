import java.util.Locale;
import java.util.Scanner;

public class SobreMim {
    public static void main(String[] args){
    
        try (Scanner scanner = new Scanner(System.in).useLocale(Locale.US)) {
            System.out.println("Digite seu nome: ");
            String nome = scanner.next();

            System.out.println("Digite seu sobre nome: ");
            String sobreNome = scanner.next();

            System.out.println("Digite sua idade: ");
            int idade = scanner.nextInt();

            System.out.println("Digite sua altura: ");
            double altura = scanner.nextDouble(); 

            System.out.println("Ola, me chamo " + nome + " " + sobreNome);
            System.out.println("Tenho " + idade + " anos ");
            System.out.println("Minha altura é " + altura + "cm ");
        }
    }
}
