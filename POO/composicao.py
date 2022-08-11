from POO.classes.classes_composicao import Cliente, Endereco

cliente1 = Cliente('Luis', 32)
cliente1.insere_endereco('Belo Horizonte', 'MG')
print(cliente1.nome)
print(cliente1.lista_enderecos())
del cliente1
print()

cliente2 = Cliente('Maria', 55)
cliente2.insere_endereco('Salvador', 'BA')
cliente2.insere_endereco('Rio de Janeiro', 'RJ')
print(cliente2.nome)
print(cliente2.lista_enderecos())
print()


cliente3 = Cliente('João', 19)
cliente3.insere_endereco('São Paulo', 'SP')
print(cliente3.nome)
print(cliente3.lista_enderecos())
print('###################################################################')