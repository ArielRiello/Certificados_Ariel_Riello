def mensagem(nome):
    print('executando mensagem')
    return f'Oi {nome}'

def mensagem_longa(nome):
    print('executando mensagem_longa')
    return f'Olá tudo bem com você, {nome}?'

def executar(funcao, nome):
    print('executando executar')
    return funcao(nome)

print(executar(mensagem, 'Ariel'))
print(executar(mensagem_longa, 'Ariel'))