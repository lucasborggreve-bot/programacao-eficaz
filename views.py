from utils import load_data, load_template
import json

def index():
    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(title=dados['titulo'], details=dados['detalhes'])
        for dados in load_data()
    ]
    notes = '\n'.join(notes_li)

    return load_template('index.html').format(notes=notes)

def submit(titulo,detalhes):
    notes = load_data()
    note = {"titulo" : titulo, "detalhes": detalhes}
    notes.append(note)
    with open(f'static/data/notes.json', 'w') as arquivo:
        return json.dump(notes,arquivo)