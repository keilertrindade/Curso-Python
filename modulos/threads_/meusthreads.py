from time import sleep
from threading import Thread
from threading import Lock

"""class MeuTrhead(Thread):
    def __init__(self, texto, tempo):
        self.texto = texto
        self.tempo = tempo

        super().__init__()  #Podemos usar Thread.__init__(self) também

    def run(self):
        sleep(self.tempo)
        print(self.texto)


t1 = MeuTrhead('Trhead 1', 5)
t1.start()

t2 = MeuTrhead('Trhead 2', 3)
t2.start()

t3 = MeuTrhead('Trhead 3', 2)
t3.start()


for i in range(20):
    print(i)
    sleep(1)
"""

"""
def vai_demorar(texto, tempo):
    sleep(tempo)
    print(texto)


t = Thread(target=vai_demorar, args=('Olá mundo 1!', 5))
t.start()

t2 = Thread(target=vai_demorar, args=('Olá mundo 2!', 1))
t2.start()

t3 = Thread(target=vai_demorar, args=('Olá mundo 3!', 2))
t3.start()


for i in range(20):
    print(i)
    sleep(0.5)
"""
# ------------------------------------------
"""def vai_demorar(texto, tempo):
    sleep(tempo)
    print(texto)

t = Thread(target=vai_demorar, args=('Olá mundo 1!', 10))
t.start()

while t.is_alive():
    print('Esperando a thread.')
    sleep(2)
"""


class Ingressos:
    def __init__(self, estoque):
        self.estoque = estoque
        self.lock = Lock()

    def comprar(self, quantidade):
        self.lock.acquire()  # tranca o método impedindo que outra thread "entre"
        if self.estoque < quantidade:
            print('Não temos ingressos suficientes')
            self.lock.release()
            return

        sleep(1)

        self.estoque -= quantidade
        print(f'Você comprou  {quantidade} ingresso(s). '
              f'Ainda temos {self.estoque} no estoque')

        self.lock.release()  # libera para as outras threads


ingressos = Ingressos(10)

for i in range(1, 20):
    thread = Thread(target=ingressos.comprar, args=(i,))
    thread.start()
