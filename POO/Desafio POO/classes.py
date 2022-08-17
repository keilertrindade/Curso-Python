from abc import ABC, abstractmethod


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
    def __init__(self, agencia, conta, saldo):
        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo

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
    def __init__(self):
        self._agencias = []
        self._contas = []
        self._clientes = []

    def criar_cliente(self, nome, idade, tipo_conta, limite=100):
        pass

    def checar(self):  # Método de checagem, verifica com as informações do cliente se ele pertence nesse banco (?)
        pass

"""
Para melhorar posso usar randint para gerar as contas, verificando se não existe na lista daquele banco
E ai uso simplesmente a função gerar_cliente(?) do banco para dar um return no cliente com as informações que passamos
'nome' 'idade' 'tipo da conta' 'limite'  
"""
