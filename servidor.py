from flask import Flask, render_template_string, request, redirect
import views


app = Flask(__name__)



# Configurando a pasta de arquivos estáticos
app.static_folder = 'static'

@app.route('/')
def index():

    return render_template_string(views.index())

@app.route('/submit', methods=['POST'])

def submit_form():
    titulo = request.form.get('titulo') 
    detalhes = request.form.get('detalhes') 
    views.submit(titulo, detalhes)
    return redirect('/')

@app.route('/delete', methods = ["POST"])
def delete_form():
    delete = request.form.get("id")
    views.delete(delete)
    return redirect ('/')

@app.route('/update', methods=['GET'])
def recebe_edit_form():
    note_id = request.args.get("id")
    nota = views.busca_nota(note_id)
    return render_template_string(views.edit(nota))

@app.route('/update', methods = ["POST"])
def edit_form():
    note_id = request.form.get("id")
    titulo = request.form.get("titulo")
    detalhes = request.form.get("detalhes")
    views.salva_edit(note_id,titulo,detalhes)
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)