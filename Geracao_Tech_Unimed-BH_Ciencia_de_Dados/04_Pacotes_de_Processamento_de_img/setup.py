from setuptools import setup, find_packages

setup(
    name='redimensionador_imagem',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Pillow',
    ],
    description='Um pacote para redimensionar e converter formatos de imagens\
        para o projeto Criação de Pacotes de Processamento de Imagens em Python\
            do curso Geração Tech Unimed-BH - Ciência de Dados',
    author='Ariel Riello',
    author_email='riello.programmer@gmail.com',
)