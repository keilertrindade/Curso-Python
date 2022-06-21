import os
import shutil
from PyPDF2 import PdfFileWriter, PdfFileReader
import sys

""" 
pip install --user PyPDF2
python -m pip install --upgrade pip
"""

"""
 - Verificar número de páginas -> Ok
 - Número de páginas < 500 -> cria cópia
 - Páginas entre 500 e 800 -> Divide na metade
 - Páginas > 800 -> Vai criando arquivo novo a cada 500 páginas 

"""

if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")


diretorio_base = input(r'Digite o caminho da pasta: ')
lista_arquivos = os.listdir(diretorio_base)
lista_anexos = []
contador = 0


for lista in lista_arquivos:
    if lista_arquivos[contador].find("ANEXO") == -1:
        nome_pasta = lista_arquivos[contador].replace(".pdf", "")
        nova_pasta = os.path.join(diretorio_base, nome_pasta)
        # os.makedirs(nova_pasta)
        origem = diretorio_base + '\\' + lista_arquivos[contador]
        destino = diretorio_base + '\\' + nome_pasta + '\\' + lista_arquivos[contador]

        """
        Após mover, nesse mesmo laço já posso realizar as alterações no PDF -> Nesse teste vou percorrer apenas 
        mostrando o número de páginas de cada arquivo
        """

        leitor = PdfFileReader(open(origem, 'rb'))
        print(nome_pasta, leitor.getNumPages())

        # shutil.move(origem, destino)
    else:
        lista_anexos.append(lista_arquivos[contador])
    contador += 1

contador = 0
for lista in lista_anexos:
    posicao = lista_anexos[contador].find(". ANEXOS")
    pasta = lista_anexos[contador][0:posicao]

    origem = diretorio_base + '\\' + lista_anexos[contador]
    destino = diretorio_base + '\\' + pasta + '\\' + lista_anexos[contador]

    leitor = PdfFileReader(open(origem, 'rb'))
    print(lista_anexos[contador], leitor.getNumPages())

    #shutil.move(origem, destino)
    contador += 1