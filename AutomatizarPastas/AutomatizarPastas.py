import os
import shutil

diretorio_base = r'E:\Users\DEV\Desktop\teste'
lista_arquivos = os.listdir(diretorio_base)
lista_anexos = []
contador = 0
#print(lista_arquivos)

for lista in lista_arquivos:
    if lista_arquivos[contador].find("ANEXO") == -1:
        nome_pasta = lista_arquivos[contador].replace(".pdf", "")
        nova_pasta = os.path.join(diretorio_base, nome_pasta)
        os.makedirs(nova_pasta)
        origem = diretorio_base + '\\' + lista_arquivos[contador]
        destino = diretorio_base + '\\' + nome_pasta + '\\' + lista_arquivos[contador]
        shutil.move(origem, destino)
    else:
        lista_anexos.append(lista_arquivos[contador])
        # print(lista_arquivos[contador], nova_pasta)
    contador += 1

#print(lista_anexos)
contador = 0

for lista in lista_anexos:
    posicao = lista_anexos[contador].find(". ANEXOS")
    pasta = lista_anexos[contador][0:posicao]

    origem = diretorio_base + '\\' + lista_anexos[contador]
    destino = diretorio_base + '\\' + pasta + '\\' + lista_anexos[contador]
    shutil.move(origem, destino)
    contador += 1
