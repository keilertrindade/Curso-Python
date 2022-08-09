from pessoa import Pessoa


p1 = Pessoa('Keiler', 26)
p2 = Pessoa.por_ano_nascimento('Joana', 1995)

# print(p1.ano_nascimento())
# print(p2.ano_nascimento())

print(p1.gera_id())
print(Pessoa.gera_id())
print(p2)

print(p2.nome, p2.idade)



