from POO.classes.classes_agregacao import CarrinhoDeCompras, Produto


carrinho = CarrinhoDeCompras()

p1 = Produto('Camiseta', 50)
p2 = Produto('Iphone', 10000)
p3 = Produto('Caneca', 15)

carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)
carrinho.inserir_produto(p1)


print(carrinho.lista_produto())
print(f'R$: {carrinho.soma_total()}')
#
