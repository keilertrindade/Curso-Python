"""class Arquivo:
    def __init__(self, arquivo, modo):
        self.arquivo = open(arquivo, modo)

    def __enter__(self):
        return self.arquivo

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.arquivo.close()


with Arquivo('abc.txt', 'w') as arquivo:
    arquivo.write('Alguma coisa')

"""

from contextlib import contextmanager

def abrir(arquivo, modo):
    try:
        arquivo = open(arquivo,modo)
        yield arquivo
    finally:
        arquivo.close()


with abrir('abc.txt', 'w') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.write('Linha 3\n')