"""

Criar estrutura de repetição, usando dois contadores um contando de maneira progressiva e um contando de maneira regres-
siva

"""

"""progressivo = 0
regressivo = 10

while progressivo <= 10:
    print(progressivo, regressivo)
    progressivo += 1
    regressivo -= 1
"""

# Solução do professor:

for r, p in enumerate(range(10, 1, -1)):
    print(p, r)
