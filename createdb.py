import sqlite3

con = sqlite3.connect('banco.db')
cur = con.cursor()
cur.execute('''
CREATE TABLE note(id INTEGER PRIMARY KEY,
title TEXT,
content TEXT)
''')

con.commit()
con.close()
