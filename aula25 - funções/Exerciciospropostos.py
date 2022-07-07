"""
Função que exibe saudação com parametros saudação e nome
"""


def saudacao(saudacao, nome):
    print(f"{saudacao} {nome}")


"""Soma 03 numeros"""


def soma(n1, n2, n3):
    conta = n1 + n2 + n3
    print(conta)


"""Recebe dois números, Retorne o valor do primeiro somado do aumento do percentual dele mesmo"""


def porcentagem(valor, percentual):
    return percentual + (valor * percentual / 100)


"""Se o parametro for divisel por 2 retorna fizz, se for divisivel por 5 retorna buzz, se for divisel por 5 e 3 
retorne FizzBuzz, caso contrário retorne o numero enviado """


def FizzBuzz(numero):
    if numero % 5 == 0 and numero % 3 == 0:
        return 'FizzBuzz'
    if numero % 3 == 0:
        return 'fizz'
    if numero % 5 == 0:
        return 'buzz'
    return numero


""" Função1 que recebe uma função2 como parâmetro e retorne o valor da função2 executada """


def funcao2():
    return 'Olá Mundo!'


def funcao1(funcao):
    return funcao()


# print(funcao1(funcao2))


""" Função1 recebe função2 como parâmetro e retorna o valor da função executada. Faça a função1 executar duas funções
que recebam um número diferente de argumentos """

def mestre (funcao, *args, **kwargs):
    return funcao(*args, **kwargs)

def fala_oi(nome):
    return f'Oi {nome}'

def saudacao(nome, saudacao):
    return f'{saudacao}, {nome}'

executando = mestre(fala_oi, 'Keiler')
print(executando)