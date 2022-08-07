def remover_caracteres(cnpj):
    return gerar_primeiro_digito(cnpj.replace('/', '').replace('.', '').replace('-', ''))


def gerar_primeiro_digito(cnpj):
    valores = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    cnpj = list(cnpj)
    cnpj = cnpj[0:12]
    lista = []
    for digito in range(12):
        # cnpj[digito] = int(cnpj[digito])
        lista.append(int(cnpj[digito]) * valores[digito])

    digito = 11 - (sum(lista) % 11)

    if digito > 9:
        cnpj.append('0')
    else:
        cnpj.append(f'{digito}')

    return gerar_segundo_digito(cnpj)


def gerar_segundo_digito(cnpj):

    valores = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    lista = []

    for digito in range(13):
        # cnpj[digito] = int(cnpj[digito])
        lista.append(int(cnpj[digito]) * valores[digito])

    digito = 11 - (sum(lista) % 11)
    if digito > 9:
        cnpj.append('0')
    else:
        cnpj.append(f'{digito}')


    return ''.join(cnpj)

def validar(cnpj, cnpj_gerado):
    cnpj2 = cnpj.replace('/', '').replace('.', '').replace('-', '')
    if cnpj2 == cnpj_gerado:
        return f'CNPJ {cnpj} válido'
    else:
        return f'CNPJ {cnpj} inválido'