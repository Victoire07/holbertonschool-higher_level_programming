from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route("/products")
def products():
    source = request.args.get("source")
    product_id = request.args.get("id")

    products_list = []         # contiendra tous les produits vide pour l'instant!!
    error_message = None       # Si erreur source inconnue ou id introuvable


    return render_template('product_display.html',
                           products=products_list,
                           error=error_message)

