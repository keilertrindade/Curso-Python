from abc import ABC, abstractmethod


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @property
    def nome(self):
        return self.nome

    @nome.setter
    def nome(self, valor):
        self.nome = valor.title()

    @property
    def idade(self):
        return self.idade

    @idade.setter
    def idade(self, valor):
        if isinstance(valor, int):
            self.idade = valor
        else:
            raise ValueError('Idade precisa ser numérico')


class Conta:
    def __init__(self, agencia, conta, saldo):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    @property
    def saldo(self):
        return self.saldo

    @saldo.getter
    def saldo(self, valor):
        if isinstance(valor, (int, float)):
            self.saldo = valor
        else:
            raise ValueError('Saldo precisa ser numérico')

    def depositar(self, valor):
        if isinstance(valor, (int, float)):
            self.saldo += valor
        else:
            raise ValueError('Saldo precisa ser numérico')

    @abstractmethod
    def sacar(self):
        pass


class ContaPoupanca(Conta):
    def sacar(self, valor):
        if isinstance(valor, (int, float)):
            if valor <= self.saldo:
                self.saldo -= valor
                print(f'Você sacou R$ {valor}, seu saldo é de R$ {self.saldo}')
            else:
                print(f'Saldo insuficiente! Você tem apenas R$ {self.saldo} de saldo na conta')
        else:
            raise ValueError('Valor do saque precisa ser numérico!')


class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite=100):
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor):
        if isinstance(valor, (int, float)):
            if valor <= (self.saldo + self.limite):
                self.saldo -= valor
                print(f'Você sacou R$ {valor}, seu saldo é de R$ {self.saldo}')
            else:
                print(f'Saldo insuficiente! Você tem apenas R$ {self.saldo} de saldo na conta')
        else:
            raise ValueError('Valor do saque precisa ser numérico!')
