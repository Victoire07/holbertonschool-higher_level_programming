from flask import Flask, render_template
import json
import csv

app = Flask(__name__)

@app.route("/products")
def products():
    source = request.args.get("source")
    product_id = request.args.get("id")

    products_list = []         # contiendra tous les produits vide pour l'instant!!
    error_message = None       # Si erreur source inconnue ou id introuvable

    if source == "json":
        try:
            with open("products.json") as fichier:
                data = json.load(fichier)
                products_list = data
        except Exception as erreur:
            error_message = f"Erreur lecture JSON : {erreur}"

    return render_template('product_display.html',
                           products=products_list,
                           error=error_message)

