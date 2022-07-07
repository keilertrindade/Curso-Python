"""
Listas em Python
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range

"""


"""lista = list(range(1, 10))
lista = ['String', True, 10, -20.5]
print(lista)
soma = 0

for elem in lista:
    print(f'O tipo do valor: {elem} é {type(elem)}')
"""

"""chances = 3
secreto = 'perfume'
digitadas = []

while True:
    if chances <= 0:
        print('Você perdeu!')
        break
    print()
    letra = input('Digite uma letra: ')

    if len(letra) > 1 or letra.isnumeric() is True:
        print('Isso não vale, digite apenas uma letra!')
        continue

    digitadas.append(letra)
    if letra in secreto:
        print(f'A letra "{letra}" existe na palavra secreta!')
    else:
        print(f'A letra "{letra}" não existe na palavra secreta!')
        digitadas.pop()
        chances -= 1
        print(f'Você ainda tem {chances} chances.')

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'


    if secreto_temporario == secreto:
        print(f'Você ganhou!! A palavra era: {secreto_temporario}')
        break
    else:
        print(f'A palavra secreta é: {secreto_temporario}')
"""