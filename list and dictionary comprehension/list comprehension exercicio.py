"""
Criar lista utilizando a variavel string separando em blocos de '0123456789'. Após isso gerar uma string em que cada
bloco está separado por um '.'
"""

string = '01234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789'
lista = [string[indice:indice+10] for indice in range(0, len(string), 10)]
retorno = '.'.join(lista)
print(lista)
print(retorno)