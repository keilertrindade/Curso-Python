def convert_numero(valor):
    try:
        valor = int(valor)
        return valor
    except ValueError:
        try:
            valor = float(valor)
            return valor
        except ValueError:
            pass


while True:
    numero = convert_numero(input('Digite um numero: '))
    if numero is None:
        print('Erro: isso não é numero.')
    else:
        print(numero * 5)

