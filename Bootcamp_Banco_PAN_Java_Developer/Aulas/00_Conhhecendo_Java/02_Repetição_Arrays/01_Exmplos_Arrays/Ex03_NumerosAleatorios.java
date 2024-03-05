
// Faça um programa que leia 20 numeros inteiros aleatórios (entre 0 - 100) armazene-os
// num vetor. Ao final mostre os números e seus sucessores.

import java.util.Random;


public class Ex03_NumerosAleatorios {
    public static void main(String[] args) {
        java.util.Random random = new Random();

        int[] numerosAleatorios = new int[20];

        for (int i = 0; i < numerosAleatorios.length; i++){
            int numero = random.nextInt(100);
            numerosAleatorios[i] = numero;
        }
        System.out.print("Numeros aleatórios: ");
        for (int numero : numerosAleatorios) {
            System.out.print(numero + " ");
        }
        System.out.print("\nSucessores dos numeros aleatórios: ");
        for (int numero : numerosAleatorios) {
            System.out.print((numero + 1) + " ");
        }
    }
}
