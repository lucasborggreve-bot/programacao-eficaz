import sqlite3
from dataclasses import dataclass


@dataclass
class Note:
    id: int
    title: str
    content: str


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




def edita_anotacao(note,note_id):
    conexao = sqlite3.connect("banco.db")
    cursor = conexao.cursor()
    cursor.execute("UPDATE note SET title = ?, content = ? WHERE id = ?",(note["titulo"],note["detalhes"], note_id))
    conexao.commit()
    conexao.close()
    return

def busca_anotacao(note_id):
    conexao = sqlite3.connect("banco.db")
    cursor = conexao.cursor()
    execucao = cursor.execute("SELECT id,title,content FROM note WHERE id = ?", (note_id,))
    recuperacao = execucao.fetchone()
    conexao.close()
    return Note(*recuperacao) if recuperacao else None
