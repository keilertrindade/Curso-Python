class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual / 100))


    # Getter
    @property
    def preco(self):
        return self._preco  # convenção

    # Setter
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = valor.replace('R$', '')
            valor = float(valor)
        self._preco = valor

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor.title()






p1 = Produto('CaMiSeTa', 50)
p1.desconto(10)
print(p1.nome, p1.preco)

p2 = Produto('CaNeCa', 'R$ 15')
p2.desconto(10)
print(p2.nome, p2.preco)
