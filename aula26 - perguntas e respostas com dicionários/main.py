perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2+2 ? ',
        'resposta': {
            'a': '1',
            'b': '4',
            'c': '5',
            'd': '7',
        },
        'resposta_certa': 'b',
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 3*2 ? ',
        'resposta': {
            'a': '6',
            'b': '4',
            'c': '5',
            'd': '9',
        },
        'resposta_certa': 'a',
    },
    'Pergunta 3': {
        'pergunta': 'Quanto é 8/2 ? ',
        'resposta': {
            'a': '1',
            'b': '4',
            'c': '5',
            'd': '7',
        },
        'resposta_certa': 'b',
    },
}

respostas_certas = 0
for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')

    print('Escolha a resposta:')
    for rk, rv in pv['resposta'].items():
        print(f'[{rk}]: {rv}')

    resposta_usuario = input("Digita sua resposta: ")
    if resposta_usuario == pv['resposta_certa']:
        respostas_certas += 1

    print()

print(f'Você acertou {respostas_certas} perguntas!')
