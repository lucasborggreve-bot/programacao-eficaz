import sqlite3


def recebe_anotacao(note):
    conexao = sqlite3.connect("banco.db")
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO note (title,content) VALUES(?,?)",(note['titulo'],note['detalhes']))
    conexao.commit()
    conexao.close()
    

def load_data():
    conexao = sqlite3.connect("banco.db")
    cursor = conexao.cursor()
    execucao = cursor.execute("SELECT * FROM note")
    recuperacao = execucao.fetchall()
    conexao.close()
    return recuperacao



def load_template(template):
    with open(f'static/templates/{template}', 'r', encoding='utf-8') as arquivo:
        return arquivo.read()



def deleta_anotacao(note_id):
    conexao = sqlite3.connect("banco.db")
    cursor = conexao.cursor()
    cursor.execute ("DELETE FROM note WHERE id = ? ",(note_id,))
    conexao.commit()
    conexao.close()