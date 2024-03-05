import java.io.IOException;
import java.util.Scanner;

public class CodigoResposta {

	public static void main(String[] args)  throws IOException {
		Scanner sc = new Scanner(System.in);
		
		String AN1,AN2,AN3;
		
		AN1 = sc.nextLine();
		AN2 = sc.nextLine();
		AN3 = sc.nextLine();

        if (AN1.equals("vertebrado")) {
            switch (AN2) {
                case "ave":
                    switch (AN3) {
                        case "carnivoro":
                            System.out.println("aguia");
                        break;
                        case "onivoro":
                            System.out.println("pomba");
                        break;
                    }
                break;
                case "mamifero":
                    switch (AN3) {
                        case "onivoro":
                            System.out.println("homem");
                        break;
                        case "herbivoro":
                            System.out.println("vaca");
                        break;
                    }
                break;

            }
        } else if (AN1.equals("invertebrado")) {
            switch (AN2) {
                case "inseto":
                    switch (AN3) {
                        case "hematofago":
                            System.out.println("pulga");
                        break;
                        case "herbivoro":
                            System.out.println("lagarta");
                        break;
                    }
                break;
                case "anelideo":
                    switch (AN3) {
                        case "hematofago":
                            System.out.println("sanguessuga");
                        break;
                        case "onivoro":
                            System.out.println("minhoca");
                        break;
                    }
                break;
            }
        }
    }
}
