import sqlite3


class AgendaDB:
    def __init__(self, arquivo):
        self.conn = sqlite3.connect(arquivo)
        self.cursor = self.conn.cursor()

    def inserir(self, nome, telefone):
        consulta = 'INSERT OR IGNORE INTO agenda (nome, telefone) VALUES (?,?)'
        self.cursor.execute(consulta, (nome, telefone))
        self.conn.commit()
        pass

    def editar(self, nome, telefone, id):
        consulta = 'UPDATE OR IGNORE agenda SET nome=?, telefone=? WHERE id=?'
        self.cursor.execute(consulta, (nome, telefone, id))
        self.conn.commit()
        pass

    def excluir(self, id):
        consulta = 'DELETE FROM agenda WHERE id=?'
        self.cursor.execute(consulta, (id,))
        self.conn.commit()
        pass

    def listar(self):
        self.cursor.execute('SELECT * FROM agenda')
        for linha in self.cursor.fetchall():
            print(linha)

    def buscar(self, valor):
        consulta = 'SELECT * FROM agenda WHERE nome LIKE ?'
        self.cursor.execute(consulta, (f'%{valor}%',))
        for linha in self.cursor.fetchall():
            print(linha)

    def fechar(self):
        self.cursor.close()
        self.conn.close()



if __name__ == '__main__':

    agenda = AgendaDB('agenda.db')

    # agenda.inserir('Keiler', '111111')
    # agenda.inserir('João', '222222')
    # agenda.inserir('Rose', '123456')
    # agenda.inserir('Guilherme', '444444')
    # agenda.inserir('Fabricio', '555555')
    # agenda.inserir('Mais um', '666666')

    agenda.inserir('Luiz Otávio', '566666')
    agenda.inserir('Luiz Felipe', '546666')
    agenda.inserir('Ronaldo Luiz', '536666')
    agenda.inserir('Luiza Maria', '526666')
    agenda.inserir('Luiza Maria casa do caralho', '516666')



    agenda.editar('Francisco', '131313', 9)
    agenda.excluir(8)
    agenda.buscar('luiz')
