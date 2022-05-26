"""
While
utilizado para realizar ações enquanto uma condigção for verdadeira.

Requisitos: Entender condições e operadores

"""

"""x = 0
while x < 10:
    if x == 3:
        x += 1
        # continue  # Evita a execução das linhas posteriores
        break # Encerra o loop 

    print(x)
    x += 1

print('Acabou!')
"""

x = 0
y = 0

while x < 10:
   y = 0
   while y < 5:
       print(f'({x},{y})')
       y += 1
   x += 1

print('Acabou!')