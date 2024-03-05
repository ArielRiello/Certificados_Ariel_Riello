public class No {
    private String conteudo;
    private No proximoNo;

    public No(String conteudo){
        this.proximoNo = null;
        this.conteudo = conteudo;
    }

    public String getConteudo(){
        return conteudo;
    }

    public void setConteudo(String conteudo){
        this.conteudo = conteudo;
    }

    public No getProximNo(){
        return proximoNo;
    }

    public void setProximoNo(No proxiNo){
        this.proximoNo = proxiNo;
    }

    @Override
    public String toString(){
        return "No{" +
            "conteudo=" + conteudo + '\'' + '}';
    }
}