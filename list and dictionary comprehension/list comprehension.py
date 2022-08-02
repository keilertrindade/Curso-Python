# Forma concisa de criar e manipular listas

numeros = [1,2,3,4,5,6,7,8,9,10]
# novos_numeros = [n for n in numeros]

"""
Mesma coisa que: 

novos_numeros = []
for numero in numeros:
    novos_numeros.append(numero)

"""
# divisao = [numero / 2 for numero in numeros]
# print(novos_numeros)
# print(divisao)

novos_numeros = [numero for numero in numeros if numero > 5]
# print(novos_numeros)

outro_if = [
    numero if numero != 6 else 600
    for numero in numeros
    if numero % 2 == 0
]
# print(outro_if)

linhas_colunas = [
    (x,y)
    for x in range (1, 11)
    for y in range (1, 6)
]

# print(linhas_colunas)

string = 'Keiler Trindade'
nova_string = [letra for letra in string]
#print(nova_string)

numeros = [[numero, numero **2] for numero in range(10)]
print(numeros)

flat = [y for x in numeros for y in x]
print(flat)