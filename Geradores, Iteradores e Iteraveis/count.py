"""
count - Itertools
Gera um contador que é um iterador sem fim, podendo usar a função next
a função range gera um iteravel


"""
import time
from types import GeneratorType
from itertools import count

#contador = count()
contador = count(start=5, step=2)
for valor in contador:
    print(round(valor, 2))
    time.sleep(0.5)
    if valor >= 10:
        break
