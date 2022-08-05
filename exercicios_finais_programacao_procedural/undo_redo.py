"""
Faça uma lista de tarefas com as seguintes opções:
    adicionar tarefa
    listar tarefas
    opçõo de desfazer (a cada vez que chamarmos, desfaz a última ação. Podendo voltar até o final)
    opção de refazer (a cada que chamarmos, refaz a última ação)
"""

#
# variavel para salvar ultima operação
# Usar um while true
# variável para ultima operacao (?)
#


tarefas = []
redo_tarefas = []


def adicionar_tarefa(lista, tarefa):
    lista.append(tarefa)
    print(f'Tarefa: {tarefa} adicionada com sucesso!\n\n')


def listar_tarefa():
    print(f'\nListando tarefas: \n')
    print(tarefas)
    print(f'\n')


def desfazer(lista, desfazer):
    desfazer.append(lista[-1])
    lista.pop()

def refazer(lista, desfazer):
    lista.append(desfazer.pop())


while True:
    opcao = int(input(f'Escolha a opção: \n'
          f'1- Adicionar tarefa. \n'
          f'2- Listar tarefas. \n'
          f'3- Desfazer ação. \n'
          f'4- Refazer ação.\n'
          f'Opção: '
        )
    )

    if opcao == 1:
        tarefa = input(f'\nDigite a tarefa que irá ser adicionada: ')
        adicionar_tarefa(tarefas, tarefa)

    elif opcao == 2:
        listar_tarefa()

    elif opcao == 3:
        desfazer(tarefas, redo_tarefas)


    elif opcao == 4:
        refazer(tarefa, redo_tarefas)

