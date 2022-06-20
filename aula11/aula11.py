
usuario = input('Digite seu usuário: ')
qtd_caracteres = len(usuario)

#  print(f'{usuario} possui {qtd_caracteres} caracteres e a variável é do tipo {type(qtd_caracteres)}')

if qtd_caracteres < 6:
    print('Você precisa digitar pelo menos 06 caracteres')
else:
    print('Você foi cadastrado no sistema')

