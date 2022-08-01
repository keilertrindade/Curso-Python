"""
Zip - Unindo iteráveis
Zip_longest - Itertools
"""
from itertools import zip_longest, count

cidades = ['São Paulo', 'Belo Horizonte', ' Salvador', 'Monte Belo']
estados = ['SP', 'MG', 'BA']
indice = count()

cidades_estados = zip_longest(
                              indice,
                              cidades,
                              estados,
                              fillvalue='Estado'
                              ) #função lista junta dois iteráveis, salvando num objeto zip

for valor in cidades_estados:
    print(valor)

