"""
No Python, o comportamento dos operadores é definido por métodos especiais.
Vamor alterar o comportamento de operadores com classes definidas pelo usuário.
"""

class Retangulo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        return Retangulo(novo_x, novo_y)

    def get_area(self):
        return self.x * self.y


    def __lt__(self, other): #Sobreescrevendo o método 'menor que'  "<"
        if self.get_area() < other.get_area():
            return True
        else:
            return False

    def __gt__(self, other): #Sobreescrevendo o método 'maior que'  ">"
        if self.get_area() > other.get_area():
            return True
        else:
            return False


    def __eq__(self, other): #Sobreescrevendo o método 'maior que'  ">"
        if self.get_area() == other.get_area():
            return True
        else:
            return False


    def __repr__(self):
        return f"<class 'Retangulo({self.x}, {self.y})'>"



r1 = Retangulo(10, 20)
r2 = Retangulo(10, 20)
print(r1)

"""
Ao usar o sinal de adição antes de declamar a sobreposição do método da o erro
TypeError: unsupported operand type(s) for +: 'Retangulo' and 'Retangulo'

Usamos o __add__ e definimos o método para quando usarmos o operador ' + '



"""