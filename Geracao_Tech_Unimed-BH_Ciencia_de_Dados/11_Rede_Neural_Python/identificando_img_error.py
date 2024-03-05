from PIL import Image
import os

diretorio_imagens = 'dataset/validation/cat'

arquivos_corrompidos = []

for arquivo in os.listdir(diretorio_imagens):
    caminho_arquivo = os.path.join(diretorio_imagens, arquivo)
    try:
        with Image.open(caminho_arquivo) as img:
            img.verify()  # Verifica se a imagem é válida sem carregá-la completamente
    except (IOError, SyntaxError) as e:
        print(f'Arquivo corrompido: {caminho_arquivo} - {e}')
        arquivos_corrompidos.append(caminho_arquivo)

# Se necessário, salve a lista de arquivos corrompidos para um arquivo de texto para análise posterior
if arquivos_corrompidos:
    with open('arquivos_corrompidos.txt', 'w') as f:
        for arquivo in arquivos_corrompidos:
            f.write(f"{arquivo}\n")

print("Verificação concluída.")
