from POO.classes.classes_agregacao import CarrinhoDeCompras, Produto


carrinho = CarrinhoDeCompras()
print(carrinho.__dict__)

p1 = Produto('Camiseta', 50)
p2 = Produto('Iphone', 10000)
p3 = Produto('Caneca', 15)

carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)
carrinho.inserir_produto(p1)

print(carrinho.__dict__)

# print(carrinho.lista_produto())
# print(carrinho.soma_total())
#
