#  Exercicios

# 01 Digitar número inteiro e informar se é par ou impar.
"""  ---> num = input('Por favor digite um número inteiro: ')
try:
    num = int(num)
    if num % 2 == 0:
        print('Numero par')
    else:
        print('Numero impar')
except:
    print(f'"{num}" não é um número inteiro!')"""


""" ---> horas = input('Por favor informe a hora: ')
try:
    horas = int(horas)
    if horas >= 0 and horas <= 11:
        print('Bom dia!')
    elif horas >= 12 and horas <= 17 :
        print('Boa tarde!')
    elif horas <= 23:
        print('Boa noite!')
    else:
        print('Digite um horário válido (00 às 23)!')
except:
    print(f'"{horas}" não é uma hora válida!')"""

nome = input('Digite seu primeiro nome: ')
if len(nome) <= 4:
    print('Seu nome é curto')

elif len(nome) <= 6:
    print('Seu nome é normal')

else:
    print('Seu nome é muito grande')
