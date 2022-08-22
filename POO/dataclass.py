"""
O módulo Dataclasses fornece um decorador e funções para criar automaticamente métodos, como
__init(), __repr()__, __eq__ etc em classes definidas pelo usuário.

Basicamente, dataclasses são syntax surgar para criar classes normais.
Foi originalmente descrito na PEP 557. Adicionado na versão 3.7 do Python.

Documentação disponível em: https://docs.python.org/pt-br/3/library/dataclass.html
"""

from dataclasses import dataclass, field, asdict, astuple


@dataclass(eq=True, repr=True, order=True, frozen=False, init=True)
# init = Criar o método de forma automática ou não
# eq = 'True' permite a comparação de objetos, com o '=='
# order = 'True' permite a ordenação de objetos da classe
# frozen = 'True' impede a edição de nenhum valor da classe, ela fica imutável

class Pessoa:
    nome: str
    sobrenome: str # = field(repr=False)   "field(repr=False)" -> Impede que esse campo apareça no repr (print)

    def __post_init__(self):
        self.nome_completo = f'{self.nome} {self.sobrenome}'


p1 = Pessoa(3333333, 'Trindade')

print(p1)

