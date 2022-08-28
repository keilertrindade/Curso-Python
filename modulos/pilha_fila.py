"""
Pilhas e filas
Pilha (stack) - LIFO - last in, first out.
    Exemplo: Pilha de livros que são adicionados um sobre o outro
    lista.append() e lista.pop()


Fila (queue) - FIFO - first in, first out
    Exemplo: Fila de banco

Filas podem ter efeitos colaterais em desempenho, pois a cada item alterado todos os itens são modificados

"""

from collections import deque
fila = deque()
#fila = deque(maxlen=5) Ao adicionar um elemento acima do tamanho máximo, o primeiro inserido será removido
#fila.insert(indice,valor) -> Adiciona o valor na posição do indice, movendo os outros valores para o final, se fila
#estiver cheia da erro

fila.append('Joãozinho')
fila.append('Maria')
fila.append('Keiler')
fila.append('Marcos')
fila.append('José')
print(fila)
fila.popleft()  #Remove o primeiro elemento
