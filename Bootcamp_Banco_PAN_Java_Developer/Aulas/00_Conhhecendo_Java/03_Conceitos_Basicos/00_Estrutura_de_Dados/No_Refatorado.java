public class No<T> {
    private T conteudo;
    private No<T> proximoNo;

    public No(T conteudo){
        this.proximoNo = null;
        this.conteudo = conteudo;
    }

    public T getConteudo(){
        return conteudo;
    }

    public void setConteudo(T conteudo){
        this.conteudo = conteudo;
    }

    public No<T> getProximNo(){
        return proximoNo;
    }

    public void setProximoNo(No<T> proxiNo){
        this.proximoNo = proxiNo;
    }

    @Override
    public String toString(){
        return "No{" +
            "conteudo=" + conteudo + '\'' + '}';
    }
}