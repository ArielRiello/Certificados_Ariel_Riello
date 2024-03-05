// Faça um programa que faça N números inteiros, calcule e mostre a quantidade
// de números pares e a quantidade de números impares.

import java.util.Scanner;

public class Ex04_ParImpar {
    
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);

        int qtdNumeros; 
        int numero;
        int qtdPares = 0;
        int qtdImpares = 0;
    
        System.out.println("Quantidade de numeros: ");
        qtdNumeros = scan.nextInt();

        int contador = 0;
        do {
            System.out.print("Número: ");
            numero = scan.nextInt();

            if (numero % 2 == 0) qtdPares++;
            else qtdImpares++;

            contador++;
            
       } while(contador < qtdNumeros);

       System.out.println("Pares: " + qtdPares);
       System.out.println("Impares: " + qtdImpares);
    }
}
