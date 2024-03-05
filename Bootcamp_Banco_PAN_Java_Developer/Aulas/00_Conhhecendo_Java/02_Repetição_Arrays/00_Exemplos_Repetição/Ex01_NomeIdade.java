import java.util.Scanner;

// Faça um programa que leia conjuntos de dois valores, o primeiro
// representando o nome do auno e o segundo representando a sua idade.
// Pare o programa inserindo o vaor 0 no campo nome.

public class Ex01_NomeIdade {

    public static void main (String[] args) {
        
        Scanner scan = new Scanner(System.in);

        while(true){
            System.out.println("Nome: ");
            String nome = scan.next();
            if (nome.equals("0")) break;

            System.out.println("Idade: ");
            int idade = scan.nextInt();

        }

        System.out.println("Contina aqui....");   

    }
}