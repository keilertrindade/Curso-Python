"""

Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valodres somados:
Se uma lista for maior que a outra. a sp,a s[p vai considerar o tamanho da menor


"""

lista_a = [1, 2, 3, 4, 5, 6]
lista_b = [4, 5, 5, 9]

#listas = zip(lista_a, lista_b)
soma = [x + y for x, y in zip(lista_a, lista_b)]
print(soma)


