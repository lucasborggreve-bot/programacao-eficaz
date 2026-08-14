import json

def load_data(notes):
    with open(f'static/data/{notes}', 'r', encoding='utf-8') as arquivo:
        return json.load(arquivo)

def load_template(template):
    with open(f'static/templates/{template}', 'r', encoding='utf-8') as arquivo:
        return arquivo.read()