import sqlite3

def criar_tabela():
    conexao = sqlite3.connect("banco.db")
    cursor = conexao.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS note (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    content TEXT
);""")
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