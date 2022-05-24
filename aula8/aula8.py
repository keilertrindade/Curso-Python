nome = 'Keiler Trindade'
idade = 27
altura = 1.66
peso = 56.7
ano_atual = 2022
ano_nascimento = ano_atual - idade
imc = peso / altura ** 2

print('{}  tem {} anos e {} metros de altura.'.format(nome, idade, altura))
print('{} pensa {} quilos e seu IMC é: {:.2f}.'.format(nome, peso, imc))
print('{} nasceu em {}.'.format(nome, ano_nascimento))


print('Acho "Legal ter dois nomes.')