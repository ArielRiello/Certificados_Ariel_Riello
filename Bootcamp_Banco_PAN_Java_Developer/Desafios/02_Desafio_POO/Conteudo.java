package Desafio_POO_Dio;

public abstract class Conteudo { // Classe MÃE de Curso e Mentoria

    protected static final double XP_PADRAO = 10;

    private String titulo;
    private String descricao;

    public abstract double calcularXp();

    public String getTitulo() {
        return titulo;
    }
    public void setTitulo(String titulo) {
        this.titulo = titulo;
    }

    public String getDescricao() {
        return descricao;
    }
    public void setDescricao(String descricao) {
        this.descricao = descricao;
    }
}
