lista = [
    ('chave', 'valor'),
    ('chave2', 'valor2')
]

""" Podemos usar a função dict 'd1.dict(lista)' para criar um dicionário.
    Mas usando dictionary comprehensive podemos processar dados enquanto criamos ele
 """

# d1 = {x: y for x,y in lista}
# d1 = {x: y.upper() for x, y in lista}
# d1 = {x: y for x, y in enumerate(range(5))}
# d1 = {x for x in range(5)}  # Cria um set
d1 = {f'chave_{x}': x**2 for x in range(5)}

print(d1)


d2 = dict(lista)
print(d2)

