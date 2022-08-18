from abc import ABC, abstractmethod
from random import randint


class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor.title()

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, valor):
        if isinstance(valor, int):
            self._idade = valor
        else:
            raise ValueError('Idade precisa ser numérico')


class Cliente(Pessoa):
    def __init__(self, nome, idade, conta):
        super().__init__(nome, idade)
        self._conta = conta

    @property
    def conta(self):
        return self._conta


class Conta:
    def __init__(self, agencia, numero_conta, saldo):
        self._agencia = agencia
        self._numero_conta = numero_conta
        self._saldo = saldo

    @property
    def agencia(self):
        return self._agencia

    @property
    def numero_conta(self):
        return self._numero_conta

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if isinstance(valor, (int, float)):
            self._saldo = valor
        else:
            raise ValueError('Saldo precisa ser numérico')

    def depositar(self, valor):
        if isinstance(valor, (int, float)):
            self._saldo += valor
            print(f'Você depositou R$ {valor}, seu saldo é de R$ {self._saldo}')
        else:
            raise ValueError('Saldo precisa ser numérico')

    @abstractmethod
    def sacar(self):
        pass


class ContaPoupanca(Conta):
    def sacar(self, valor):
        if isinstance(valor, (int, float)):
            if valor <= self.saldo:
                self._saldo -= valor
                print(f'Você sacou R$ {valor}, seu saldo é de R$ {self._saldo}')
            else:
                print(f'Saldo insuficiente! Você tem apenas R$ {self._saldo} de saldo na conta')
        else:
            raise ValueError('Valor do saque precisa ser numérico!')


class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite=100):
        super().__init__(agencia, conta, saldo)
        self._limite = limite

    def sacar(self, valor):
        if isinstance(valor, (int, float)):
            if valor <= (self._saldo + self._limite):
                self._saldo -= valor
                print(f'Você sacou R$ {valor}, seu saldo é de R$ {self._saldo}')
            else:
                print(f'Saldo insuficiente! Você tem apenas R$ {self._saldo} de saldo na conta')
        else:
            raise ValueError('Valor do saque precisa ser numérico!')


class Banco:
    def __init__(self, nome):
        self._nome = nome
        self._agencias = self.criar_agencias()
        self._contas = []
        self._clientes = []

    def criar_cliente(self, nome, idade, tipo_conta, saldo, limite=100):
        num_conta = randint(10000, 99999)
        while num_conta in self._contas:
            num_conta = randint(10000, 99999)
        self._contas.append(num_conta)

        if tipo_conta == 'Corrente':
            # Perguntar limite aqui ?
            conta = ContaCorrente(self._agencias[randint(0, 4)], num_conta, saldo, limite)
        elif tipo_conta == 'Poupanca':
            conta = ContaPoupanca(self._agencias[randint(0, 4)], num_conta, saldo)

        cliente = Cliente(nome, idade, conta)
        self._clientes.append(cliente)

        return cliente

    @staticmethod
    def criar_agencias():
        agencias = []
        for ag in range(5):
            agencias.append(randint(10000, 99999))
        return agencias

    def autenticar_saque(self, cliente,
                         valor):  # Método de checagem, verifica com as informações do cliente se ele pertence nesse banco (?)
        conta = cliente.conta
        if conta._numero_conta in self._contas and conta._agencia in self._agencias and cliente in self._clientes:
            # print(f'Conta: {conta._numero_conta}')
            conta.sacar(valor)
        else:
            print(f'Cliente não está cadastrado no nosso banco!')

    @property
    def agencias(self):
        return self._agencias

    @property
    def contas(self):
        return self._contas


"""
Para melhorar posso usar randint para gerar as contas, verificando se não existe na lista daquele banco
E ai uso simplesmente a função gerar_cliente(?) do banco para dar um return no cliente com as informações que passamos
'nome' 'idade' 'tipo da conta' 'limite'  
"""
