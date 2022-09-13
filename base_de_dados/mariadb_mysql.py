# pip install pymysql
# pip install cryptography
# pip install PyMySQL[rsa]

import pymysql.cursors

conexao = pymysql.connect(
    host='127.0.0.1',
    user='keiler',
    password='',
    port=3308,
    db='montepascoal',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor

)

cursor = conexao.cursor()
query = 'SELECT * FROM atletas'
cursor.execute(query)
resultado = cursor.fetchone()

print(resultado)

cursor.close()
conexao.close()
