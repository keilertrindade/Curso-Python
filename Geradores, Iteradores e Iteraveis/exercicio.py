carrinho = []

carrinho.append(('Produto 1', 30))
carrinho.append(('Produto 2', 20))
carrinho.append(('Produto 3', 50))
carrinho.append(('Produto 4', 20))

soma = [x[1] for x in carrinho]
print(sum(soma))

#solução aula:
soma = sum([float(y) for x, y in carrinho])
print(soma)