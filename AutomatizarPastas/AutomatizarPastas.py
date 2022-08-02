import os
import shutil
from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger, PageRange
import sys

""" arquivo a ser editado - arquivo de destino - nome da pasta"""
def dividirPdf (origem, nova_pasta, nome_arquivo):
    leitor = PdfFileReader(open(origem, 'rb'))
    gravador: PdfFileWriter = PdfFileWriter()
    # print(nome_pasta, leitor.getNumPages())
    num_paginas = leitor.getNumPages()

    if num_paginas < 500:
        for page in range(num_paginas):
            gravador.addPage(leitor.getPage(page))

        caminho = os.path.join(nova_pasta, nome_arquivo + " - Copia.pdf")
        resultado = open(caminho, 'wb')
        gravador.write(resultado)
        resultado.close()

    elif num_paginas < 800:
        partes = num_paginas // 2
        merge = PdfFileMerger()

        range_paginas = '0:' + str(partes)
        merge.append(leitor, pages=PageRange(range_paginas))
        caminho = os.path.join(nova_pasta, nome_arquivo + "_split_1.pdf")
        resultado = open(caminho, 'wb')
        merge.write(resultado)
        resultado.close()
        merge.close()

        merge = PdfFileMerger()
        range_paginas = str(partes) + ':'
        merge.append(leitor, pages=PageRange(range_paginas))
        caminho = os.path.join(nova_pasta, nome_arquivo + "_split_2.pdf")
        resultado = open(caminho, 'wb')
        merge.write(resultado)
        resultado.close()
        merge.close()

    else:
        merge = PdfFileMerger()
        partes = num_paginas // 500

        if num_paginas % 500 != 0:
            partes += 1

        inicio = 0
        final = 500
        cont = 0

        for parte in range(partes):
            merge = PdfFileMerger()

            if cont == partes - 1:
                range_paginas = str(inicio) + ':'
                merge.append(leitor, pages=PageRange(range_paginas))
                # merge.write()
            else:
                range_paginas = str(inicio) + ':' + str(final)
                merge.append(leitor, pages=PageRange(range_paginas))

            #caminho = nova_pasta + "_split_" + str(cont + 1) + ".pdf"
            caminho = os.path.join(nova_pasta, nome_arquivo + "_split_" + str(cont + 1) + ".pdf")
            resultado = open(caminho, 'wb')
            merge.write(resultado)
            resultado.close()
            merge.close()
            inicio += 500
            final += 500
            cont += 1


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

# diretorio_base = input(r'Digite o caminho da pasta: ')
diretorio_base = r'E:\Users\DEV\Desktop\teste'
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

        # shutil.move(origem, destino)
        dividirPdf(destino, origem.replace(".pdf", ""), nome_pasta)

    else:
        lista_anexos.append(lista_arquivos[contador])
    contador += 1

contador = 0

for lista in lista_anexos:
    posicao = lista_anexos[contador].find(". ANEXOS")
    pasta = lista_anexos[contador][0:posicao]

    origem = diretorio_base + '\\' + lista_anexos[contador]
    destino = diretorio_base + '\\' + pasta + '\\' + lista_anexos[contador]
    shutil.move(origem, destino)

    # leitor = PdfFileReader(open(destino, 'rb'))
    # print(lista_anexos[contador], leitor.getNumPages())
    print(origem, destino)

    dividirPdf(destino, destino.replace(".pdf", ""), pasta)

    contador += 1
