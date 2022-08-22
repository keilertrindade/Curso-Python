class MinhaLista:
    def __init__(self):
        self.__itens = []
        self.__index = 0

    def add(self, valor):
        self.__itens.append(valor)

    def __getitem__(self, index):
        try:
            return self.__itens[index]
        except IndexError:
            raise IndexError('Index não está na lista')

    def __setitem__(self, index, valor):
        if index >= len(self.__itens):
            self.add(valor)
        self.__itens[index] = valor

    def __delitem__(self, index):
        if index >= len(self.__itens):
            raise IndexError('Index não está na lista')
        del self.__itens[index]

    def __iter__(self):
        return self

    def __next__(self):
        try:
            item = self.__itens[self.__index]
            self.__index += 1
            return item
        except IndexError:
            raise StopIteration

    def __str__(self):
        return f'{self.__class__.__name__}({self.__itens})'


lista = MinhaLista()
lista.add('Keiler')
lista.add('EuMesmo')
lista.add('Trindade')
print(lista)
del lista[1]
print(lista)

