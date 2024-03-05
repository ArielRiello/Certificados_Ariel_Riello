package Desafio_POO_Dio;

import java.time.LocalDate;

public class Mentoria extends Conteudo{ // Classe FILHA de Conteudo

    @Override
    public double calcularXp() {
        return XP_PADRAO + 20d;
    }
    
    private LocalDate data;

    public Mentoria() {}

    public LocalDate getData() {
        return data;
    }
    public void setData(LocalDate data) {
        this.data = data;
    }

    @Override
    public String toString() {
        return "titulo = " + getTitulo() + " / " +
        "descricao = " + getDescricao() + " / " +
        "data = " + data;
    }

}
