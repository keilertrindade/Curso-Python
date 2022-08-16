"""

Em pyhton tudo é um objeto, incluindo classes.
Metaclasses são as "classes" que criam classes.
type é uma metaclasse

"""


class Meta(type):
    def __new__(mcs, name, bases, namespace):
        if name == 'A':
            return type.__new__(mcs, name, bases, namespace)
        print(namespace)
        if 'b_fala' not in namespace:
            print(f'Você precisa criar o método b_fala em {name}')
        else:
            if not callable(namespace['b_fala']):
                print(f'b_fala precisa ser um método, não atributo em {name}.')


class A(metaclass=Meta):
    def fala(self):
        self.b_fala()


class B(A):
    def b_fala(self):
        print("Falando!")

