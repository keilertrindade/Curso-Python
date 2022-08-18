from classes import *

banco_1 = Banco('Santander')
banco_2 = Banco('Itau')

cliente_1 = banco_1.criar_cliente('keiler', 26, 'Corrente', 200, 600)
cliente_2 = banco_1.criar_cliente('keiler', 26, 'Poupanca', 200)
cliente_3 = banco_1.criar_cliente('keiler', 26, 'Corrente', 200)
cliente_4 = banco_1.criar_cliente('keiler', 26, 'Poupanca', 200)
cliente_5 = banco_1.criar_cliente('keiler', 26, 'Corrente', 200)


# print(banco_1.agencias)
# print(banco_1.contas)


cliente_6 = banco_2.criar_cliente('keiler', 26, 'Corrente', 200)
cliente_7 = banco_2.criar_cliente('keiler', 26, 'Poupanca', 200)
cliente_8 = banco_2.criar_cliente('keiler', 26, 'Corrente', 200)
cliente_9 = banco_2.criar_cliente('keiler', 26, 'Poupanca', 200)
cliente_10 = banco_2.criar_cliente('keiler', 26, 'Corrente', 200)


# print(banco_2.agencias)
# print(banco_2.contas)
# print("###### ----- ###### ----- ###### -----")


print(cliente_1.conta.numero_conta)
banco_1.autenticar_saque(cliente_1, 500)
banco_2.autenticar_saque(cliente_9, 77)
