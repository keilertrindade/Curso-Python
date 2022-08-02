from dados import pessoas, produtos, lista
from functools import reduce

# nova_lista = [num * 2 for num in lista]
# # nova_lista = map(lambda x: x*2, lista)
# print(lista)
# print(list(nova_lista))

"""
MAP:

def aumenta_preco(p):
    p['preco'] = round(p['preco'] * 1.05, 2)
    return p

novos_produtos = map(aumenta_preco, produtos)

for produto in novos_produtos:
    print(produto)

nomes = map(lambda p: p['nome'], pessoas)
nomes = map(lambda p: p['idade'] * 1.20, pessoas)

for pessoas in nomes:
    print(pessoas)
    
----------------------------------------------
Filter

def filtra(produto):
    if produto['preco'] > 50:
        return True
    else:
        return False

def filtraP(pessoa):
    if pessoa['idade'] >= 18:
        return True
    else:
        return False



# nova_lista = filter(lambda produto: produto['preco'] > 50, produtos)
nova_lista = filter(filtra, produtos)
nova_lista_P = filter(filtraP, pessoas)


# for produto in nova_lista:
#     print(produto)

for pessoa in nova_lista_P:
    print(pessoa)

----------------------------------------------
Reduce

"""

# soma_lista = reduce(lambda ac, i: i + ac, lista, 0)
# print(soma_lista)

soma_produtos = reduce(lambda ac, p: p['preco'] + ac, produtos, 0)
print(soma_produtos / len(produtos))

soma_idades = reduce(lambda ac, p: p['idade'] + ac, pessoas, 0)
print(soma_idades / len(pessoas))
