from datetime import datetime
from random import randint

class Pessoa:
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))


    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

    @staticmethod
    def gera_id(): # Função normal, mas não podemos usar nem self nem metodos da classe, podemos chamar pela classe ou pelo objeto
        rand = randint(10000, 19999)
        return rand

    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar enquanto come')
            return
        if self.falando:
            print(f'{self.nome} já está falando')
            return
        print(f'{self.nome} está falando sobre {assunto}')
        self.falando = True

    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} parou de falar')
            self.falando = False
            return

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo')
            return
        if self.falando:
            print(f'{self.nome} não pode comer falando')
            return

        print(f'{self.nome} está comendo {alimento}.')
        self.comendo = True

    def parar_comer(self):
        if not self.comendo:
            print(f'{self.comendo} não está comendo.')
            return
        print(f'{self.nome} parou de comer')
        self.comendo = False

    def ano_nascimento(self):
        return self.ano_atual - self.idade
