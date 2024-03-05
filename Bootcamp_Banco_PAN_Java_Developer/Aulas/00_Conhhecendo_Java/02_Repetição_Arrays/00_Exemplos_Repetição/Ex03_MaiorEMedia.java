
// Faça um programa que leia 5 numeros e informe
// maior numero e a média desses numeros.

import java.util.Scanner;


public class Ex03_MaiorEMedia {
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);

        int numero;
        int contador = 0;
        int maior = 0;
        int soma = 0;

        do {
            System.out. print("Número: ");
            numero = scan.nextInt();

            contador++;

            soma = soma + numero;

            if (numero > maior) maior = numero;

        } while(contador < 5);

        System.out.println("Maior: " + maior);
        System.out.println("Média: " + (soma/5));

    }
}
