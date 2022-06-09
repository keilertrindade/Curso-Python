"""

CPF = 168.995.350-09
---------------------------
1 * 10 = 10                        1 * 11 = 11
6 * 09 = 54                        6 * 10 = 60
8 * 08 = 64                        8 * 09 = 72
9 * 07 = 63                        9 * 08 = 72
9 * 06 = 54                        9 * 07 = 63
5 * 05 = 25                        5 * 06 = 30
3 * 04 = 12                        3 * 05 = 15
5 * 03 = 15                        5 * 04 = 20
0 * 02 = 0                         0 * 03 = 0
                                -> 0 * 02 = 0

        297                             343
11 - (297 % 11) = 11               11 - (343 % 11) = 9
11 > 9 = 0 #se resultado for menor que 9, vale o numero
Digito 1 = 0                           Digito 2 = 9

"""

cpf = '168.995.350-09'
# cpf = input('Digite seu CPF no seguinte formato xxx.xxx.xxx-xx : ')
cpf_verificador = cpf.split('-')[0].replace('.', '')

cont = 0
soma = 0

for r in range(10, 1, -1):
    soma = soma + (int(cpf_verificador[cont]) * r)
    cont += 1

digito_verificador = 11 - (soma % 11)
digito_maior = (digito_verificador > 9)

cpf_verificador = cpf_verificador + '0' if digito_maior else cpf_verificador + str(digito_verificador)

soma = 0
cont = 0

for r in range(11, 1, -1):
    soma = soma + (int(cpf_verificador[cont]) * r)
    cont += 1

digito_verificador = 11 - (soma % 11)
digito_maior = (digito_verificador > 9)

cpf_verificador = cpf_verificador + '0' if digito_maior else cpf_verificador + str(digito_verificador)

if cpf_verificador == cpf.replace('.', '').replace('-', ''):
    print('CPF Válido')
else:
    print('CPF Inválido')


