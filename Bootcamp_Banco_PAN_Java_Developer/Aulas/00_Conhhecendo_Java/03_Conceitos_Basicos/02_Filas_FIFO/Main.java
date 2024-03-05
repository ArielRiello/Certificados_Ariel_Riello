package FilasExCodigo;

public class Main {
    public static void main(String[] args) {
        Fila minhaFIla = new Fila();

        minhaFIla.enqueue(new No("primeiro"));
        minhaFIla.enqueue(new No("segundo"));
        minhaFIla.enqueue(new No("terceiro"));
        minhaFIla.enqueue(new No("quarto"));

        System.out.println(minhaFIla);

        System.out.println(minhaFIla.dequeue());

        System.out.println(minhaFIla);
    }
}
