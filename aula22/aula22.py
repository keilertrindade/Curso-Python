""""
Split, Join, Enumerate

* Split - Dividir a string #str
* Join - Juntar uma lista #str
* Enumerate - Enumera elementos de uma lista #list (objetos iteraveis)

"""


"""lista = [
    [1, 2],
    [3, 4],
    [5, 6],

]


for indice, valor in enumerate(lista):
    print(indice, valor)
"""
"""
# indices  0      1        2
lista = [
    ['Edu', 'João', 'Luiz'],
    ['Maria', 'Aline', 'Joana'],
    ['Helena', 'Ed', 'Lu'],
]

for v1 in enumerate(lista):
    valor_enumerado, minha_lista = v1
    nome1, nome2, nome3 = minha_lista
    print(valor_enumerado, minha_lista, nome1, nome2, nome3)



print(enumerada[1][0])

[
(0, ['Edu', 'João', 'Luiz']), 
(1, ['Maria', 'Aline', 'Joana']), 
(2, ['Helena', 'Ed', 'Lu'])
]
"""


"""lista = ['Edu', 'João', 'Luiz', 1, 2, 3, 4, 5, 6, 7, 8, 9]
n1, n2, n3,  *_ = lista

print(_)
"""

x = 10
y = "Keiler"
z = "Trindade"
x, y, z = z, x, y

print(f'X = {x}, Y = {y} e Z = {z}')

