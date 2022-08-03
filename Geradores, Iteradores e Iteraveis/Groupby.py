from itertools import groupby, tee

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Leticia', 'nota': 'B'},
    {'nome': 'Rosemary', 'nota': 'A'},
    {'nome': 'Joana', 'nota': 'C'},
    {'nome': 'João', 'nota': 'D'},
    {'nome': 'Eduardo', 'nota': 'A'},
    {'nome': 'André', 'nota': 'B'},
    {'nome': 'Anderson', 'nota': 'C'},
    {'nome': 'José', 'nota': 'B'},
]

ordena = lambda item: item['nota']
alunos.sort(key=ordena)
alunos_agrupados = groupby(alunos, ordena) # Gera um iteravel para cada nota com todos os alunos com essa nota

for agrupamento, valores_agrupados in alunos_agrupados:
    va1, va2 = tee(valores_agrupados) #tee retorna um iterador indepentende de um único iterável, basicamente cópia
    print(f'Agrupamento: {agrupamento}')
    for aluno in va1:
        print(f'\t{aluno}')

    quantidade = len(list(va2))
    print(f'\t{quantidade} alunos tiraram a nota {agrupamento}')
    print()
