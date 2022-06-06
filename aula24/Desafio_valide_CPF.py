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
cpf_verificador = cpf.split('-')[1]
cpf_01 = cpf.split('-')[0].replace('.', '')
# cpf_verificador = cpf_dividido[1]

novo_cpf = ''
cont = 0
soma_01 = 0
soma_02 = 0

for r in range(10, 1, -1):
    soma_01 = soma_01 + (int(cpf_01[cont]) * r)
    cont += 1

digito_1 = 11 - (soma_01 % 11)

if digito_1 > 9:
    digito_1 = '0'
else:
    digito_1 = str(digito_1)


print(soma_01, digito_1)

cpf_01 = cpf_01 + digito_1
print(cpf_01)


cont = 0
for r in range(11, 1, -1):
    soma_02 = soma_02 + (int(cpf_01[cont]) * r)
    cont += 1

digito_2 = 11 - (soma_02 % 11)

if digito_2 > 9:
    digito_2 = '0'
else:
    digito_2 = str(digito_2)

cpf_01 = cpf_01 + digito_2

if cpf_01 == cpf.replace('.', '').replace('-', ''):
    print('CPF Válido')
else:
    print('CPF Inválido')