"""
For / Else em Python

for valor in variavel:
    if valor.lower().startswith('k'):
        #print("Começa com K: ", valor)
        comeca_jota = True

if comeca_jota:
    print("Existe uma palavra que começa com K!")
else:
    print('Não existe uma palavra que começa com K!')

"""

variavel = ['Keiler', 'Maria', 'João']
comeca_jota = False

for valor in variavel:
    print(valor)
    if valor.lower().startswith('k'):
        #print('Palavra começa com K!')
        break
else:
    print('Não existe uma palavra que começa com K!')
