
// Faça um programa que peça uma nota, entre zero e dez.
// Mostre uma mensagem caso o valor seja inváido e continue 
// pedindo até que o usuário informe um valor valido.

import java.util.Scanner;

public class Ex02_Nota {
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);

        int nota;
        
        System.out.println("Nota :");
        nota = scan.nextInt();

        while(nota < 0 | nota > 10){
            System.out.println("Nota Inválida! Digite novamente: ");
            nota = scan.nextInt();
        }
    }
}
