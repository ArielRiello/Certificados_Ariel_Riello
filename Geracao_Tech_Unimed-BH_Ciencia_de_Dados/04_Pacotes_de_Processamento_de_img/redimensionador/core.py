from PIL import Image

def redimensionar_imagem(caminho_entrada, caminho_saida, tamanho):
    """Redimensiona a imagem para o tamanho especificado e salva no caminho de saída."""
    imagem = Image.open(caminho_entrada)
    imagem_redimensionada = imagem.resize(tamanho)
    # Converte para RGB se for RGBA (ou qualquer outro modo que não seja compatível com JPEG)
    if imagem_redimensionada.mode in ("RGBA", "LA") or (imagem_redimensionada.mode == "P" and "transparency" in imagem_redimensionada.info):
        imagem_redimensionada = imagem_redimensionada.convert("RGB")
    imagem_redimensionada.save(caminho_saida)

def converter_formato(caminho_entrada, caminho_saida, formato):
    """Converte a imagem para o formato especificado e salva no caminho de saída."""
    imagem = Image.open(caminho_entrada)
    # Converte para RGB se for RGBA (ou qualquer outro modo que não seja compatível com JPEG)
    if imagem.mode in ("RGBA", "LA") or (imagem.mode == "P" and "transparency" in imagem.info):
        imagem = imagem.convert("RGB")
    imagem.save(caminho_saida, formato)
