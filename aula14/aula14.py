"""
Formatando valores com modificadores - Aula 5

:s - Texto (strings)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:.(NÚMERO)f - Quantidade de casas decimais (float)
:(CARACTERE) ( > ou < ou ^) (QUANTIDADE) (TIPO - s, d ou f)

> - Esquerda
< - Direita
^ - Centro

"""

"""num_1 = 10
num_2 = 3
divisao = num_1 / num_2
print('{:.2f}'.format(divisao))
print(f'{divisao:.2f}')"""

"""num_1 = 1
print(f'{num_1:0>10}')

num_2 = 1150
print(f'{num_2:.2f}')"""

nome = ' Keiler '
sobrenome = ' Trindade '
maisum = 'mais'
nome_formatado = '{0:$^50} {1:#^50}'.format(nome, sobrenome, maisum)
print(nome_formatado)