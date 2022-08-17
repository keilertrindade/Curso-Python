from classes import *

# cc = ContaCorrente(1111, 2222, 100)

conta = ContaCorrente(1111, 2222, 100, 300)
cliente = Cliente('Keiler', 10, conta)
cliente.conta.sacar(301)
cliente.conta.depositar(201)


