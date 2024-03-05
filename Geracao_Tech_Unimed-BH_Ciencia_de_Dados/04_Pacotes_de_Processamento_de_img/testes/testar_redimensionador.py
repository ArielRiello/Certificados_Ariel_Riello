import os
from redimensionador.core import redimensionar_imagem, converter_formato

# Função para garantir que o diretório de destino exista
def garantir_diretorio(caminho_saida):
    diretorio = os.path.dirname(caminho_saida)
    if not os.path.exists(diretorio):
        os.makedirs(diretorio)

# Caminhos de entrada e saída
caminho_entrada = 'testes/img_teste.png'
caminho_saida_redimensionada = 'testes/redimensionada.jpg'
caminho_saida_convertida = 'testes/convertida.jpg'

# Garante que o diretório de destino exista
garantir_diretorio(caminho_saida_redimensionada)
garantir_diretorio(caminho_saida_convertida)

# Teste de redimensionamento
redimensionar_imagem(caminho_entrada, caminho_saida_redimensionada, (800, 600))

# Teste de conversão de formato
converter_formato(caminho_entrada, caminho_saida_convertida, 'JPEG')