"""
public, protected, private -> outras linguagens

_ -> Atributo privado, de maneiro sutil conseguimos acessar colocando o '_' e ele mostra os outros (protected)
__ -> Atributo privado, proibindo o acesso de fora da classe,
Aplicavel também em métodos

"""

class BaseDeDados:
    def __init__(self):
        self.__dados = {}


    @property
    def dados(self):
        return self.__dados


    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})


    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self.__dados['clientes'][id]




bd = BaseDeDados()
bd.inserir_cliente(1, 'Keiler')
bd.inserir_cliente(2, 'João')
bd.inserir_cliente(3, 'Rose')
bd.lista_clientes()
bd.apaga_cliente(2)
bd.__dados = 'Outra coisa' # Como o atributo é privado "forte", essa linha vai criar uma nova variavel e não alterará
# a variavel da classe
print(bd._BaseDeDados__dados) #Só assim acessaremos a variavel da privada da classe


bd.lista_clientes()

