from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact_page():
    return render_template('contact.html')

@app.route('/items')
def items():
    try:
        with open('items.json') as f:
            data = json.load(f)  # transforme le JSON en dictionnaire Python

        # Récupère la liste des items
        items_list = data.get('items', [])  # si 'items' n'existe pas dcp retourne liste vide !

    except Exception as erreur:
        print(f"Erreur lors de la lecture du fichier JSON : {erreur}")
        items_list = []

    # Passation de la liste au template
    return render_template('items.html', items=items_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
