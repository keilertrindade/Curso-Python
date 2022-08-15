from POO.classes.classes_abstratas import Conta

class ContaPoupanca(Conta):

    def sacar(self, valor):
        if self._saldo < valor:
            print('Saldo insuficiente')
            return

        self._saldo -= valor
        self.detalhes()


class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite=100):
        super().__init__(agencia, conta, saldo)
        self._limite = limite

    @property
    def limite(self):
        return self._limite

    def sacar(self, valor):
        if (self._saldo + self._limite) < valor:
            print('Saldo insuficiente')
            return

        self._saldo -= valor
        self.detalhes()





cp = ContaPoupanca(1111,2222, 10)
cp.sacar(5)
cp.depositar(10)
cp.sacar(5)
print('################')

cc = ContaCorrente(1111, 3333, 0, 300)
cc.depositar(100)
cc.sacar(250)
cc.sacar(250)


