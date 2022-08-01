import sys
import time

# listas, tuplas, string -> sequencias -> Iterável
# for converte automaticamente em tempo de execução a variavel para iterador e vai usando o next
# podemos converter a variável para iterador usando o metodo var = iter(var) para poder usarmos o metodo next
# print(next(var))


"""def gera():

    for n in range(100):
        yield n
        time.sleep(0.1)


g = gera()
print(next(g))
print(next(g))"""

l1 = [x for x in range(10000)]  #cria lista
print(sys.getsizeof(l1))

l2 = (x for x in range(10000)) #cria gerador
print(sys.getsizeof(l2))

for v in l2:
    print(v)

