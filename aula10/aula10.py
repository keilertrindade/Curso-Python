"""

Condições IF, ELIF e ELSE



if True:
    print("Verdadeiro.")
else:
    print('Não é verdadeiro.')
"""
"""

Operadores relacionais

== igualdade  

> maior que  ---  >= maior ou igual

< menor que  ---  <= menor ou igual 

!= diferente



nome = input("Qual o seu nome ? ")
idade = int(input("Qual a sua idade ? "))

#  limite para pegar empréstimo
idade_menor = 20  # muito jovem
idade_maior = 30  # passou da idade

if idade >= idade_menor and idade <= idade_maior:
    print(f'{nome} pode pegar o empréstimo!')
else:
    print(f'{nome} não pode pegar o empréstimo!')
    
"""


"""

OPERADORES LÓGICOS

and -> As duas precisam ser verdadeiras para retornar TRUE

or -> Uma das expressões precisa ser verdadeira para retornar TRUE 

not -> "Inverte" a expressão. Também usado para verificar se a variável está vazia ou tem valor de 0 (booleano falso)


in -> Verifica se algo existe dentro da outra expressão
 
not in -> Verifica se algo não existe dentro da outra expressão

"""

"""usuario = input('Nome de usuário: ')
senha = input('Senha do usuário: ')

usuario_bd = 'keiler'
senha_bd = '123456'

if usuario_bd == usuario and senha_bd == senha:
    print('Você está logado no sistema')
else:
    print('Usuário ou senha inválidos')"""

