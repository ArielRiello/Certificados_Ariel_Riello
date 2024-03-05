import java.util.Scanner;

public class CodigoResposta {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.nextLine();
        String[] strSplit = str.split(" ");
        char[] arrVogais = {'a', 'e', 'i', 'o', 'u'};
        int espacosEmBranco = strSplit.length - 1, quantVogais = 0;
        for (String item : strSplit) {
            for (char vogal : arrVogais) {
                quantVogais += item.toLowerCase().chars().filter(ch -> ch == vogal).count();
            }
        }
        System.out.println("Espacos em branco: " + espacosEmBranco + " Vogais: " + quantVogais);
    }
}
