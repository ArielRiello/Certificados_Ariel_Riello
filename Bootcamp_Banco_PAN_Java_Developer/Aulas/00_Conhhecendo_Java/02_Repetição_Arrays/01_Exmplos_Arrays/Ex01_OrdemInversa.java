
// Crie um vetor de 6 numeros inteiros e mostre a ordem inversa.

public class Ex01_OrdemInversa {
    public static void main(String[] args) {
        int[] vetor = {1, 2, 3, 4, 5, 6};

        int contador = 0;
        System.out.print("Vetor: ");
        while(contador < (vetor.length)){
            System.out.print(vetor[contador]);
            contador++; 
        }

        System.out.print("\nVetor Invertido: ");
        for (int i = (vetor.length - 1); i>= 0; i--){
            System.out.print(vetor[i]);
        }
    }
}