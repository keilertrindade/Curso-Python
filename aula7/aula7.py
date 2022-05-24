nome = 'Luiz Otávio'
idade = 32
altura = 1.80
e_maior = idade > 18
peso = 80
data_atual = 2022
imc = peso/altura ** 2

# print(nome, 'tem', idade, 'anos de idade e seu imc é: ', imc)

print(f'{nome} tem {idade} anos de idade e seu IMC é: {imc:.2f}')
print('{} tem {} anos de idade e seu IMC é: {:.2f}'.format(nome, idade, imc))
