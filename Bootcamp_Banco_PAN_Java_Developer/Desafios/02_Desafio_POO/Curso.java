package Desafio_POO_Dio;

public class Curso extends Conteudo{ // Classe FILHA de Conteudo

    @Override
    public double calcularXp() {
        return XP_PADRAO * cargaHoraria;
    }

    private int cargaHoraria;

    public Curso() {}

    public int getCargaHoraria() {
        return cargaHoraria;
    }
    public void setCargaHoraria(int cargaHoraria) {
        this.cargaHoraria = cargaHoraria;
    }

    @Override
    public String toString() {
        return "titulo = " + getTitulo() + " / " +
        "descricao = " + getDescricao() + " / " +
        "carga horaria = " + cargaHoraria;
    }

}