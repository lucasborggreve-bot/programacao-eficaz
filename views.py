from utils import load_data, load_template,recebe_anotacao, deleta_anotacao


def index():
    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(note_id = dados[0], title=dados[1], details=dados[2])
        for dados in load_data()
    ]
    notes = '\n'.join(notes_li)

    return load_template('index.html').format(notes=notes)

def submit(titulo,detalhes):

    note = {"titulo" : titulo, "detalhes": detalhes}
    recebe_anotacao(note)
    return

def delete(note_id):
    deleta_anotacao(note_id)
    return