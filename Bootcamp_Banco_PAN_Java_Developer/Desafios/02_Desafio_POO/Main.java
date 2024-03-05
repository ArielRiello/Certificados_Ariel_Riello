import java.time.LocalDate;

import Desafio_POO_Dio.Bootcamp;
import Desafio_POO_Dio.Curso;
import Desafio_POO_Dio.Dev;
import Desafio_POO_Dio.Mentoria;

public class Main {

    public static void main(String[] args) {
        
        Curso curso1 = new Curso();
        curso1.setTitulo("curso java");
        curso1.setDescricao("descricao curso de java");
        curso1.setCargaHoraria(8);

        Curso curso2 = new Curso();
        curso2.setTitulo("curso js");
        curso2.setDescricao("descricao curso de js");
        curso2.setCargaHoraria(4);

        System.out.println(curso1);
        System.out.println(curso2);

        Mentoria mentoria1 = new Mentoria();
        mentoria1.setTitulo("curso java");
        mentoria1.setDescricao("descricao curso de java");
        mentoria1.setData(LocalDate.now());
    
        System.out.println(mentoria1);

        System.out.println("***------------------***");

        Bootcamp bootcamp1 = new Bootcamp();
        bootcamp1.setNome("Bootcamp Java Devloper");
        bootcamp1.setDescricao("Bootcamp para aprendizado de Java");
        bootcamp1.getConteudos().add(curso1);
        bootcamp1.getConteudos().add(curso2);
        bootcamp1.getConteudos().add(mentoria1);

        Dev dev01 = new Dev();
        dev01.setNome("Ariel");
        dev01.inscreverBootcamp(bootcamp1);
        System.out.println("Conteudos inscritos" + dev01.getConteudoInscritos());
        dev01.progredir();
        dev01.progredir();
        System.out.println("******");
        System.out.println("Conteudos inscritos" + dev01.getConteudoInscritos());
        System.out.println("Conteudos Concluidos" + dev01.getConteudosConcluidos());
        System.out.println("XP = " + dev01.calcularTotalXp());

        System.out.println("***------------------***");

        Dev dev02 = new Dev();
        dev02.setNome("Mirella");
        dev02.inscreverBootcamp(bootcamp1);
        System.out.println("Conteudos inscritos" + dev02.getConteudoInscritos());
        dev02.progredir();
        dev02.progredir();
        dev02.progredir();
        System.out.println("******");
        System.out.println("Conteudos inscritos" + dev02.getConteudoInscritos());
        System.out.println("Conteudos Concluidos" + dev02.getConteudosConcluidos());
        System.out.println("XP = " + dev02.calcularTotalXp());
    }
}