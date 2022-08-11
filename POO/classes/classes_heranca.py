class Pessoa:
    def __init__(self, nome, idade):
        self.idade = idade
        self.nome = nome

    def falar(self):
        print(f'{self.nome} está falando...')

class Cliente(Pessoa):
    pass


class Aluno(Pessoa):
    pass

class ClienteVIP(Cliente):
    def falar(self):
        print(f'Cliente VIP falando.')


class A:
    def falar(self):
        print('Falando... Estou em A.')


class B(A):
    def falar(self):
        print('Falando... Estou em B.')


class C(B, A):
    pass