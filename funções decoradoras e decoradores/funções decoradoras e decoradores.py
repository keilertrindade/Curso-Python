def master(funcao): #Função decoradora
    def slave(*args, **kwargs): #No teste da outra_funcao() caso não tenha os *args e **kwargs dará erro
        print('Agora estou decorada.')
        funcao(*args, **kwargs)
    return slave

@master #decorador
def fala_oi():
    print('Oi')

"""  """
@master
def outra_funcao(msg):
    print(msg)

# fala_oi()
outra_funcao('1321.2')

from time import time
from time import sleep

def velocidade(funcao):
    def interna(*args, **kwargs):
        start_time = time()
        resultado = funcao(*args, **kwargs)
        end_time = time()
        tempo = (end_time - start_time) * 1000
        print(f'A função {funcao.__name__} levou {tempo:.2f} ms para executar.')
    return interna

@velocidade
def demora():
    for i in range(5):
        print(i)
        sleep(1)

# demora()