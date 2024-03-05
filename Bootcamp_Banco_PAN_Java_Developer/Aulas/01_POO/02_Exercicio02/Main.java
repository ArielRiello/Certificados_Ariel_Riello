package Exercicio02;

public class Main {
    public static void main(String[] args) {
        
        Funcionario funcionario = new Funcionario();

        // Upcast
        Funcionario gerente = new Gerente();
        Funcionario vendedor = new Vendedor();
        Funcionario faxineiro = new Faxineiro();

        //Gerente gerente_ = new Funcionario(); (erro)
        Vendedor vendedor_ = (Vendedor) new Funcionario(); // Evitar downcast
    }
}
