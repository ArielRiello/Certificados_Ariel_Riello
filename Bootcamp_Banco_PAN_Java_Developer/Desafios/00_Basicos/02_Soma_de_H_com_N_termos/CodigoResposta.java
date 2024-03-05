import java.util.Scanner;

public class CodigoResposta {

    public static void main(String[] Args) {

        double h = 0;
        Scanner sc = new Scanner(System.in);
        double n = sc.nextDouble();

        for (int i = 1; i <= n; i++) {
            double x = 1.0 / i;
            h += x;
        }
        System.out.println(h);
        int hInt = (int) Math.round(h);
        System.out.println(hInt);
    }
}
