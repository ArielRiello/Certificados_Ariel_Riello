from PIL import Image
import os

diretorio_imagens = ''

for arquivo in os.listdir(diretorio_imagens):
    caminho_arquivo = os.path.join(diretorio_imagens, arquivo)
    try:
        with Image.open(caminho_arquivo) as img:
            img.verify()
    except (IOError, SyntaxError) as e:
        print(f'Excluindo arquivo corrompido: {caminho_arquivo} - {e}')
        os.remove(caminho_arquivo)

print("Limpeza de arquivos corrompidos concluída.")