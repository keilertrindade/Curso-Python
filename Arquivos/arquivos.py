"""
Uso basico de leitura e formas de escrita
file = open('abc.txt', 'w+')
file.write('Linha 1\n')
file.write('Linha 2\n')
file.write('Linha 3\n')


file.seek(0, 0)
print('Lendo linhas')
print(file.read())
file.seek(0, 0)
print('#############')
print(file.readline(), end='') # Ler linha por linha
print(file.readline())
file.seek(0, 0)
print(file.readlines()) # Cria lista com todas as linhas
file.close()

"""

"""

Usando com try/exception

try:
    file = open('abc.txt', 'w+')
    file.write('Linha')
    file.seek(0, 0)
    print(file.read())
finally:
    file.close()

"""
"""
#Forma correta

with open('abc.txt', 'w+') as file:
    file.write('Linha 1\n')
    file.write('Linha 2\n')
    file.write('Linha 3\n')

    file.seek(0)
    print(file.read())

"""

import json

d1 = {
    'Pessoa 1': {
        'nome': 'Keiler',
        'idade': 26,
    },
    'Pessoa 2': {
        'nome': 'Rose',
        'idade': 30,
    },
}

d1_json = json.dumps(d1, indent=True)

with open('abc.json', 'w+') as file:
    file.write(d1_json)
