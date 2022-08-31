import sqlite3
""" https://sqlitebrowser.org/dl/ """


conexao = sqlite3.connect('basededados.db')
cursor = conexao.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS clientes ('
               'id INTEGER PRIMARY KEY AUTOINCREMENT,'
               'nome TEXT,'
               'peso REAL'
               ')')

# cursor.execute('INSERT INTO clientes(nome, peso) VALUES ("Keiler Trindade", 54.6)') -> Forma insegura, habilita sqlinjection

# cursor.execute('INSERT INTO clientes(nome, peso) VALUES (?, ?)', ('Joana', 66.6))
# cursor.execute('INSERT INTO clientes(nome, peso) VALUES (:nome, :peso)', {'nome': 'Joãozinho', 'peso': 25})
# cursor.execute('INSERT INTO clientes VALUES (:id, :nome, :peso)', {'id': None, 'nome': 'Daniel', 'peso': 113})

# cursor.execute('UPDATE clientes SET nome=:nome WHERE id=:id', {'nome': 'Maria', 'id': 2})
# cursor.execute('DELETE FROM clientes WHERE id=:id', {'id': 2})
cursor.execute('SELECT nome, peso FROM clientes WHERE peso > :peso', {'peso': 50})
conexao.commit()
# cursor.execute('SELECT * FROM clientes')

for linha in cursor.fetchall():
    print(linha)

cursor.close()
conexao.close()
