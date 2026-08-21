from utils import load_data, load_template,recebe_anotacao, deleta_anotacao,edita_anotacao,busca_anotacao


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

def edit(note):
    edit_template = load_template('components/edit.html')
    return edit_template.format(note_id = note[0], title = note[1], details = note[2])
    

def busca_nota(note_id):
    return busca_anotacao(note_id)

def salva_edit(note_id, titulo, detalhes):
    note = {"titulo": titulo, "detalhes": detalhes}
    return edita_anotacao(note, note_id)