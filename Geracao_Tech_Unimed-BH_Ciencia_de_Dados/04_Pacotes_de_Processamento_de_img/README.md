# Redimensionador de Imagens

Projeto Desenvolvido para o Curso: Geração Tech Unimed-BH - Ciência de Dados

Este pacote oferece uma maneira simples e eficiente de redimensionar imagens e converter entre diferentes formatos de arquivo de imagem. Construído sobre a biblioteca Pillow, ele permite a manipulação fácil de imagens para projetos Python.

## Modo de uso

Para redimensionar uma imagem:

~~~py
from redimensionador.core import redimensionar_imagem

redimensionar_imagem('caminho/para/imagem/original.jpg', 'caminho/para/imagem/redimensionada.jpg', (800, 600))
~~~

Para converter o formato de uma imagem:

~~~py
from redimensionador.core import converter_formato

converter_formato('caminho/para/imagem/original.jpg', 'caminho/para/imagem/convertida.png', 'PNG')
~~~

### Usando o pacote:

*Clone o repositório*

~~~CMD
git clone {URL DO REPOSITÓRIO}
cd redimensionador
pip install .
~~~