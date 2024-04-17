def principal():
    print('executando a funcao principal')

    def funcao_interna_1():
        print('executando a funcao_interna_1')

    def funcao_interna_2():
        print('executando a funcao_interna_2')

    funcao_interna_1()
    funcao_interna_2()

principal()