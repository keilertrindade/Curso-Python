from classes import *

# cc = ContaCorrente(1111, 2222, 100)

"""conta = ContaCorrente(1111, 2222, 100, 300)
cliente = Cliente('Keiler', 10, conta)
cliente.conta.sacar(301)
cliente.conta.depositar(201)"""


banco_1 = Banco('Santander')
banco_2 = Banco('Itau')

cliente_1 = banco_1.criar_cliente('keiler', 26, 'Corrente', 200)
cliente_2 = banco_1.criar_cliente('keiler', 26, 'Poupanca', 200)
cliente_3 = banco_1.criar_cliente('keiler', 26, 'Corrente', 200)
cliente_4 = banco_1.criar_cliente('keiler', 26, 'Poupanca', 200)
cliente_5 = banco_1.criar_cliente('keiler', 26, 'Corrente', 200)

print(banco_1.agencias)
print(banco_1.contas)

cliente_1 = banco_2.criar_cliente('keiler', 26, 'Corrente', 200)
cliente_2 = banco_2.criar_cliente('keiler', 26, 'Poupanca', 200)
cliente_3 = banco_2.criar_cliente('keiler', 26, 'Corrente', 200)
cliente_4 = banco_2.criar_cliente('keiler', 26, 'Poupanca', 200)
cliente_5 = banco_2.criar_cliente('keiler', 26, 'Corrente', 200)

print("###### ----- ###### ----- ###### ----- ###### ----- ")

print(banco_2.agencias)
print(banco_2.contas)

"""cliente_1.conta.sacar(290)
cliente_1.conta.depositar(180)
print(cliente_1.__dict__)"""