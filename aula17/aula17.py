"""
While /Else
contadores
acumuladores -> Incremento não linear


"""

contador = 1
acumulador = 1

while contador <= 10:
    print(contador, acumulador)
    acumulador = acumulador + contador
    contador += 1
else:
    print()
    print("Cheguei no Else")
